"""
SPMH Dashboard — Прокси-сервер для IIKO
==========================================
Запуск:
    python server.py

Затем открой в браузере: http://localhost:5050
"""

from flask import Flask, request, jsonify, send_from_directory, Response
from flask_cors import CORS
import requests
import hashlib
import json
import os

app = Flask(__name__, static_folder='.')
CORS(app)

IIKO_TOKEN = None
IIKO_BASE  = None

# ── Утилиты ─────────────────────────────────────────────
def sha1(password: str) -> str:
    return hashlib.sha1(password.encode('utf-8')).hexdigest()

def iiko_headers():
    return {'Content-Type': 'application/json', 'Accept': 'application/json'}

# ── Главная страница ─────────────────────────────────────
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# ── АВТОРИЗАЦИЯ IIKO ─────────────────────────────────────
@app.route('/proxy/auth', methods=['POST'])
def proxy_auth():
    global IIKO_TOKEN, IIKO_BASE
    data = request.json or {}

    host   = data.get('host', '').rstrip('/')
    login  = data.get('login', '')
    passwd = data.get('password', '')

    if not host or not login:
        return jsonify({'error': 'Укажите хост и логин'}), 400

    IIKO_BASE = host
    pass_hash = sha1(passwd)

    try:
        url = f"{host}/resto/api/auth?login={login}&pass={pass_hash}"
        r = requests.get(url, verify=False, timeout=10)
        if r.status_code != 200:
            return jsonify({'error': f'Ошибка авторизации: HTTP {r.status_code}'}), 401

        token = r.text.strip()
        if len(token) < 10:
            return jsonify({'error': f'Неверный токен: {token}'}), 401

        IIKO_TOKEN = token
        return jsonify({'token': token, 'status': 'ok'})

    except requests.exceptions.SSLError:
        # Retry without SSL verification
        try:
            r = requests.get(url, verify=False, timeout=10)
            IIKO_TOKEN = r.text.strip()
            return jsonify({'token': IIKO_TOKEN, 'status': 'ok'})
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ── СПИСОК ОРГАНИЗАЦИЙ ───────────────────────────────────
@app.route('/proxy/organizations', methods=['GET'])
def proxy_organizations():
    global IIKO_TOKEN, IIKO_BASE
    if not IIKO_TOKEN:
        return jsonify({'error': 'Не авторизован'}), 401
    try:
        url = f"{IIKO_BASE}/resto/api/v2/entities/list?rootType=Corporation&key={IIKO_TOKEN}"
        r = requests.get(url, verify=False, timeout=10)
        return Response(r.content, status=r.status_code, content_type='application/json')
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ── ОТЧЁТ OLAP (продажи) ────────────────────────────────
@app.route('/proxy/olap', methods=['POST'])
def proxy_olap():
    global IIKO_TOKEN, IIKO_BASE
    if not IIKO_TOKEN:
        return jsonify({'error': 'Не авторизован'}), 401
    try:
        body = request.json or {}
        url  = f"{IIKO_BASE}/resto/api/v2/reports/olap?key={IIKO_TOKEN}"
        r = requests.post(url, json=body, verify=False, timeout=30)
        return Response(r.content, status=r.status_code, content_type='application/json')
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ── ПРОДАЖИ ПО ЧАСАМ (упрощённый endpoint) ──────────────
@app.route('/proxy/sales', methods=['POST'])
def proxy_sales():
    global IIKO_TOKEN, IIKO_BASE
    if not IIKO_TOKEN:
        return jsonify({'error': 'Не авторизован'}), 401

    data     = request.json or {}
    date_from = data.get('dateFrom', '')
    date_to   = data.get('dateTo', '')

    olap_body = {
        "reportType": "SALES",
        "buildSummary": True,
        "groupByRowFields": ["OpenDate.Hour"],
        "aggregateFields": ["OrdersCount", "GuestNum", "Revenue", "DiscountSum"],
        "filters": {
            "openDateCustomFrom": f"{date_from} 00:00:00",
            "openDateCustomTo":   f"{date_to} 23:59:59"
        }
    }

    try:
        url = f"{IIKO_BASE}/resto/api/v2/reports/olap?key={IIKO_TOKEN}"
        r   = requests.post(url, json=olap_body, verify=False, timeout=30)

        if r.status_code != 200:
            return jsonify({'error': f'IIKO вернул {r.status_code}: {r.text[:200]}'}), r.status_code

        raw = r.json()
        # Нормализуем в единый формат
        rows = raw.get('data', raw.get('rows', []))
        result = []
        total_rev, total_checks = 0, 0

        for row in rows:
            h   = row.get('OpenDate.Hour', row[0] if isinstance(row, list) else None)
            cnt = int(row.get('OrdersCount', row[1] if isinstance(row, list) else 0) or 0)
            rev = float(row.get('Revenue',     row[2] if isinstance(row, list) else 0) or 0)
            if h is not None:
                result.append({'hour': int(h), 'checks': cnt, 'revenue': rev})
                total_rev    += rev
                total_checks += cnt

        return jsonify({
            'hourly':       sorted(result, key=lambda x: x['hour']),
            'totalRevenue': total_rev,
            'totalChecks':  total_checks,
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ── КАССОВЫЕ СМЕНЫ ──────────────────────────────────────
@app.route('/proxy/cashier-shifts', methods=['POST'])
def proxy_shifts():
    global IIKO_TOKEN, IIKO_BASE
    if not IIKO_TOKEN:
        return jsonify({'error': 'Не авторизован'}), 401
    data = request.json or {}
    try:
        url = f"{IIKO_BASE}/resto/api/v2/cashshifts/list?key={IIKO_TOKEN}"
        r   = requests.post(url, json=data, verify=False, timeout=15)
        return Response(r.content, status=r.status_code, content_type='application/json')
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ── СТАТУС ───────────────────────────────────────────────
@app.route('/proxy/status', methods=['GET'])
def proxy_status():
    return jsonify({
        'connected': IIKO_TOKEN is not None,
        'base': IIKO_BASE,
    })

if __name__ == '__main__':
    import urllib3
    urllib3.disable_warnings()
    print("=" * 50)
    print("  SPMH Dashboard — Прокси-сервер")
    print("=" * 50)
    print("  Открой в браузере: http://localhost:5050")
    print("  Остановить: Ctrl+C")
    print("=" * 50)
    app.run(host='0.0.0.0', port=5050, debug=False)
