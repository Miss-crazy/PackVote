PackVote
PackVote is an AI-powered group travel planning system that generates personalized trip recommendations by aggregating user preferences and integrating data from APIs like Google Places, Amadeus, and OpenAI. It supports mock APIs for local testing without real API keys.

Features
Modular architecture with clear separation between core service logic, pipelines, and CLI

Integration with external APIs for rich place data and AI-generated recommendations

Mock API implementations for offline development and testing without API credentials

Command-line interface for easy recommendation generation

Uses SQLite for lightweight data persistence

Environment variable-based configuration for API keys and mock toggling

Project Structure
PackVote/cli/ — CLI entrypoints

PackVote/pipelines/ — Workflow orchestration

PackVote/services/ — API service modules and business logic

PackVote/sql/ — Database setup and queries

config.py — Project-specific settings and environment config

requirements.txt — Python package dependencies

Data Storage and Group Planning Model
PackVote leverages a lightweight SQLite database (packvote.sqlite) to persistently store data related to groups, members, places, and recommendations. This enables maintaining state across multiple runs and serves as the source of truth for your travel planning.

Database Contents
Group ID: Identifier for a user group traveling together. Each group can have multiple members.

Member ID: Each user/member within a group is uniquely identified, allowing individual preferences to be tracked separately. Members can specify availability, preferred places, visited places, trip duration, and budget constraints.

Places and Recommendations: Stores details about suggested places (museum, parks, cafes, etc.) and AI-generated recommendation summaries tailored for the group based on aggregated member data.

Historical Records: Keeps track of past recommendations and user interactions for reference and iterative improvement.

Group-Based Recommendations
The system uses the concept of group travel by aggregating individual member preferences and constraints to compute personalized travel recommendations for the entire group. This offers a consensus plan accommodating various interests and schedules.

The recommendation algorithm produces the top 5 most relevant recommendations for the group, prioritizing places and activities that best match combined preferences and inputs.

Mock APIs for Cost Efficiency & Testing
To minimize cost and ease development, the current implementation uses mock APIs which emulate:

Google Places API

Amadeus Travel API

OpenAI GPT API for summarization

This approach avoids the need for live API keys, prevents overuse of paid resources, and enables reliable local testing.

Future Use of Real APIs
Switching to actual APIs is straightforward: toggle mock usage in environment settings and provide valid credentials. The system will then fetch live data, update the database with real places and AI recommendations, reflecting all changes in persistent storage.

This design ensures zero code rewrite when transitioning from mock to production, promoting flexibility and scalability.
