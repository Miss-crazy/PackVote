from typing import Any, Dict, List
from PackVote.services.openai_fallback import summarize_to_recs

def build_recommendations_from_facts(facts: Dict[str, Any]) -> List[Dict[str, Any]]:
    google_all = facts.get("google") or []
    amadeus_all = facts.get("amadeus") or []
    first_error = facts.get("first_error")

    if not google_all and not amadeus_all:
        return summarize_to_recs("APIs returned nothing; craft generic but actionable group ideas.", [], force=True)

    if first_error:
        slim = [{
            "title": p.get("displayName", {}).get("text") or p.get("displayName"),
            "address": p.get("formattedAddress"),
            "types": p.get("types"),
            "rating": p.get("rating"),
            "website": (p.get("_details") or {}).get("websiteUri"),
        } for p in google_all[:6]]
        return summarize_to_recs(f"Partial data available ({first_error}). Build concise suggestions.", slim, force=True)

    slim = [{
        "title": p.get("displayName", {}).get("text") or p.get("displayName"),
        "address": p.get("formattedAddress"),
        "types": p.get("types"),
        "rating": p.get("rating"),
        "website": (p.get("_details") or {}).get("websiteUri"),
    } for p in google_all[:6]]

    recs = summarize_to_recs("Craft group-friendly recommendations from these places.", slim, force=False)
    if recs: return recs

    # naive fallback if OpenAI not available
    out: List[Dict[str, Any]] = []
    for p in google_all[:3]:
        title = p.get("displayName", {}).get("text") or p.get("displayName") or "Trip Idea"
        bullets = []
        if p.get("rating"): bullets.append(f"Google rating: {p['rating']}")
        if p.get("types"): bullets.append(f"Categories: {', '.join(p['types'][:4])}")
        out.append({
            "title": title,
            "summary": f"Experience {title} — discovered via Google Places.",
            "estimated_cost": "Varies by season",
            "best_time_to_visit": "See local seasonality",
            "ideal_trip_length": "Half day to 5 days",
            "highlight_bullets": bullets or ["Good for small groups."],
        })
    return out
