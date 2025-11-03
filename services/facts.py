from typing import Any, Dict, List, Optional
from PackVote.services import api_switcher

google_places = api_switcher.google_places
amadeus = api_switcher.amadeus
openai_fallback = api_switcher.openai_fallback  # If used elsewhere

def get_display_text(place: dict) -> str:
    d = place.get("displayName", "")
    if isinstance(d, dict):
        return d.get("text", "")
    if isinstance(d, str):
        return d
    return ""

def fetch_external_facts(queries: List[str], *, want_details: bool = True, include_amadeus: bool = True) -> Dict[str, Any]:
    google_all: List[Dict[str, Any]] = []
    first_error: Optional[str] = None

    for q in queries:
        try:
            google_all.extend(google_places.text_search(q, max_results=5))
        except Exception as exc:
            first_error = first_error or f"Google error: {exc}"

    if want_details and google_all:
        enriched = []
        for p in google_all:
            pid = p.get("id") or p.get("name")
            if not pid:
                enriched.append(p)
                continue
            try:
                d = google_places.details(pid)
                merged = dict(p)
                merged["_details"] = d
                enriched.append(merged)
            except Exception:
                enriched.append(p)
        google_all = enriched

    amadeus_all: List[Dict[str, Any]] = []
    if include_amadeus and google_all:
        for p in google_all[:6]:
            name = get_display_text(p)
            keyword = name.split(" ")[0] if name else "travel"
            loc = p.get("location") or p.get("_details", {}).get("location") or {}
            lat, lng = loc.get("latitude"), loc.get("longitude")
            try:
                amadeus_all.extend(amadeus.pois_by_keyword(keyword, limit=6, latitude=lat, longitude=lng))
            except Exception as exc:
                first_error = first_error or f"Amadeus error: {exc}"

    return {"google": google_all, "amadeus": amadeus_all, "first_error": first_error}

