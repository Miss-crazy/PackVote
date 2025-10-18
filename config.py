import os
from pathlib import Path

_BASE_DIR = Path(__file__).resolve().parent
_DEFAULT_SQLITE_PATH = _BASE_DIR / "sql" / "packvote.sqlite"
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"sqlite:///{_DEFAULT_SQLITE_PATH.as_posix()}",
)

#google
GOOGLE_PLACES_API_KEY = os.getenv("GOOGLE_PLACES_API_KEY")
GOOGLE_PLACES_ENDPOINT = "https://places.googleapis.com/v1"

#AMADEUS
AMADEUS_API_KEY = os.getenv("AMADEUS_API_KEY")
AMADEUS_API_SECRET = os.getenv("AMADEUS_API_SECRET")
AMADEUS_API_BASE = "https://test.api.amadeus.com"

#openAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPEN_MODEL = os.getenv("OPEN_MODEL" , "gpt-4.1-mini")

#app behavior
DEFAULT_MAX_RECS = 5 
RANK_DESCENDING = True 
REQUEST_TIMEOUT_SEC = 15 # Timeout for external API requests
