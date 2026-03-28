<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>E-commerce Conversion Optimization — A/B Testing Analysis</title>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Syne:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0c0d0f;
    --bg2: #111316;
    --bg3: #161a1f;
    --surface: #1a1f27;
    --border: #232830;
    --border2: #2e3540;
    --amber: #f0a500;
    --amber2: #ffc84a;
    --amber-dim: rgba(240,165,0,0.12);
    --amber-glow: rgba(240,165,0,0.06);
    --teal: #1fcfb0;
    --teal-dim: rgba(31,207,176,0.1);
    --red: #e8534a;
    --text: #e2e4e9;
    --text2: #8a9aad;
    --text3: #556070;
    --mono: 'IBM Plex Mono', monospace;
    --sans: 'Syne', sans-serif;
    --radius: 8px;
  }

  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: var(--sans);
    line-height: 1.7;
    -webkit-font-smoothing: antialiased;
    overflow-x: hidden;
  }

  /* ── GRID NOISE BACKGROUND ── */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
      linear-gradient(rgba(240,165,0,0.015) 1px, transparent 1px),
      linear-gradient(90deg, rgba(240,165,0,0.015) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
    z-index: 0;
  }

  .wrap { max-width: 860px; margin: 0 auto; padding: 0 2rem; position: relative; z-index: 1; }

  /* ── HEADER ── */
  header {
    border-bottom: 1px solid var(--border);
    padding: 3.5rem 0 3rem;
    position: relative;
  }
  header::after {
    content: '';
    position: absolute;
    bottom: -1px;
    left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--amber), transparent);
    opacity: 0.4;
  }

  .badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-family: var(--mono);
    font-size: 11px;
    color: var(--amber);
    background: var(--amber-dim);
    border: 1px solid rgba(240,165,0,0.25);
    border-radius: 20px;
    padding: 4px 12px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 1.5rem;
  }
  .badge::before { content: '●'; font-size: 7px; animation: pulse 2s ease-in-out infinite; }

  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.3} }

  h1 {
    font-size: clamp(2rem, 5vw, 3.2rem);
    font-weight: 800;
    line-height: 1.1;
    letter-spacing: -0.03em;
    color: #fff;
    margin-bottom: 1rem;
  }
  h1 span { color: var(--amber); }

  .subtitle {
    font-family: var(--mono);
    font-size: 13px;
    color: var(--text2);
    letter-spacing: 0.02em;
    max-width: 580px;
  }

  .header-meta {
    display: flex;
    gap: 2rem;
    margin-top: 2rem;
    flex-wrap: wrap;
  }
  .meta-item {
    display: flex;
    align-items: center;
    gap: 8px;
    font-family: var(--mono);
    font-size: 12px;
    color: var(--text3);
  }
  .meta-item strong { color: var(--text2); font-weight: 500; }

  /* ── STATS ROW ── */
  .stats-row {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 1px;
    background: var(--border);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    overflow: hidden;
    margin: 3rem 0;
  }
  .stat {
    background: var(--surface);
    padding: 1.4rem 1.5rem;
    position: relative;
  }
  .stat::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: var(--amber);
    opacity: 0;
    transition: opacity 0.3s;
  }
  .stat:hover::before { opacity: 1; }
  .stat-label {
    font-family: var(--mono);
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: var(--text3);
    margin-bottom: 0.5rem;
  }
  .stat-value {
    font-size: 1.8rem;
    font-weight: 700;
    color: #fff;
    letter-spacing: -0.04em;
    line-height: 1;
  }
  .stat-value span { font-size: 1rem; color: var(--amber); font-weight: 400; }

  /* ── SECTION HEADERS ── */
  section { padding: 3rem 0; border-bottom: 1px solid var(--border); }
  section:last-child { border-bottom: none; }

  h2 {
    font-size: 0.7rem;
    font-family: var(--mono);
    text-transform: uppercase;
    letter-spacing: 0.18em;
    color: var(--amber);
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    gap: 10px;
  }
  h2::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, var(--border2), transparent);
  }

  h3 {
    font-size: 1.15rem;
    font-weight: 700;
    color: #fff;
    margin-bottom: 0.75rem;
    letter-spacing: -0.02em;
  }

  p {
    color: var(--text2);
    font-size: 0.95rem;
    line-height: 1.75;
    font-family: var(--mono);
    max-width: 680px;
  }

  /* ── DATASET TABLE ── */
  .table-wrap {
    overflow-x: auto;
    border-radius: var(--radius);
    border: 1px solid var(--border);
    margin-top: 1.5rem;
  }
  table { width: 100%; border-collapse: collapse; }
  thead { background: var(--bg3); }
  th {
    font-family: var(--mono);
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: var(--text3);
    padding: 10px 16px;
    text-align: left;
    border-bottom: 1px solid var(--border);
  }
  td {
    font-family: var(--mono);
    font-size: 13px;
    color: var(--text2);
    padding: 10px 16px;
    border-bottom: 1px solid var(--border);
    vertical-align: top;
  }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: var(--amber-glow); }
  td:first-child { color: var(--amber2); font-weight: 500; }
  .pill {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 11px;
    background: var(--bg3);
    border: 1px solid var(--border2);
    color: var(--text2);
  }

  /* ── PIPELINE ── */
  .pipeline {
    display: flex;
    align-items: stretch;
    gap: 0;
    margin-top: 1.5rem;
    overflow-x: auto;
    padding-bottom: 4px;
  }
  .pipe-step {
    flex: 1;
    min-width: 130px;
    position: relative;
    padding: 1.2rem 1rem 1rem;
    background: var(--surface);
    border: 1px solid var(--border);
    border-right: none;
    cursor: default;
    transition: background 0.2s;
  }
  .pipe-step:first-child { border-radius: var(--radius) 0 0 var(--radius); }
  .pipe-step:last-child { border-radius: 0 var(--radius) var(--radius) 0; border-right: 1px solid var(--border); }
  .pipe-step:hover { background: var(--bg3); }
  .pipe-step::after {
    content: '›';
    position: absolute;
    right: -10px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--border2);
    font-size: 18px;
    z-index: 2;
    background: var(--bg);
    line-height: 1;
    padding: 0 2px;
  }
  .pipe-step:last-child::after { display: none; }
  .pipe-num {
    font-family: var(--mono);
    font-size: 10px;
    color: var(--amber);
    margin-bottom: 6px;
    letter-spacing: 0.1em;
  }
  .pipe-name {
    font-size: 13px;
    font-weight: 600;
    color: #fff;
    line-height: 1.3;
    margin-bottom: 4px;
  }
  .pipe-desc {
    font-family: var(--mono);
    font-size: 10px;
    color: var(--text3);
    line-height: 1.5;
  }

  /* ── INSTALL BLOCK ── */
  .install-block {
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    margin-top: 1.5rem;
    overflow: hidden;
  }
  .install-bar {
    background: var(--bg3);
    border-bottom: 1px solid var(--border);
    padding: 8px 16px;
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .dot { width: 10px; height: 10px; border-radius: 50%; }
  .dot.r { background: #e8534a; }
  .dot.y { background: #f0a500; }
  .dot.g { background: #1fcfb0; }
  .install-bar span {
    font-family: var(--mono);
    font-size: 11px;
    color: var(--text3);
    margin-left: auto;
  }
  pre {
    padding: 1.2rem 1.4rem;
    overflow-x: auto;
    font-family: var(--mono);
    font-size: 13px;
    color: var(--text2);
    line-height: 1.7;
  }
  .kw { color: var(--amber); }
  .cm { color: var(--text3); }
  .fn { color: var(--teal); }
  .str { color: #a8c7a0; }

  /* ── HYPOTHESIS CARDS ── */
  .hypothesis-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
    margin-top: 1.5rem;
  }
  @media(max-width:520px) { .hypothesis-grid { grid-template-columns: 1fr; } }
  .hyp-card {
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.25rem;
    background: var(--surface);
    position: relative;
    overflow: hidden;
  }
  .hyp-card.null::before { content:''; position:absolute; top:0;left:0;right:0;height:2px; background:var(--text3); }
  .hyp-card.alt::before  { content:''; position:absolute; top:0;left:0;right:0;height:2px; background:var(--amber); }
  .hyp-label {
    font-family: var(--mono);
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: var(--text3);
    margin-bottom: 8px;
  }
  .hyp-card.alt .hyp-label { color: var(--amber); }
  .hyp-text {
    font-size: 0.9rem;
    font-weight: 600;
    color: #fff;
    line-height: 1.4;
  }

  /* ── OUTPUT BLOCK ── */
  .output-block {
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    overflow: hidden;
    margin-top: 1.5rem;
  }
  .output-bar {
    background: var(--bg3);
    border-bottom: 1px solid var(--border);
    padding: 8px 16px;
    font-family: var(--mono);
    font-size: 11px;
    color: var(--text3);
    display: flex;
    justify-content: space-between;
  }
  .output-bar em { color: var(--teal); font-style: normal; }
  .out-line {
    display: flex;
    align-items: baseline;
    gap: 12px;
    padding: 6px 16px;
    border-bottom: 1px solid rgba(35,40,48,0.5);
    font-family: var(--mono);
    font-size: 13px;
    transition: background 0.15s;
  }
  .out-line:hover { background: var(--amber-glow); }
  .out-line:last-child { border-bottom: none; }
  .out-key { color: var(--text3); font-size: 11px; min-width: 240px; }
  .out-val { color: var(--amber2); font-weight: 500; }
  .out-val.ok { color: var(--teal); }

  /* ── NOTES ── */
  .notes-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 1rem;
    margin-top: 1.5rem;
  }
  .note-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.2rem;
  }
  .note-card h4 {
    font-size: 0.85rem;
    font-weight: 600;
    color: #fff;
    margin-bottom: 0.5rem;
  }
  .note-card p {
    font-size: 0.78rem;
    line-height: 1.6;
  }

  /* ── FOOTER ── */
  footer {
    padding: 2.5rem 0;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 1rem;
  }
  footer p { font-size: 12px; color: var(--text3); }
  .author-badge {
    font-family: var(--mono);
    font-size: 11px;
    color: var(--text3);
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 4px 14px;
  }

  /* ── FADE-IN ANIMATION ── */
  @keyframes fadeUp { from { opacity:0; transform:translateY(20px); } to { opacity:1; transform:none; } }
  .fade { opacity: 0; animation: fadeUp 0.6s ease forwards; }
  .fade:nth-child(1){animation-delay:0.0s}
  .fade:nth-child(2){animation-delay:0.1s}
  .fade:nth-child(3){animation-delay:0.2s}
  .fade:nth-child(4){animation-delay:0.3s}
  .fade:nth-child(5){animation-delay:0.4s}

  /* ── COUNTER ── */
  .counting { transition: all 0.05s; }
</style>
</head>
<body>

<div class="wrap">

  <!-- HEADER -->
  <header>
    <div class="badge">Statistical Analysis · A/B Testing</div>
    <h1>E-commerce Conversion<br><span>Optimization</span></h1>
    <p class="subtitle">A statistical A/B testing framework using Frequentist &amp; Bayesian inference to evaluate landing page performance across 288,540 user sessions.</p>
    <div class="header-meta">
      <div class="meta-item"><strong>Language</strong> Python 3</div>
      <div class="meta-item"><strong>Domain</strong> E-commerce / CRO</div>
      <div class="meta-item"><strong>Method</strong> Two-sample Z-test · Beta simulation</div>
      <div class="meta-item"><strong>α</strong> 0.05</div>
    </div>
  </header>

  <!-- STATS -->
  <div class="stats-row">
    <div class="stat fade">
      <div class="stat-label">Total Sessions</div>
      <div class="stat-value counting" data-target="288540" data-suffix="">0</div>
    </div>
    <div class="stat fade">
      <div class="stat-label">Total Conversions</div>
      <div class="stat-value counting" data-target="34483" data-suffix="">0</div>
    </div>
    <div class="stat fade">
      <div class="stat-label">Baseline Conv. Rate</div>
      <div class="stat-value">11.95<span>%</span></div>
    </div>
    <div class="stat fade">
      <div class="stat-label">Significance Level</div>
      <div class="stat-value">0.05<span>α</span></div>
    </div>
    <div class="stat fade">
      <div class="stat-label">Bayesian Samples</div>
      <div class="stat-value">1<span>K</span></div>
    </div>
  </div>

  <!-- OVERVIEW -->
  <section>
    <h2>Overview</h2>
    <h3>What does this project do?</h3>
    <p>This pipeline evaluates whether a redesigned call-to-action button drives a statistically significant lift in conversion rate. It runs the full stack: data cleaning, exploratory analysis, confidence interval estimation, Bayesian simulation, and a one-sided proportions Z-test — producing a clear accept/reject decision on the null hypothesis.</p>
  </section>

  <!-- DATASET -->
  <section>
    <h2>Dataset</h2>
    <h3>Expected schema — <code style="font-family:var(--mono);font-size:0.9rem;color:var(--amber)">ab_data.csv</code></h3>
    <div class="table-wrap">
      <table>
        <thead>
          <tr><th>Column</th><th>Type</th><th>Values</th><th>Description</th></tr>
        </thead>
        <tbody>
          <tr><td>user_id</td><td><span class="pill">int</span></td><td>unique</td><td>Unique identifier per user session</td></tr>
          <tr><td>group</td><td><span class="pill">str</span></td><td>control · treatment</td><td>Experiment arm assignment</td></tr>
          <tr><td>landing_page</td><td><span class="pill">str</span></td><td>old_page · new_page</td><td>Page variant rendered to the user</td></tr>
          <tr><td>converted</td><td><span class="pill">int</span></td><td>0 · 1</td><td>Whether the user completed a purchase</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- REQUIREMENTS -->
  <section>
    <h2>Requirements</h2>
    <h3>Install dependencies</h3>
    <div class="install-block">
      <div class="install-bar">
        <div class="dot r"></div><div class="dot y"></div><div class="dot g"></div>
        <span>terminal</span>
      </div>
      <pre><span class="kw">pip install</span> pandas numpy scipy statsmodels matplotlib seaborn</pre>
    </div>
    <br>
    <div class="install-block">
      <div class="install-bar">
        <div class="dot r"></div><div class="dot y"></div><div class="dot g"></div>
        <span>requirements.txt</span>
      </div>
      <pre><span class="fn">pandas</span>
<span class="fn">numpy</span>
<span class="fn">scipy</span>
<span class="fn">statsmodels</span>
<span class="fn">matplotlib</span>
<span class="fn">seaborn</span></pre>
    </div>
  </section>

  <!-- PIPELINE -->
  <section>
    <h2>Pipeline</h2>
    <h3>Analysis stages</h3>
    <div class="pipeline">
      <div class="pipe-step">
        <div class="pipe-num">01</div>
        <div class="pipe-name">Data Cleaning</div>
        <div class="pipe-desc">Dedup · drop mismatches · null check</div>
      </div>
      <div class="pipe-step">
        <div class="pipe-num">02</div>
        <div class="pipe-name">EDA</div>
        <div class="pipe-desc">Descriptives · conversion distribution</div>
      </div>
      <div class="pipe-step">
        <div class="pipe-num">03</div>
        <div class="pipe-name">Frequentist</div>
        <div class="pipe-desc">Raw conversion rates per group</div>
      </div>
      <div class="pipe-step">
        <div class="pipe-num">04</div>
        <div class="pipe-name">Bayesian</div>
        <div class="pipe-desc">Beta posterior · P(B&nbsp;&gt;&nbsp;A)</div>
      </div>
      <div class="pipe-step">
        <div class="pipe-num">05</div>
        <div class="pipe-name">Confidence Intervals</div>
        <div class="pipe-desc">95% CI per group · margin of error</div>
      </div>
      <div class="pipe-step">
        <div class="pipe-num">06</div>
        <div class="pipe-name">Z-Test</div>
        <div class="pipe-desc">One-sided proportions test · decision</div>
      </div>
    </div>
  </section>

  <!-- HYPOTHESIS -->
  <section>
    <h2>Hypothesis</h2>
    <h3>Test structure</h3>
    <div class="hypothesis-grid">
      <div class="hyp-card null">
        <div class="hyp-label">H₀ — Null Hypothesis</div>
        <div class="hyp-text">There is no significant difference between the old and new button conversion rates.</div>
      </div>
      <div class="hyp-card alt">
        <div class="hyp-label">H₁ — Alternative Hypothesis</div>
        <div class="hyp-text">The new button achieves a significantly higher conversion rate than the original.</div>
      </div>
    </div>
    <br>
    <p>A one-sided Z-test for proportions is applied at significance level α&nbsp;=&nbsp;0.05. If p-value &lt; α, H₀ is rejected and the new button is declared the winner.</p>
  </section>

  <!-- USAGE -->
  <section>
    <h2>Usage</h2>
    <h3>Running the analysis</h3>
    <div class="install-block">
      <div class="install-bar">
        <div class="dot r"></div><div class="dot y"></div><div class="dot g"></div>
        <span>terminal</span>
      </div>
      <pre><span class="cm"># Ensure ab_data.csv is in the working directory</span>
<span class="kw">python</span> <span class="str">"E-commerce_Conversion_Optimization_A_Statistical_AB_Testing_Analysis.py"</span></pre>
    </div>
  </section>

  <!-- OUTPUT -->
  <section>
    <h2>Expected Output</h2>
    <h3>Console results</h3>
    <div class="output-block">
      <div class="output-bar">
        <span>stdout</span>
        <em>live output</em>
      </div>
      <div class="out-line"><span class="out-key">Probability of buying (Group B)</span><span class="out-val">11.95%</span></div>
      <div class="out-line"><span class="out-key">P(B converts better than A) — Bayesian</span><span class="out-val">~0.87</span></div>
      <div class="out-line"><span class="out-key">95% CI — Control (Group A)</span><span class="out-val">[0.1173, 0.1192]</span></div>
      <div class="out-line"><span class="out-key">95% CI — Treatment (Group B)</span><span class="out-val">[0.1170, 0.1189]</span></div>
      <div class="out-line"><span class="out-key">Z-test conclusion</span><span class="out-val ok">Fail to reject H₀ — no significant difference detected</span></div>
    </div>
  </section>

  <!-- NOTES -->
  <section>
    <h2>Notes</h2>
    <h3>Implementation details</h3>
    <div class="notes-grid">
      <div class="note-card">
        <h4>Bayesian Priors</h4>
        <p>The simulation uses α&nbsp;=&nbsp;150, β&nbsp;=&nbsp;180 as Beta distribution priors over 1,000 samples. Adjust these in the script to reflect different prior beliefs about expected conversion rates.</p>
      </div>
      <div class="note-card">
        <h4>One-sided Z-test</h4>
        <p>The proportions Z-test uses <code style="font-family:var(--mono);color:var(--amber);font-size:0.8rem">alternative='larger'</code>, testing specifically whether treatment out-converts control — not just that they differ.</p>
      </div>
      <div class="note-card">
        <h4>Mismatch Removal</h4>
        <p>Rows where group assignment and landing page don't align (e.g., a treatment user seeing the old page) are removed before analysis to preserve experiment integrity.</p>
      </div>
      <div class="note-card">
        <h4>Deduplication</h4>
        <p>Only the first record per <code style="font-family:var(--mono);color:var(--amber);font-size:0.8rem">user_id</code> is retained. This prevents repeat visitors from inflating either group's conversion count.</p>
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer>
    <p>E-commerce Conversion Optimization · Statistical A/B Testing Analysis</p>
    <div class="author-badge">Python · scipy · statsmodels · pandas</div>
  </footer>

</div>

<script>
  // Animated counters
  function animateCount(el) {
    const target = parseInt(el.dataset.target, 10);
    const suffix = el.dataset.suffix || '';
    const duration = 1400;
    const start = performance.now();
    function update(now) {
      const elapsed = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - elapsed, 3);
      const value = Math.round(eased * target);
      el.textContent = value.toLocaleString() + suffix;
      if (elapsed < 1) requestAnimationFrame(update);
    }
    requestAnimationFrame(update);
  }

  const observer = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.querySelectorAll('.counting').forEach(animateCount);
        observer.unobserve(e.target);
      }
    });
  }, { threshold: 0.3 });

  document.querySelectorAll('.stats-row').forEach(el => observer.observe(el));
</script>
</body>
</html>
