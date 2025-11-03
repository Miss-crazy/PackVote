<title>PackVote – AI-Powered Group Travel Planner</title>
<style>
  body {
    font-family: "Segoe UI", Arial, sans-serif;
    background-color: #f8f9fa;
    color: #222;
    line-height: 1.7;
    margin: 0;
    padding: 0 10%;
  }
  h1, h2, h3 {
    color: #0078d7;
  }
  h1 {
    border-bottom: 2px solid #0078d7;
    padding-bottom: 0.4em;
  }
  p {
    margin-bottom: 1em;
  }
  code {
    background-color: #eee;
    padding: 2px 5px;
    border-radius: 4px;
    font-size: 90%;
  }
  pre {
    background: #272822;
    color: #f8f8f2;
    padding: 1em;
    border-radius: 6px;
    overflow-x: auto;
  }
  ul {
    list-style-type: square;
    margin-left: 1.5em;
  }
  .section {
    margin-bottom: 2.5em;
  }
  .highlight {
    background-color: #e9f5ff;
    padding: 0.6em 1em;
    border-left: 5px solid #0078d7;
    border-radius: 4px;
  }
</style>
</head>
<body>

<h1>🌍 PackVote – AI-Powered Group Travel Planner</h1>

<p><strong>PackVote</strong> is an AI-powered group travel planning system that generates personalized trip recommendations by aggregating user preferences and integrating data from APIs like <strong>Google Places</strong>, <strong>Amadeus</strong>, and <strong>OpenAI</strong>. It also includes mock APIs for local testing without real API keys.</p>

<div class="section">
  <h2>🚀 Features</h2>
  <ul>
    <li>Modular architecture with clear separation between core service logic, pipelines, and CLI</li>
    <li>Integration with external APIs for rich place data and AI-generated recommendations</li>
    <li>Mock API implementations for offline development and testing without API credentials</li>
    <li>Command-line interface (CLI) for easy recommendation generation</li>
    <li>Uses SQLite for lightweight data persistence</li>
    <li>Environment variable-based configuration for API keys and mock toggling</li>
  </ul>
</div>

<div class="section">
  <h2>📂 Project Structure</h2>
  <div class="highlight">
    <p><code>PackVote/cli/</code> — CLI entrypoints</p>
    <p><code>PackVote/pipelines/</code> — Workflow orchestration</p>
    <p><code>PackVote/services/</code> — API service modules and business logic</p>
    <p><code>PackVote/sql/</code> — Database setup and queries</p>
    <p><code>config.py</code> — Project-specific settings and environment config</p>
    <p><code>requirements.txt</code> — Python package dependencies</p>
  </div>
</div>

<div class="section">
  <h2>💾 Data Storage and Group Planning Model</h2>
  <p><strong>PackVote</strong> uses a lightweight <code>SQLite</code> database (<code>packvote.sqlite</code>) to persistently store data related to groups, members, places, and recommendations. This allows maintaining state across runs and serves as the single source of truth for travel planning.</p>

  <h3>Database Contents</h3>
  <ul>
    <li><strong>Group ID:</strong> Identifier for a user group traveling together. Each group can have multiple members.</li>
    <li><strong>Member ID:</strong> Uniquely identifies each user/member, enabling tracking of individual preferences (availability, preferred places, budget, etc.).</li>
    <li><strong>Places & Recommendations:</strong> Stores suggested places (e.g., museums, cafes) and AI-generated summaries tailored to the group.</li>
    <li><strong>Historical Records:</strong> Maintains past recommendations and user interactions for iterative improvement.</li>
  </ul>
</div>

<div class="section">
  <h2>🧭 Group-Based Recommendations</h2>
  <p>The system aggregates member preferences and constraints to generate <strong>personalized group recommendations</strong>. It produces the <strong>top 5 most relevant destinations</strong> that best match the collective interests, ensuring a consensus-based travel plan.</p>
</div>

<div class="section">
  <h2>🧪 Mock APIs for Cost Efficiency & Testing</h2>
  <p>To minimize cost and simplify development, PackVote uses mock APIs that emulate:</p>
  <ul>
    <li>Google Places API</li>
    <li>Amadeus Travel API</li>
    <li>OpenAI GPT API for summarization</li>
  </ul>
  <p>This design avoids real API keys, prevents overuse of paid resources, and supports reliable local testing.</p>
</div>

<div class="section">
  <h2>🔑 Future Use of Real APIs</h2>
  <p>Switching from mock to live mode is seamless — simply toggle mock usage in environment settings and provide valid credentials.</p>
  <p>Once activated, the system fetches live data and updates the database with real places and AI-driven insights, reflecting changes in persistent storage.</p>

  <div class="highlight">
    <p><strong>✅ Zero Code Rewrite:</strong> Transitioning from mock to production requires no code changes — ensuring flexibility and scalability.</p>
  </div>
</div>

</body>
</html>
