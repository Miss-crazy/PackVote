import json , re
from decimal import Decimal
from datetime import date 
from typing import Any , Dict , List 
from sqlalchemy import text
from sqlalchemy.engine import Engine

def _parse_text_list(s: str|None) -> List[str]:
    if not s: return []
    s=s.strip()
    if(s.startswith("[") and s.endswith("]")) or (s.startswith("{") and s.endswith("}")):
        try:
            val = json.loads(s)
            if isinstance(val , list): return [str(x).strip() for x in val if str(x).strip()]
            if isinstance(val , dict): return [str(v).strip() for v in val.values() if str(v).strip()]
        except Exception:
            pass
    return [p.strip() for p in re.split(r"[,\n;]+",s) if p.strip()]

def fetch_group_context(engine:Engine, group_id:int)->Dict[str,Any]:
    with engine.begin() as conn:
        g = conn.execute(text("SELECT id , name from groups WHERE id=:gid") , {"gid":group_id}).mappings().first()
        if not g:raise ValueError(f"Group {group_id} not found")
        group_name = g["name"]

        members = conn.execute(text("SELECT id , username FROM members WHERE group_id=:gid ORDER BY id"), {"gid":group_id}).mappings().all()

        profiles : List[Dict[str,Any]] = []
        all_pref , all_visited , all_dates , lengths , budgets = [] , [], [], [],[]
        for m in members :
            mid , uname = m['id'] , m['username']
            pref = conn.exeute(text("SELECT trip_length_days , preferred_places ,visited_places , budget FROM preferences WHERE group_id=:gid AND member_id=:mid"),{"gid":group_id,"mid" : mid}).mappings().first()

            avail = conn.execute(text(" SELECT available_date FROM member_availability WHERE member_id=:mid ORDER BY available_date"), {"mid": mid}).mappings().all()
            dates = [r["available_date"]for r in avail]
            all_dates.extend(dates)

            pp = _parse_text_list(pref["preferred_places"]) if pref else []
            vp = _parse_text_list(pref["visited_places"]) if pref else []
            tl = int(pref["trip_length_days"]) if pref and pref["trip_length_days"] is not None else None
            bd = Decimal(pref["budget"]) if pref and pref["budget"] is not None else None

            all_pref.extend(pp); all_visited.extend(vp)
            if tl is not None: lengths.append(tl)
            if bd is not None: budgets.append(bd)

            profiles.append({
                "member_id": mid, "username": uname, "available_dates": dates,
                "trip_length_days": tl, "preferred_places": pp, "visited_places": vp, "budget": bd
            })

        ctx = {
            "group_id": group_id,
            "group_name": group_name,
            "member_profiles": profiles,
            "preferred_keywords": list(dict.fromkeys([p for p in all_pref if p]))[:5],
            "visited_places": list(dict.fromkeys([p for p in all_visited if p])),
            "aggregated_dates": sorted(list(dict.fromkeys(all_dates))),
            "duration_range": (min(lengths) if lengths else None, max(lengths) if lengths else None),
            "budget_range": (min(budgets) if budgets else None, max(budgets) if budgets else None),
        }
        return ctx
    

    