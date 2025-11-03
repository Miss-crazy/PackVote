from typing import Any , Dict , List , Optional
from PackVote.config import AMADEUS_API_BASE , AMADEUS_API_KEY,AMADEUS_API_SECRET
from PackVote.services.retry import retry_request , HttpFailure

def _token() ->str:
    if not (AMADEUS_API_KEY and AMADEUS_API_SECRET):
        raise RuntimeError("Missing Amadeus_api_key?Amadeus_api_secret")
    resp = retry_request("POST" ,f"{AMADEUS_API_BASE}/v1/security/oauth2/token",
                         headers={"Content-Type": "application/x-www-form-urlencoded"},
                         data={"grant_type":"client_credentials","client_id":AMADEUS_API_KEY,"client_secret":AMADEUS_API_SECRET})
    try: return resp.json()["access_token"]
    except Exception: raise HttpFailure(f"Amadeus token parse failed :{resp.text[:500]}")

def pois_bykeyword(keyword:str , *, limit:int=10 , latitude:Optional[float]=None , longitude:Optional[float]=None)->List[Dict[str,Any]]:
    tok = _token()
    params: Dict[str, Any] = {"keyword": keyword, "page[limit]": limit, "sort": "RANK"}
    if latitude is not None and longitude is not None:
        params["latitude"] = latitude; params["longitude"] = longitude
    resp = retry_request("GET", f"{AMADEUS_API_BASE}/v1/reference-data/locations/points-of-interest",
                         headers={"Authorization": f"Bearer {tok}"}, params=params)
    try:return resp.json().get("data",[])
    except Exception: raise HttpFailure(f"Amadeus POIs parse failed:{resp.text[:500]}")