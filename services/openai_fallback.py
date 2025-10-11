# packvote/services/openai_fallback.py
import json
from typing import Any, Dict, List, Optional
from PackVote.config import OPENAI_API_KEY, OPEN_MODEL

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

def summarize_to_recs(context_line: str, items: List[Dict[str, Any]], *, force: bool = False) -> List[Dict[str, Any]]:
    if not OPENAI_API_KEY or OpenAI is None:
        return [{
            "title": "Fallback Recommendation",
            "summary": "Providers unavailable; best-effort ideas only.",
            "estimated_cost": "Varies",
            "best_time_to_visit": "Varies",
            "ideal_trip_length": "3-5 days",
            "highlight_bullets": ["Try again later for live pricing."],
        }] if force else []

    client = OpenAI(api_key=OPENAI_API_KEY)
    schema = {
        "type": "array",
        "items": {
            "type": "object",
            "required": ["title","summary","estimated_cost","best_time_to_visit","ideal_trip_length","highlight_bullets"],
            "properties": {
                "title":{"type":"string"},"summary":{"type":"string"},"estimated_cost":{"type":"string"},
                "best_time_to_visit":{"type":"string"},"ideal_trip_length":{"type":"string"},
                "highlight_bullets":{"type":"array","items":{"type":"string"}},
            },
        },
    }
    try:
        resp = client.responses.create(
            model=OPEN_MODEL,
            input=[
                {"role":"system","content":"You are a concise, factual group-travel recommendation engine."},
                {"role":"user","content":f"{context_line}\n\nPlaces (JSON):\n{json.dumps(items)}\n\nReturn 2-3 items."},
            ],
            response_format={"type":"json_schema","json_schema":{"name":"recs","schema":schema}},
        )
        return json.loads(resp.output_text)
    except Exception:
        return [{
            "title": "Backup Plan", "summary": "Could not reach OpenAI reliably.",
            "estimated_cost":"N/A","best_time_to_visit":"N/A","ideal_trip_length":"N/A",
            "highlight_bullets":["Please retry soon."],
        }] if force else []
