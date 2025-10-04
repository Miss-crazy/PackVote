import json
from typing import Any , Dict , List
from sqlalchemy import text 
from sqlalchemy.engine import Engine 
from PackVote.config import DEFAULT_MAX_RECS , RANK_DESCENDING

def persist_recommendations(engine:Engine , group_id:int , recs:List[Dict[str,Any]])->List[int]:
    recs = (recs or [])[:DEFAULT_MAX_RECS]
    if len(recs)< DEFAULT_MAX_RECS:
        recs = recs + recs[:max(0,DEFAULT_MAX_RECS - len(recs))] 
    
    if RANK_DESCENDING:
        ranks = list(range(DEFAULT_MAX_RECS , 0 , -1))
    else:
        ranks = list(range(1 , DEFAULT_MAX_RECS +1))

    row_ids : List[int] = []
    with engine.begin() as conn:
        conn.execute(text("DELETE FROM recommendations WHERE group_id=:gid") , {"gid":group_id})
        for rank , rec in zip(ranks , recs):
            details = json.dumps({
                "estimated_cost": rec.get("estimated_cost"),
                "best_time_to_visit": rec.get("best_time_to_visit"),
                "ideal_trip_length": rec.get("ideal_trip_length"),
                "highlight_bullets": rec.get("highlight_bullets") or [],
            } , ensure_ascii = False)
            res = conn.execute(text("""
                INSERT INTO recommendations (group_id, rank, title, summary, details, vote_count)
                VALUES (:gid, :rank, :title, :summary, :details, 0)""")
            ,{"gid":group_id , "rank":rank , "title":rec.get("title", "Trip Idea"),
              "summary": rec.get("summary",""), "details": details})
            row_ids.append(res.lastrowid if hasattr(res, "lastrowid") else None)
    return row_ids
