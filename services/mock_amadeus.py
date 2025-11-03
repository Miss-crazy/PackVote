# mock_amadeus.py
def pois_by_keyword(keyword: str, *, limit: int = 10, latitude=None, longitude=None):
    print(f"[Mock Amadeus] pois_by_keyword called with keyword='{keyword}', limit={limit}")
    return [
        {
            "id": "mock_amadeus_poi_1",
            "name": "Mock Historic Site",
            "location": {"latitude": 40.7128, "longitude": -74.006},
            "category": "Historic",
        }
    ][:limit]
