from typing import Any, Dict, List

def derive_text_queries(context: Dict[str, Any]) -> List[str]:
    kws = [k for k in (context.get("preferred_keywords") or []) if k][:3]
    q: List[str] = []
    if kws: q.append(" ".join(kws) + " group travel experience")

    min_days, max_days = context.get("duration_range") or (None, None)
    if min_days and max_days: q.append(f"{min_days}-{max_days} day itinerary ideas")

    for prof in (context.get("member_profiles") or []):
        pp = prof.get("preferred_places") or []
        if pp: q.append(f"{pp[0]} activities for friends")

    visited = {v.lower() for v in (context.get("visited_places") or [])}
    out = []
    for s in (q or ["memorable group trip ideas worldwide"]):
        if any(v in s.lower() for v in visited): continue
        if s not in out: out.append(s)
    return out[:6]
