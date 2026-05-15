<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SPMH — IIKO + Verifix</title>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600&display=swap" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<style>
:root{
  --bg:#0c0f14;--bg2:#131820;--bg3:#1a2130;
  --gold:#e8b84b;--gold2:rgba(232,184,75,0.12);
  --teal:#2dd4bf;--red:#f87171;--green:#4ade80;--yellow:#fbbf24;
  --muted:#4a5568;--text:#e2e8f0;--text2:#94a3b8;
  --border:rgba(232,184,75,0.12);--card:rgba(20,26,38,0.97);
  --radius:16px;
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--text);font-family:'DM Sans',sans-serif;font-size:15px;line-height:1.6;overflow-x:hidden}
body::before{content:'';position:fixed;inset:0;z-index:0;
  background:radial-gradient(ellipse 80% 60% at 15% 10%,rgba(232,184,75,0.06) 0%,transparent 60%),
             radial-gradient(ellipse 60% 40% at 85% 85%,rgba(45,212,191,0.04) 0%,transparent 60%);
  pointer-events:none}

/* ── TOPBAR ── */
.topbar{position:sticky;top:0;z-index:100;background:rgba(12,15,20,0.92);backdrop-filter:blur(16px);
  border-bottom:1px solid var(--border);padding:0 32px;display:flex;align-items:center;
  justify-content:space-between;height:60px;gap:16px}
.topbar-logo{font-family:'Bebas Neue',sans-serif;font-size:24px;color:var(--gold);letter-spacing:.1em}
.topbar-status{display:flex;align-items:center;gap:8px;font-size:13px;color:var(--text2)}
.dot{width:8px;height:8px;border-radius:50%;background:var(--muted)}
.dot.live{background:var(--green);box-shadow:0 0 8px var(--green);animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.4}}
.topbar-actions{display:flex;gap:8px;align-items:center}
.btn{display:inline-flex;align-items:center;gap:6px;padding:8px 16px;border-radius:10px;
  font-size:13px;font-weight:500;cursor:pointer;border:none;transition:.2s;font-family:'DM Sans',sans-serif}
.btn-ghost{background:rgba(255,255,255,0.05);color:var(--text2);border:1px solid rgba(255,255,255,0.08)}
.btn-ghost:hover{background:rgba(255,255,255,0.09);color:var(--text)}
.btn-gold{background:var(--gold);color:#0c0f14;font-weight:600}
.btn-gold:hover{background:var(--gold2);filter:brightness(1.1)}
.btn-sm{padding:6px 12px;font-size:12px}

/* ── PAGE ── */
.page{position:relative;z-index:1;max-width:1300px;margin:0 auto;padding:32px 24px 80px}

/* ── HERO ── */
.hero{display:flex;align-items:flex-end;justify-content:space-between;
  padding:40px 0 40px;border-bottom:1px solid var(--border);gap:24px;flex-wrap:wrap}
.hero-eyebrow{font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);
  margin-bottom:10px;display:flex;align-items:center;gap:8px}
.hero-eyebrow::before{content:'';width:24px;height:1px;background:var(--gold)}
.hero h1{font-family:'Bebas Neue',sans-serif;font-size:clamp(48px,7vw,88px);
  line-height:.9;letter-spacing:.02em}
.hero h1 span{color:var(--gold)}
.hero-meta{font-size:13px;color:var(--text2);margin-top:14px;display:flex;align-items:center;gap:8px}
.kpis-row{display:flex;gap:3px;flex-wrap:wrap}
.kpi-card{background:var(--bg3);border:1px solid var(--border);border-radius:14px;
  padding:18px 22px;min-width:130px;position:relative;overflow:hidden}
.kpi-card::before{content:'';position:absolute;top:0;left:0;right:0;height:2px}
.kpi-card.ok::before{background:var(--green)}
.kpi-card.bad::before{background:var(--red)}
.kpi-card.warn::before{background:var(--yellow)}
.kpi-card.neu::before{background:var(--gold)}
.kpi-label{font-size:10px;color:var(--text2);letter-spacing:.08em;text-transform:uppercase;margin-bottom:4px}
.kpi-val{font-family:'Bebas Neue',sans-serif;font-size:30px;line-height:1}
.kpi-sub{font-size:11px;margin-top:3px}
.kpi-card.ok .kpi-sub{color:var(--green)}
.kpi-card.bad .kpi-sub{color:var(--red)}
.kpi-card.warn .kpi-sub{color:var(--yellow)}
.kpi-card.neu .kpi-sub{color:var(--gold)}

/* ── SECTIONS ── */
.section{margin-top:48px}
.sec-head{display:flex;align-items:baseline;gap:14px;margin-bottom:24px}
.sec-title{font-family:'Bebas Neue',sans-serif;font-size:26px;letter-spacing:.04em}
.sec-line{flex:1;height:1px;background:var(--border)}
.sec-badge{font-size:10px;color:var(--gold);letter-spacing:.12em;text-transform:uppercase;
  background:rgba(232,184,75,0.08);border:1px solid rgba(232,184,75,0.2);padding:3px 10px;border-radius:20px}

/* ── GRID ── */
.g2{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.g3{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
@media(max-width:860px){.g2,.g3{grid-template-columns:1fr}}

/* ── CARD ── */
.card{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:24px;position:relative;overflow:hidden}
.card-title{font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--gold);
  margin-bottom:18px;display:flex;align-items:center;gap:8px}
.card-title::after{content:'';flex:1;height:1px;background:var(--border)}

/* ── SETTINGS MODAL ── */
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,0.7);backdrop-filter:blur(6px);
  z-index:200;align-items:center;justify-content:center}
.overlay.show{display:flex}
.modal{background:#131820;border:1px solid var(--border);border-radius:20px;
  width:min(620px,95vw);max-height:90vh;overflow-y:auto;padding:32px}
.modal-title{font-family:'Bebas Neue',sans-serif;font-size:28px;color:var(--gold);margin-bottom:6px}
.modal-sub{font-size:13px;color:var(--text2);margin-bottom:28px}
.tabs{display:flex;gap:4px;margin-bottom:24px;background:rgba(255,255,255,0.03);
  padding:4px;border-radius:12px}
.tab{flex:1;padding:8px;border-radius:9px;text-align:center;font-size:13px;font-weight:500;
  cursor:pointer;color:var(--text2);transition:.2s;border:none;background:none;font-family:'DM Sans',sans-serif}
.tab.active{background:var(--gold);color:#0c0f14}
.form-group{margin-bottom:18px}
.form-label{font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--text2);
  margin-bottom:6px;display:block}
.form-input{width:100%;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.1);
  border-radius:10px;padding:10px 14px;color:var(--text);font-size:14px;font-family:'DM Sans',sans-serif;
  outline:none;transition:.2s}
.form-input:focus{border-color:var(--gold);background:rgba(232,184,75,0.04)}
.form-hint{font-size:11px;color:var(--muted);margin-top:4px}
.form-row{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.divider{height:1px;background:var(--border);margin:24px 0}
.tab-panel{display:none}
.tab-panel.active{display:block}
.alert{border-radius:10px;padding:12px 16px;font-size:13px;margin-bottom:16px}
.alert-info{background:rgba(45,212,191,0.08);border:1px solid rgba(45,212,191,0.2);color:var(--teal)}
.alert-warn{background:rgba(251,191,36,0.08);border:1px solid rgba(251,191,36,0.2);color:var(--yellow)}
.modal-actions{display:flex;gap:10px;justify-content:flex-end;margin-top:24px}

/* ── DATA TABLES ── */
.tbl{width:100%;border-collapse:collapse}
.tbl th{font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--gold);
  font-weight:500;padding:9px 10px;border-bottom:1px solid var(--border);text-align:left;white-space:nowrap}
.tbl td{padding:9px 10px;border-bottom:1px solid rgba(255,255,255,0.03);font-size:13px;color:var(--text2)}
.tbl td:first-child{color:var(--text);font-weight:500}
.tbl tr:last-child td{border:none}
.tbl-scroll{overflow-x:auto}

/* ── STATUS BADGE ── */
.badge{display:inline-block;font-size:11px;padding:3px 10px;border-radius:20px;font-weight:500}
.badge-ok{background:rgba(74,222,128,0.1);color:var(--green)}
.badge-bad{background:rgba(248,113,113,0.1);color:var(--red)}
.badge-warn{background:rgba(251,191,36,0.1);color:var(--yellow)}
.badge-neu{background:rgba(232,184,75,0.1);color:var(--gold)}

/* ── HEATMAP ── */
.hm-grid{display:grid;grid-template-columns:repeat(16,1fr);gap:4px}
.hm-cell{aspect-ratio:1;border-radius:6px;display:flex;flex-direction:column;
  align-items:center;justify-content:center;cursor:default;transition:.15s;font-size:8px}
.hm-cell:hover{transform:scale(1.2);z-index:10;box-shadow:0 8px 24px rgba(0,0,0,.5)}
.hm-h{opacity:.7;margin-bottom:1px}
.hm-v{font-size:10px;font-weight:600}

/* ── PROGRESS BAR ── */
.prog-row{margin-bottom:16px}
.prog-meta{display:flex;justify-content:space-between;margin-bottom:5px;align-items:baseline}
.prog-name{font-size:13px;color:var(--text)}
.prog-vals{font-size:12px;color:var(--text2)}
.prog-track{background:rgba(255,255,255,0.05);border-radius:4px;height:7px;position:relative;overflow:hidden}
.prog-bar{height:100%;border-radius:4px;position:absolute;top:0;left:0;transition:width 1s cubic-bezier(.4,0,.2,1)}

/* ── VERIFIX TABLE ── */
.vf-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:10px}
.vf-emp{background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.06);
  border-radius:12px;padding:14px;display:flex;flex-direction:column;gap:4px}
.vf-name{font-size:13px;color:var(--text);font-weight:500}
.vf-role{font-size:11px;color:var(--text2)}
.vf-time{font-size:12px;color:var(--gold);font-weight:500}
.vf-status{font-size:10px}

/* ── LOADING ── */
.loader{display:flex;flex-direction:column;align-items:center;justify-content:center;
  padding:48px;gap:16px;color:var(--text2);font-size:14px}
.spinner{width:36px;height:36px;border:2px solid rgba(232,184,75,0.2);
  border-top-color:var(--gold);border-radius:50%;animation:spin .8s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}

/* ── EMPTY STATE ── */
.empty{text-align:center;padding:48px 24px;color:var(--text2)}
.empty-icon{font-size:40px;margin-bottom:12px;opacity:.5}
.empty-title{font-size:16px;color:var(--text);margin-bottom:6px}
.empty-sub{font-size:13px}

/* ── CONNECTION INDICATOR ── */
.conn-row{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:6px}
.conn-item{display:flex;align-items:center;gap:6px;font-size:12px;color:var(--text2);
  background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.07);
  border-radius:8px;padding:5px 12px}
.conn-dot{width:7px;height:7px;border-radius:50%}
.conn-dot.ok{background:var(--green)}
.conn-dot.err{background:var(--red)}
.conn-dot.off{background:var(--muted)}
.conn-dot.connecting{background:var(--yellow);animation:pulse 1s infinite}

@keyframes fadeUp{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:translateY(0)}}
.animate{opacity:0;animation:fadeUp .5s ease forwards}
</style>
</head>
<body>

<!-- TOPBAR -->
<nav class="topbar">
  <div class="topbar-logo">SPMH</div>
  <div class="conn-row" id="connStatus">
    <div class="conn-item"><span class="conn-dot off" id="iikoDot"></span><span id="iikoLabel">IIKO не подключён</span></div>
    <div class="conn-item"><span class="conn-dot off" id="vfDot"></span><span id="vfLabel">Verifix: ручной режим</span></div>
  </div>
  <div class="topbar-actions">
    <button class="btn btn-ghost btn-sm" onclick="loadDemo()">🎲 Демо</button>
    <button class="btn btn-ghost btn-sm" onclick="refreshData()" id="refreshBtn" style="display:none">↻ Обновить</button>
    <button class="btn btn-gold btn-sm" onclick="openSettings()">⚙ Настройки</button>
  </div>
</nav>

<!-- MAIN -->
<div class="page">

  <!-- HERO -->
  <header class="hero">
    <div class="animate">
      <div class="hero-eyebrow">Планирование персонала · IIKO + Verifix</div>
      <h1>SPM<span>H</span></h1>
      <div class="hero-meta" id="heroMeta">
        <svg width="13" height="13" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
        <span id="currentDate">—</span> · Нажмите <strong style="color:var(--gold)">Демо</strong> или <strong style="color:var(--gold)">Настройки</strong> для подключения
      </div>
    </div>
    <div class="kpis-row animate" id="kpisRow">
      <div class="kpi-card neu"><div class="kpi-label">Выручка факт</div><div class="kpi-val" id="kpiRevenue">—</div><div class="kpi-sub" id="kpiRevenueSub">Ожидание данных</div></div>
      <div class="kpi-card neu"><div class="kpi-label">Чеков</div><div class="kpi-val" id="kpiChecks">—</div><div class="kpi-sub" id="kpiChecksSub">Ожидание данных</div></div>
      <div class="kpi-card neu"><div class="kpi-label">Средний чек</div><div class="kpi-val" id="kpiAvg">—</div><div class="kpi-sub" id="kpiAvgSub">Ожидание данных</div></div>
      <div class="kpi-card neu"><div class="kpi-label">Сотрудников</div><div class="kpi-val" id="kpiStaff">—</div><div class="kpi-sub" id="kpiStaffSub">Ожидание данных</div></div>
    </div>
  </header>

  <!-- HEATMAP -->
  <section class="section">
    <div class="sec-head"><span class="sec-title">Нагрузка по часам</span><span class="sec-line"></span><span class="sec-badge">IIKO · TSPH</span></div>
    <div class="card">
      <div class="card-title">Количество чеков в час</div>
      <div id="heatmapWrap"><div class="empty"><div class="empty-icon">📊</div><div class="empty-title">Нет данных</div><div class="empty-sub">Подключите IIKO или загрузите демо</div></div></div>
    </div>
  </section>

  <!-- ПЛАН vs ФАКТ + ГРАФИК -->
  <section class="section">
    <div class="sec-head"><span class="sec-title">План vs Факт</span><span class="sec-line"></span><span class="sec-badge">IIKO · Продажи</span></div>
    <div class="g2">
      <div class="card">
        <div class="card-title">Ключевые показатели</div>
        <div id="kpiTableWrap"><div class="empty"><div class="empty-icon">📋</div><div class="empty-title">Нет данных</div></div></div>
      </div>
      <div class="card">
        <div class="card-title">Динамика по часам</div>
        <div style="position:relative;height:230px"><canvas id="hourChart"></canvas></div>
      </div>
    </div>
  </section>

  <!-- VERIFIX -->
  <section class="section">
    <div class="sec-head"><span class="sec-title">Персонал</span><span class="sec-line"></span><span class="sec-badge">Verifix · Расписание</span></div>
    <div class="g2">
      <div class="card">
        <div class="card-title">Сотрудники сегодня</div>
        <div id="vfEmpWrap"><div class="empty"><div class="empty-icon">👥</div><div class="empty-title">Нет данных</div><div class="empty-sub">Verifix: ручной ввод или CSV</div></div></div>
      </div>
      <div class="card">
        <div class="card-title">FOT и ASPMH</div>
        <div id="fotWrap"><div class="empty"><div class="empty-icon">💰</div><div class="empty-title">Нет данных</div></div></div>
      </div>
    </div>
    <!-- Manual Verifix input -->
    <div class="card" style="margin-top:18px">
      <div class="card-title">Ввод данных Verifix (ручной режим)</div>
      <div class="alert alert-warn">⚠ Verifix API недоступен — введите данные вручную или загрузите CSV из Verifix</div>
      <div style="display:flex;gap:12px;flex-wrap:wrap;align-items:flex-end">
        <div class="form-group" style="margin:0;flex:1;min-width:160px">
          <label class="form-label">Имя сотрудника</label>
          <input class="form-input" id="vfName" placeholder="Иван Иванов">
        </div>
        <div class="form-group" style="margin:0;flex:1;min-width:130px">
          <label class="form-label">Должность</label>
          <select class="form-input" id="vfRole">
            <option>Повар</option><option>Кассир</option><option>Официант</option><option>Уборщица</option><option>Менеджер</option>
          </select>
        </div>
        <div class="form-group" style="margin:0;width:100px">
          <label class="form-label">Начало</label>
          <input class="form-input" id="vfStart" type="time" value="09:00">
        </div>
        <div class="form-group" style="margin:0;width:100px">
          <label class="form-label">Конец</label>
          <input class="form-input" id="vfEnd" type="time" value="18:00">
        </div>
        <div class="form-group" style="margin:0;width:110px">
          <label class="form-label">Ставка (сум/ч)</label>
          <input class="form-input" id="vfRate" type="number" placeholder="35000">
        </div>
        <button class="btn btn-gold" onclick="addEmployee()">+ Добавить</button>
      </div>
      <div style="margin-top:16px;display:flex;align-items:center;gap:12px">
        <label class="btn btn-ghost" style="cursor:pointer">
          📁 Загрузить CSV
          <input type="file" accept=".csv" style="display:none" onchange="loadCSV(event)">
        </label>
        <span style="font-size:12px;color:var(--muted)">Колонки: Имя, Должность, Начало, Конец, Ставка</span>
      </div>
    </div>
  </section>

  <!-- SPMH TABLE -->
  <section class="section">
    <div class="sec-head"><span class="sec-title">SPMH по часам</span><span class="sec-line"></span><span class="sec-badge">Эффективность</span></div>
    <div class="card">
      <div class="card-title">Чеков на сотрудника в час</div>
      <div class="tbl-scroll"><div id="spmhTableWrap"><div class="empty"><div class="empty-icon">⚡</div><div class="empty-title">Нет данных</div></div></div></div>
    </div>
  </section>

</div>

<!-- SETTINGS MODAL -->
<div class="overlay" id="overlay" onclick="if(event.target===this)closeSettings()">
<div class="modal">
  <div class="modal-title">⚙ Настройки подключения</div>
  <div class="modal-sub">Введите данные для IIKO и Verifix</div>
  <div class="tabs">
    <button class="tab active" onclick="switchTab('iiko',this)">IIKO</button>
    <button class="tab" onclick="switchTab('verifix',this)">Verifix</button>
    <button class="tab" onclick="switchTab('date',this)">Дата / Период</button>
  </div>

  <!-- IIKO TAB -->
  <div class="tab-panel active" id="tab-iiko">
    <div class="alert alert-info">💡 Введите данные вашего IIKO сервера. Логин и пароль — те же что в RMS.</div>
    <div class="form-group">
      <label class="form-label">Тип подключения</label>
      <select class="form-input" id="iikoType" onchange="toggleIikoType()">
        <option value="cloud">iiko.biz (облако)</option>
        <option value="local">Локальный сервер</option>
      </select>
    </div>
    <div id="iikoCloudFields">
      <div class="form-group">
        <label class="form-label">API Login (iikoCloud)</label>
        <input class="form-input" id="iikoApiLogin" placeholder="ваш_api_login">
        <div class="form-hint">Берётся из личного кабинета iiko.biz → API</div>
      </div>
    </div>
    <div id="iikoLocalFields" style="display:none">
      <div class="form-group">
        <label class="form-label">Адрес сервера</label>
        <input class="form-input" id="iikoHost" placeholder="http://192.168.1.100:8080">
        <div class="form-hint">IP или имя хоста вашего IIKO сервера</div>
      </div>
      <div class="form-row">
        <div class="form-group">
          <label class="form-label">Логин</label>
          <input class="form-input" id="iikoLogin" placeholder="admin">
        </div>
        <div class="form-group">
          <label class="form-label">Пароль</label>
          <input class="form-input" id="iikoPass" type="password" placeholder="••••••">
        </div>
      </div>
    </div>
    <div class="form-group">
      <label class="form-label">Организация / Ресторан (ID или название)</label>
      <input class="form-input" id="iikoOrg" placeholder="оставьте пустым для авто-определения">
    </div>
    <div style="display:flex;gap:10px">
      <button class="btn btn-ghost" onclick="testIiko()" id="testBtn">🔌 Тест подключения</button>
      <span id="testResult" style="font-size:12px;align-self:center;color:var(--text2)"></span>
    </div>
  </div>

  <!-- VERIFIX TAB -->
  <div class="tab-panel" id="tab-verifix">
    <div class="alert alert-warn">⚠ Verifix не предоставляет публичный API — используйте ручной ввод или экспортируйте CSV из Verifix и загрузите его на странице.</div>
    <div class="form-group">
      <label class="form-label">Если у вас есть API ключ Verifix</label>
      <input class="form-input" id="vfApiKey" placeholder="vf_xxxxxxxxxxxxxxxx">
      <div class="form-hint">Обратитесь в поддержку Verifix для получения ключа</div>
    </div>
    <div class="form-group">
      <label class="form-label">URL сервера Verifix</label>
      <input class="form-input" id="vfHost" placeholder="https://api.verifix.uz">
    </div>
    <div class="divider"></div>
    <div style="font-size:13px;color:var(--text2);line-height:1.8">
      <strong style="color:var(--text)">Как экспортировать CSV из Verifix:</strong><br>
      1. Войдите в Verifix → Расписание<br>
      2. Выберите нужную дату<br>
      3. Нажмите Экспорт → CSV<br>
      4. Загрузите файл на странице дашборда
    </div>
  </div>

  <!-- DATE TAB -->
  <div class="tab-panel" id="tab-date">
    <div class="form-row">
      <div class="form-group">
        <label class="form-label">Дата начала</label>
        <input class="form-input" id="dateFrom" type="date">
      </div>
      <div class="form-group">
        <label class="form-label">Дата конца</label>
        <input class="form-input" id="dateTo" type="date">
      </div>
    </div>
    <div class="form-group">
      <label class="form-label">Быстрый выбор</label>
      <div style="display:flex;gap:8px;flex-wrap:wrap">
        <button class="btn btn-ghost btn-sm" onclick="setRange(0)">Сегодня</button>
        <button class="btn btn-ghost btn-sm" onclick="setRange(7)">7 дней</button>
        <button class="btn btn-ghost btn-sm" onclick="setRange(30)">30 дней</button>
        <button class="btn btn-ghost btn-sm" onclick="setRange('month')">Этот месяц</button>
      </div>
    </div>
    <div class="form-group">
      <label class="form-label">Плановое кол-во чеков/день</label>
      <input class="form-input" id="planChecks" type="number" value="200" placeholder="200">
    </div>
    <div class="form-group">
      <label class="form-label">Плановая выручка/день (сум)</label>
      <input class="form-input" id="planRevenue" type="number" value="16564640" placeholder="16564640">
    </div>
  </div>

  <div class="modal-actions">
    <button class="btn btn-ghost" onclick="closeSettings()">Отмена</button>
    <button class="btn btn-gold" onclick="saveAndLoad()">💾 Сохранить и загрузить</button>
  </div>
</div>
</div>

<script>
// ── State ──────────────────────────────────────────
let STATE = {
  iiko: null,
  employees: [],
  hourData: [],
  planChecks: 200,
  planRevenue: 16564640,
  iikoConnected: false,
  vfConnected: false,
};
let hourChart = null;

// ── Init ──────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  const now = new Date();
  document.getElementById('currentDate').textContent = now.toLocaleDateString('ru-RU',{weekday:'long',day:'numeric',month:'long',year:'numeric'});
  const fmt = d => d.toISOString().split('T')[0];
  document.getElementById('dateFrom').value = fmt(now);
  document.getElementById('dateTo').value = fmt(now);
  const saved = localStorage.getItem('spmh_config');
  if (saved) { try { const c = JSON.parse(saved); restoreConfig(c); } catch(e){} }
});

function restoreConfig(c) {
  if(c.iikoType) { document.getElementById('iikoType').value=c.iikoType; toggleIikoType(); }
  if(c.iikoApiLogin) document.getElementById('iikoApiLogin').value=c.iikoApiLogin;
  if(c.iikoHost) document.getElementById('iikoHost').value=c.iikoHost;
  if(c.iikoLogin) document.getElementById('iikoLogin').value=c.iikoLogin;
  if(c.iikoOrg) document.getElementById('iikoOrg').value=c.iikoOrg;
  if(c.planChecks) document.getElementById('planChecks').value=c.planChecks;
  if(c.planRevenue) document.getElementById('planRevenue').value=c.planRevenue;
}

// ── Modal ──────────────────────────────────────────
function openSettings() { document.getElementById('overlay').classList.add('show'); }
function closeSettings() { document.getElementById('overlay').classList.remove('show'); }
function switchTab(name, el) {
  document.querySelectorAll('.tab').forEach(t=>t.classList.remove('active'));
  document.querySelectorAll('.tab-panel').forEach(p=>p.classList.remove('active'));
  el.classList.add('active');
  document.getElementById('tab-'+name).classList.add('active');
}
function toggleIikoType() {
  const t = document.getElementById('iikoType').value;
  document.getElementById('iikoCloudFields').style.display = t==='cloud'?'block':'none';
  document.getElementById('iikoLocalFields').style.display = t==='local'?'block':'none';
}
function setRange(n) {
  const now = new Date();
  const fmt = d => d.toISOString().split('T')[0];
  document.getElementById('dateTo').value = fmt(now);
  if(n === 'month') {
    document.getElementById('dateFrom').value = fmt(new Date(now.getFullYear(),now.getMonth(),1));
  } else {
    const from = new Date(now); from.setDate(from.getDate()-n);
    document.getElementById('dateFrom').value = fmt(from);
  }
}

// ── Proxy base URL ─────────────────────────────────
const PROXY = 'http://localhost:5050';

// ── Check if proxy is running ──────────────────────
async function checkProxy() {
  try {
    const r = await fetch(`${PROXY}/proxy/status`, {signal: AbortSignal.timeout(2000)});
    return r.ok;
  } catch { return false; }
}

// ── IIKO Test ──────────────────────────────────────
async function testIiko() {
  const btn = document.getElementById('testBtn');
  const res = document.getElementById('testResult');
  btn.disabled = true; btn.textContent = '⏳ Проверяем...';
  res.textContent = '';
  try {
    const proxyOk = await checkProxy();
    if(!proxyOk) throw new Error('Прокси-сервер не запущен. Запустите server.py');

    const host  = document.getElementById('iikoHost').value.trim().replace(/\/$/,'');
    const login = document.getElementById('iikoLogin').value.trim();
    const pass  = document.getElementById('iikoPass').value;
    if(!host||!login) throw new Error('Заполните хост и логин');

    const r = await fetch(`${PROXY}/proxy/auth`, {
      method:'POST', headers:{'Content-Type':'application/json'},
      body: JSON.stringify({host, login, password: pass})
    });
    const d = await r.json();
    if(!r.ok) throw new Error(d.error || `HTTP ${r.status}`);
    res.textContent = '✓ Подключено успешно!';
    res.style.color = 'var(--green)';
  } catch(e) {
    res.textContent = '✗ ' + e.message;
    res.style.color = 'var(--red)';
  }
  btn.disabled=false; btn.textContent='🔌 Тест подключения';
}

// ── Save and load ──────────────────────────────────
async function saveAndLoad() {
  const config = {
    iikoType:     document.getElementById('iikoType').value,
    iikoApiLogin: document.getElementById('iikoApiLogin').value,
    iikoHost:     document.getElementById('iikoHost').value.trim().replace(/\/$/,''),
    iikoLogin:    document.getElementById('iikoLogin').value.trim(),
    iikoPass:     document.getElementById('iikoPass').value,
    iikoOrg:      document.getElementById('iikoOrg').value,
    planChecks:   +document.getElementById('planChecks').value,
    planRevenue:  +document.getElementById('planRevenue').value,
  };
  const toSave = {...config}; delete toSave.iikoPass; // не сохраняем пароль
  localStorage.setItem('spmh_config', JSON.stringify(toSave));
  STATE.planChecks  = config.planChecks;
  STATE.planRevenue = config.planRevenue;
  closeSettings();
  const from = document.getElementById('dateFrom').value;
  const to   = document.getElementById('dateTo').value;
  await loadIikoData(config, from, to);
}

// ── IIKO Data Load (через прокси) ──────────────────
async function loadIikoData(config, from, to) {
  setConnecting('iiko');
  try {
    // 1. Проверяем прокси
    const proxyOk = await checkProxy();
    if(!proxyOk) throw new Error('Запустите server.py и обновите страницу');

    // 2. Авторизация
    const authR = await fetch(`${PROXY}/proxy/auth`, {
      method:'POST', headers:{'Content-Type':'application/json'},
      body: JSON.stringify({host: config.iikoHost, login: config.iikoLogin, password: config.iikoPass||''})
    });
    const authD = await authR.json();
    if(!authR.ok) throw new Error(authD.error || 'Ошибка авторизации');

    // 3. Продажи по часам
    const salesR = await fetch(`${PROXY}/proxy/sales`, {
      method:'POST', headers:{'Content-Type':'application/json'},
      body: JSON.stringify({dateFrom: from, dateTo: to})
    });
    const salesD = await salesR.json();
    if(!salesR.ok) throw new Error(salesD.error || 'Ошибка загрузки данных');

    // 4. Обрабатываем
    const hourMap = {};
    (salesD.hourly||[]).forEach(h => { hourMap[h.hour] = h; });
    STATE.iiko = { hourMap, totalRev: salesD.totalRevenue, totalChecks: salesD.totalChecks };
    STATE.hourData = Array.from({length:16},(_,i) => {
      const h = 9+i;
      return { hour: h, checks: (hourMap[h]||{}).checks||0, revenue: (hourMap[h]||{}).revenue||0 };
    });
    setConnected('iiko', 'IIKO ✓');
    document.getElementById('refreshBtn').style.display='flex';
    renderAll();
  } catch(e) {
    setError('iiko', e.message);
    console.error('IIKO error:', e);
    showProxyGuide(e.message);
  }
}

// ── Proxy guide popup ──────────────────────────────
function showProxyGuide(errMsg) {
  const isNotRunning = errMsg.includes('server.py') || errMsg.includes('Прокси');
  const msg = isNotRunning
    ? `⚠ Прокси-сервер не запущен!\n\nЧтобы подключить IIKO:\n1. Скачай файл server.py\n2. Установи Python (python.org)\n3. В терминале: pip install flask flask-cors requests\n4. Запусти: python server.py\n5. Открой: http://localhost:5050`
    : `⚠ Ошибка IIKO: ${errMsg}\n\nПроверь:\n• Адрес сервера\n• Логин и пароль\n• Сервер IIKO работает`;
  alert(msg);
}

function processIikoReport(rep) {
  const data = rep.data || rep.rows || [];
  const hourMap = {};
  let totalRev = 0, totalChecks = 0;
  data.forEach(row => {
    const h = row['OpenDate.Hour'] ?? row[0];
    const cnt = +(row['OrdersCount'] ?? row[1] ?? 0);
    const rev = +(row['Revenue'] ?? row[2] ?? 0);
    if(h !== undefined) hourMap[+h] = { checks: cnt, revenue: rev };
    totalChecks += cnt; totalRev += rev;
  });
  STATE.iiko = { hourMap, totalRev, totalChecks };
  STATE.hourData = Array.from({length:16},(_,i)=>{
    const h = 9+i;
    return { hour: h, checks: (hourMap[h]||{}).checks||0, revenue: (hourMap[h]||{}).revenue||0 };
  });
  renderAll();
}

// ── Demo Data ──────────────────────────────────────
function loadDemo() {
  const tsph = [1.67,5.33,11,23.33,25,18.67,12,10,5.33,8,18.33,17,14,11.67,10.33,8.67];
  STATE.hourData = tsph.map((c,i)=>({hour:9+i, checks:Math.round(c), revenue:Math.round(c*95659)}));
  STATE.iiko = {
    totalRev: 13870580, totalChecks: 145,
    hourMap: Object.fromEntries(tsph.map((c,i)=>[9+i,{checks:Math.round(c),revenue:Math.round(c*95659)}]))
  };
  // Demo employees
  STATE.employees = [
    {name:'Алишер К.', role:'Повар', start:'09:00',end:'18:00',rate:45000},
    {name:'Мадина Р.', role:'Повар', start:'12:00',end:'22:00',rate:45000},
    {name:'Бобур Т.', role:'Кассир',start:'10:00',end:'20:00',rate:35000},
    {name:'Зулфия Н.', role:'Официант',start:'11:00',end:'21:00',rate:30000},
    {name:'Камол А.', role:'Официант',start:'12:00',end:'22:00',rate:30000},
    {name:'Нилуфар С.', role:'Уборщица',start:'08:00',end:'16:00',rate:25000},
  ];
  setConnected('iiko','IIKO (демо)');
  document.getElementById('vfLabel').textContent='Verifix (демо)';
  document.getElementById('vfDot').className='conn-dot ok';
  document.getElementById('refreshBtn').style.display='flex';
  renderAll();
}

// ── Render All ─────────────────────────────────────
function renderAll() {
  if(!STATE.iiko) return;
  renderKPIs();
  renderHeatmap();
  renderKPITable();
  renderHourChart();
  renderSPMHTable();
  renderVfEmployees();
  renderFOT();
}

function fmt(n) { return Math.round(n).toLocaleString('ru-RU'); }

function renderKPIs() {
  const {totalRev, totalChecks} = STATE.iiko;
  const avg = totalChecks ? Math.round(totalRev/totalChecks) : 0;
  const staff = STATE.employees.length;
  const pRev = STATE.planRevenue, pChk = STATE.planChecks;
  const revPct = pRev ? Math.round((totalRev/pRev-1)*100) : 0;
  const chkPct = pChk ? Math.round((totalChecks/pChk-1)*100) : 0;
  const avgPlan = pChk&&pRev ? Math.round(pRev/pChk) : 0;
  const avgPct = avgPlan ? Math.round((avg/avgPlan-1)*100) : 0;

  const revCard = document.querySelector('.kpi-card:nth-child(1)');
  const chkCard = document.querySelector('.kpi-card:nth-child(2)');
  const avgCard = document.querySelector('.kpi-card:nth-child(3)');
  const stCard  = document.querySelector('.kpi-card:nth-child(4)');

  set('#kpiRevenue', fmt(totalRev));
  set('#kpiRevenueSub', `${revPct>=0?'▲ +':'▼ '}${revPct}% от плана`);
  revCard.className='kpi-card '+(revPct>=0?'ok':'bad');

  set('#kpiChecks', totalChecks);
  set('#kpiChecksSub', `${chkPct>=0?'▲ +':'▼ '}${chkPct}% от плана`);
  chkCard.className='kpi-card '+(chkPct>=0?'ok':'bad');

  set('#kpiAvg', fmt(avg));
  set('#kpiAvgSub', `${avgPct>=0?'▲ +':'▼ '}${avgPct}% от плана`);
  avgCard.className='kpi-card '+(avgPct>=0?'ok':'warn');

  set('#kpiStaff', staff||'—');
  set('#kpiStaffSub', staff ? 'Сотрудников сегодня' : 'Добавьте сотрудников');
  stCard.className='kpi-card '+(staff?'ok':'neu');
}

function renderHeatmap() {
  const max = Math.max(...STATE.hourData.map(d=>d.checks),1);
  const HOURS = ['09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','00'];
  let html = '<div class="hm-grid">';
  STATE.hourData.forEach((d,i) => {
    const r = d.checks/max;
    let bg,txt;
    if(r>.75){bg='rgba(153,27,27,0.85)';txt='#fecaca';}
    else if(r>.5){bg='rgba(180,83,9,0.8)';txt='#fed7aa';}
    else if(r>.25){bg='rgba(20,83,45,0.7)';txt='#bbf7d0';}
    else{bg='rgba(26,58,108,0.65)';txt='#bfdbfe';}
    html+=`<div class="hm-cell" style="background:${bg};color:${txt}" title="${HOURS[i]}:00 — ${d.checks} чеков">
      <span class="hm-h">${HOURS[i]}</span><span class="hm-v">${d.checks}</span></div>`;
  });
  html+='</div>';
  html+=`<div style="display:flex;gap:20px;margin-top:16px;flex-wrap:wrap">
    <span style="font-size:11px;color:var(--text2);display:flex;align-items:center;gap:6px"><span style="width:10px;height:10px;border-radius:3px;background:rgba(26,58,108,0.65);display:inline-block"></span>Низкая</span>
    <span style="font-size:11px;color:var(--text2);display:flex;align-items:center;gap:6px"><span style="width:10px;height:10px;border-radius:3px;background:rgba(20,83,45,0.7);display:inline-block"></span>Средняя</span>
    <span style="font-size:11px;color:var(--text2);display:flex;align-items:center;gap:6px"><span style="width:10px;height:10px;border-radius:3px;background:rgba(153,27,27,0.85);display:inline-block"></span>Высокая</span>
  </div>`;
  document.getElementById('heatmapWrap').innerHTML=html;
}

function renderKPITable() {
  const {totalRev,totalChecks}=STATE.iiko;
  const avg=totalChecks?Math.round(totalRev/totalChecks):0;
  const pRev=STATE.planRevenue,pChk=STATE.planChecks;
  const pAvg=pChk?Math.round(pRev/pChk):0;
  const rows=[
    {name:'Товарооборот (сум)',plan:fmt(pRev),fact:fmt(totalRev),ok:totalRev>=pRev},
    {name:'Количество чеков',plan:pChk,fact:totalChecks,ok:totalChecks>=pChk},
    {name:'Средний чек (сум)',plan:fmt(pAvg),fact:fmt(avg),ok:avg>=pAvg},
    {name:'Сотрудников',plan:'—',fact:STATE.employees.length||'—',ok:true},
  ];
  let html='<table class="tbl"><thead><tr><th>Показатель</th><th>План</th><th>Факт</th><th>Статус</th></tr></thead><tbody>';
  rows.forEach(r=>{
    const st=r.ok?`<span class="badge badge-ok">✓ Выполнено</span>`:`<span class="badge badge-bad">✗ Недобор</span>`;
    html+=`<tr><td>${r.name}</td><td style="color:var(--text2)">${r.plan}</td><td style="color:${r.ok?'var(--green)':'var(--red)'};font-weight:500">${r.fact}</td><td>${st}</td></tr>`;
  });
  html+='</tbody></table>';
  document.getElementById('kpiTableWrap').innerHTML=html;
}

function renderHourChart() {
  const HOURS=['09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','00'];
  const vals=STATE.hourData.map(d=>d.checks);
  const staffByHour=Array(16).fill(0);
  STATE.employees.forEach(e=>{
    const s=+e.start.split(':')[0],en=+e.end.split(':')[0];
    for(let h=s;h<en&&h<25;h++){const idx=h-9;if(idx>=0&&idx<16)staffByHour[idx]++;}
  });
  if(hourChart){hourChart.destroy();}
  hourChart=new Chart(document.getElementById('hourChart'),{
    data:{
      labels:HOURS,
      datasets:[
        {type:'bar',label:'Чеков в час',data:vals,
         backgroundColor:'rgba(232,184,75,0.55)',borderColor:'rgba(232,184,75,0.85)',borderWidth:1,borderRadius:4,yAxisID:'y'},
        {type:'line',label:'Сотрудников',data:staffByHour,
         borderColor:'#2dd4bf',backgroundColor:'rgba(45,212,191,0.1)',tension:.4,
         pointRadius:3,pointBackgroundColor:'#2dd4bf',yAxisID:'y2'}
      ]
    },
    options:{responsive:true,maintainAspectRatio:false,
      plugins:{legend:{display:false}},
      scales:{
        x:{ticks:{color:'#64748b',font:{size:10}},grid:{color:'rgba(255,255,255,0.04)'}},
        y:{ticks:{color:'#64748b',font:{size:10}},grid:{color:'rgba(255,255,255,0.04)'},
           title:{display:true,text:'Чеков',color:'#64748b',font:{size:10}}},
        y2:{position:'right',ticks:{color:'#2dd4bf',font:{size:10}},
            grid:{drawOnChartArea:false},
            title:{display:true,text:'Сотрудников',color:'#2dd4bf',font:{size:10}}}
      }
    }
  });
}

function renderSPMHTable() {
  const HOURS=['09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00','00:00'];
  const staffByHour=Array(16).fill(0);
  STATE.employees.forEach(e=>{
    const s=+e.start.split(':')[0],en=+e.end.split(':')[0];
    for(let h=s;h<en;h++){const idx=h-9;if(idx>=0&&idx<16)staffByHour[idx]++;}
  });
  let html='<table class="tbl"><thead><tr><th>Час</th><th>Чеков</th><th>Сотрудников</th><th>SPMH</th><th>Статус</th></tr></thead><tbody>';
  STATE.hourData.forEach((d,i)=>{
    const st=staffByHour[i]||0;
    const spmh=st?+(d.checks/st).toFixed(2):0;
    let cls,lbl;
    if(!st){cls='badge-neu';lbl='Нет данных';}
    else if(spmh>=4){cls='badge-ok';lbl='✓ Оптимально';}
    else if(spmh>=2){cls='badge-warn';lbl='~ Норма';}
    else{cls='badge-bad';lbl='✗ Перебор';}
    html+=`<tr><td class="time">${HOURS[i]}</td><td>${d.checks}</td><td>${st}</td>
      <td style="font-weight:500;color:${spmh>=4?'var(--green)':spmh>=2?'var(--yellow)':'var(--red)'}">${spmh||'—'}</td>
      <td><span class="badge ${cls}">${lbl}</span></td></tr>`;
  });
  html+='</tbody></table>';
  document.getElementById('spmhTableWrap').innerHTML=html;
}

function renderVfEmployees() {
  if(!STATE.employees.length){
    document.getElementById('vfEmpWrap').innerHTML='<div class="empty"><div class="empty-icon">👥</div><div class="empty-title">Добавьте сотрудников</div><div class="empty-sub">Используйте форму ниже</div></div>';
    return;
  }
  let html='<div class="vf-grid">';
  STATE.employees.forEach(e=>{
    const hrs=(+e.end.split(':')[0])-(+e.start.split(':')[0]);
    const earnFmt=fmt((e.rate||0)*hrs);
    html+=`<div class="vf-emp">
      <div class="vf-name">${e.name}</div>
      <div class="vf-role">${e.role}</div>
      <div class="vf-time">⏰ ${e.start} – ${e.end}</div>
      <div class="vf-status" style="color:var(--text2)">${earnFmt} сум</div>
    </div>`;
  });
  html+='</div>';
  document.getElementById('vfEmpWrap').innerHTML=html;
}

function renderFOT() {
  if(!STATE.employees.length){
    document.getElementById('fotWrap').innerHTML='<div class="empty"><div class="empty-icon">💰</div><div class="empty-title">Нет данных</div></div>';
    return;
  }
  const roleMap={};
  let totalFOT=0,totalHrs=0;
  STATE.employees.forEach(e=>{
    const hrs=(+e.end.split(':')[0])-(+e.start.split(':')[0]);
    const fot=(e.rate||0)*hrs;
    if(!roleMap[e.role])roleMap[e.role]={fot:0,hrs:0,count:0};
    roleMap[e.role].fot+=fot;
    roleMap[e.role].hrs+=hrs;
    roleMap[e.role].count++;
    totalFOT+=fot; totalHrs+=hrs;
  });
  const maxFot=Math.max(...Object.values(roleMap).map(r=>r.fot));
  let html='';
  Object.entries(roleMap).forEach(([role,d])=>{
    const pct=Math.round(d.fot/maxFot*100);
    html+=`<div class="prog-row">
      <div class="prog-meta"><span class="prog-name">${role} (${d.count})</span><span class="prog-vals"><strong>${fmt(d.fot)}</strong> сум · ${d.hrs} ч</span></div>
      <div class="prog-track"><div class="prog-bar" style="width:${pct}%;background:var(--gold)"></div></div>
    </div>`;
  });
  const aspmh=totalHrs?Math.round(totalFOT/totalHrs):0;
  html+=`<div style="margin-top:20px;padding-top:16px;border-top:1px solid var(--border)">
    <div style="display:flex;justify-content:space-between;margin-bottom:8px">
      <span style="font-size:12px;color:var(--text2);text-transform:uppercase;letter-spacing:.08em">Итого FOT</span>
      <span style="font-family:'Bebas Neue',sans-serif;font-size:22px;color:var(--gold)">${fmt(totalFOT)} сум</span>
    </div>
    <div style="display:flex;justify-content:space-between">
      <span style="font-size:12px;color:var(--text2);text-transform:uppercase;letter-spacing:.08em">ASPMH</span>
      <span style="font-size:16px;font-weight:600;color:var(--teal)">${fmt(aspmh)} сум/ч</span>
    </div>
  </div>`;
  document.getElementById('fotWrap').innerHTML=html;
}

// ── Employee management ─────────────────────────────
function addEmployee() {
  const name=document.getElementById('vfName').value.trim();
  const role=document.getElementById('vfRole').value;
  const start=document.getElementById('vfStart').value;
  const end=document.getElementById('vfEnd').value;
  const rate=+document.getElementById('vfRate').value||0;
  if(!name){document.getElementById('vfName').focus();return;}
  STATE.employees.push({name,role,start,end,rate});
  document.getElementById('vfName').value='';
  document.getElementById('vfDot').className='conn-dot ok';
  document.getElementById('vfLabel').textContent=`Verifix: ${STATE.employees.length} сотр.`;
  renderVfEmployees(); renderFOT(); renderSPMHTable();
  if(STATE.iiko)renderHourChart();
}

// ── CSV Load ────────────────────────────────────────
function loadCSV(ev) {
  const file=ev.target.files[0]; if(!file)return;
  const reader=new FileReader();
  reader.onload=e=>{
    const lines=e.target.result.split('\n').filter(l=>l.trim());
    const start=lines[0].toLowerCase().includes('имя')?1:0;
    lines.slice(start).forEach(line=>{
      const [name,role,s,en,rate]=(line.includes(';')?line.split(';'):line.split(','));
      if(name&&role&&s&&en) STATE.employees.push({
        name:name.trim(),role:role.trim(),
        start:s.trim(),end:en.trim(),rate:+(rate||'').trim()||0
      });
    });
    document.getElementById('vfDot').className='conn-dot ok';
    document.getElementById('vfLabel').textContent=`Verifix CSV: ${STATE.employees.length} сотр.`;
    renderVfEmployees(); renderFOT(); renderSPMHTable();
    if(STATE.iiko)renderHourChart();
  };
  reader.readAsText(file,'UTF-8');
}

// ── Refresh ─────────────────────────────────────────
async function refreshData() {
  const saved=localStorage.getItem('spmh_config');
  if(!saved){loadDemo();return;}
  const config=JSON.parse(saved);
  const from=document.getElementById('dateFrom').value;
  const to=document.getElementById('dateTo').value;
  await loadIikoData(config,from,to);
}

// ── Status helpers ──────────────────────────────────
function setConnecting(src) {
  const dot=document.getElementById(src+'Dot');
  dot.className='conn-dot connecting';
  document.getElementById(src+'Label').textContent=(src==='iiko'?'IIKO':'Verifix')+': подключение...';
}
function setConnected(src,label) {
  document.getElementById(src+'Dot').className='conn-dot ok';
  document.getElementById(src+'Label').textContent=label+' ✓';
  if(src==='iiko')document.getElementById('refreshBtn').style.display='flex';
}
function setError(src,msg) {
  document.getElementById(src+'Dot').className='conn-dot err';
  document.getElementById(src+'Label').textContent=(src==='iiko'?'IIKO':'Verifix')+': ошибка';
}
function set(sel,val){const el=document.querySelector(sel);if(el)el.textContent=val;}
</script>
</body>
</html>
