from typing import Any, Dict
from PackVote.sql.engine import make_engine
from PackVote.sql.queries import fetch_group_context
from PackVote.sql.repository import persist_recommendations
from PackVote.services.derive_queries import derive_text_queries
from PackVote.services.facts import fetch_external_facts
from PackVote.services.recommend import build_recommendations_from_facts

def run(group_id: int, *, include_amadeus: bool = True) -> Dict[str, Any]:
    engine = make_engine()
    context = fetch_group_context(engine, group_id)
    queries = derive_text_queries(context)
    facts = fetch_external_facts(queries, want_details=True, include_amadeus=include_amadeus)
    recs = build_recommendations_from_facts(facts)
    ids = persist_recommendations(engine, group_id, recs)
    return {
        "context_used": context,
        "queries": queries,
        "facts_summary": {
            "google_count": len(facts.get("google") or []),
            "amadeus_count": len(facts.get("amadeus") or []),
            "first_error": facts.get("first_error"),
        },
        "recommendations_count": len(recs),
        "inserted_ids": ids,
    }