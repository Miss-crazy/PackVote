from typing import Any , Dict , List , Optional
from PackVote.services.retry import retry_request , HttpFailure
from PackVote.config import GOOGLE_PLACES_API_KEY , GOOGLE_PLACES_ENDPOINT

def text_search(query : str , * , max_results : int =8 , field_mask : Optional[str] = None) -> List[Dict[str , Any]] :
    if not GOOGLE_PLACES_API_KEY  : raise RuntimeError("Missing GOOGLE_PLACES_API_KEY")
    headers ={
        "Content-Type" :"application/json" , 
        "X-Goog-Api-Key" : GOOGLE_PLACES_API_KEY,
        "X-Goog-FieldMask" : field_mask or ",".join([
            "places.id","places.displayName" , "places.formattedAddress","places.types",
            "places.rating" , "places.userRatingCount" , "places.priceLevel","places.location",
            "places.nationalPhoneNumber" , "places.websiteUri" , "places.photos.name",
        ]),
    }
    payload = {"textQuery":query , "maxResultCount" : max_results , "languageCode": "en"}
    resp = retry_request("POST", f"{GOOGLE_PLACES_ENDPOINT}/places:searchText", headers=headers, json=payload)
    try: return resp.json().get("places",[])
    except Exception : raise HttpFailure(f"Google Places JSON parse failed: {resp.text[:500]}")

def details(place_id:str , * , field_mask:Optional[str]=None)->Dict[str,Any]:
    if not GOOGLE_PLACES_API_KEY :raise RuntimeError("Missing GOOGLE_PLACES_API_KEY")
    normalized = place_id if place_id.startswith("place/") else f"places/{place_id}"
    headers ={
        "X-Goog-Api-Key": GOOGLE_PLACES_API_KEY,
        "X-Goog-FieldMask": field_mask or ",".join([
            "id","displayName","formattedAddress","types","rating","userRatingCount","priceLevel",
            "location","nationalPhoneNumber","internationalPhoneNumber","websiteUri",
            "currentOpeningHours.weekdayDescriptions","photos.name","photos.widthPx","photos.heightPx",
            "editorialSummary",
        ]),
    }
    resp = retry_request("GET" , f"{GOOGLE_PLACES_ENDPOINT}/{normalized}", headers=headers)
    try: return resp.json()
    except Exception : raise HttpFailure(f"Google Place Details JSON parse failed: {resp.text[:500]}")
