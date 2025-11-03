import os

USE_MOCK = os.getenv("USE_MOCK_APIS", "true").lower() == "true"

if USE_MOCK:
    from PackVote.services import mock_google_places as google_places
    from PackVote.services import mock_amadeus as amadeus
    from PackVote.services import mock_openai_fallback as openai_fallback
else:
    from PackVote.services import google_places_real as google_places
    from PackVote.services import amadeus_real as amadeus
    from PackVote.services import openai_fallback_real as openai_fallback
