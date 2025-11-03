<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PackVote README</title>
<style>
body {
  font-family: Arial, Helvetica, sans-serif;
  background-color: #f8f9fa;
  color: #222;
  line-height: 1.6;
  margin: 40px;
}
h1, h2, h3 {
  color: #003366;
}
h1 {
  border-bottom: 2px solid #003366;
  padding-bottom: 0.3em;
}
p {
  margin-bottom: 1em;
}
ul {
  margin-left: 1.5em;
}
code {
  background-color: #eee;
  padding: 2px 4px;
  border-radius: 4px;
  font-size: 90%;
}
pre {
  background-color: #f4f4f4;
  padding: 10px;
  border-radius: 6px;
}
.section {
  margin-bottom: 2em;
}
</style>
</head>
<body>

<h1>PackVote</h1>

<p>PackVote is an AI-powered group travel planning system that generates personalized trip recommendations by aggregating user preferences and integrating data from APIs like Google Places, Amadeus, and OpenAI. It supports mock APIs for local testing without real API keys.</p>

<h2>Features</h2>
<ul>
<li>Modular architecture with clear separation between core service logic, pipelines, and CLI</li>
<li>Integration with external APIs for rich place data and AI-generated recommendations</li>
<li>Mock API implementations for offline development and testing without API credentials</li>
<li>Command-line interface for easy recommendation generation</li>
<li>Uses SQLite for lightweight data persistence</li>
<li>Environment variable-based configuration for API keys and mock toggling</li>
</ul>

<h2>Project Structure</h2>
<ul>
<li>PackVote/cli/ — CLI entrypoints</li>
<li>PackVote/pipelines/ — Workflow orchestration</li>
<li>PackVote/services/ — API service modules and business logic</li>
<li>PackVote/sql/ — Database setup and queries</li>
<li>config.py — Project-specific settings and environment config</li>
<li>requirements.txt — Python package dependencies</li>
</ul>

<h2>Data Storage and Group Planning Model</h2>
<p>PackVote leverages a lightweight SQLite database (packvote.sqlite) to persistently store data related to groups, members, places, and recommendations. This enables maintaining state across multiple runs and serves as the source of truth for your travel planning.</p>

<h3>Database Contents</h3>
<ul>
<li>Group ID: Identifier for a user group traveling together. Each group can have multiple members.</li>
<li>Member ID: Each user/member within a group is uniquely identified, allowing individual preferences to be tracked separately. Members can specify availability, preferred places, visited places, trip duration, and budget constraints.</li>
<li>Places and Recommendations: Stores details about suggested places (museum, parks, cafes, etc.) and AI-generated recommendation summaries tailored for the group based on aggregated member data.</li>
<li>Historical Records: Keeps track of past recommendations and user interactions for reference and iterative improvement.</li>
</ul>

<h2>Group-Based Recommendations</h2>
<p>The system uses the concept of group travel by aggregating individual member preferences and constraints to compute personalized travel recommendations for the entire group. This offers a consensus plan accommodating various interests and schedules.</p>

<p>The recommendation algorithm produces the top 5 most relevant recommendations for the group, prioritizing places and activities that best match combined preferences and inputs.</p>

<h2>Mock APIs for Cost Efficiency & Testing</h2>
<p>To minimize cost and ease development, the current implementation uses mock APIs which emulate:</p>

<ul>
<li>Google Places API</li>
<li>Amadeus Travel API</li>
<li>OpenAI GPT API for summarization</li>
</ul>

<p>This approach avoids the need for live API keys, prevents overuse of paid resources, and enables reliable local testing.</p>

<h2>Future Use of Real APIs</h2>
<p>Switching to actual APIs is straightforward: toggle mock usage in environment settings and provide valid credentials. The system will then fetch live data, update the database with real places and AI recommendations, reflecting all changes in persistent storage.</p>

<p>This design ensures zero code rewrite when transitioning from mock to production, promoting flexibility and scalability.</p>

</body>
</html>


