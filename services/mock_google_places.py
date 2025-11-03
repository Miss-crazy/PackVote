# mock_google_places.py
def text_search(query: str, *, max_results: int = 8):
    print(f"[Mock Google Places] text_search called with query='{query}', max_results={max_results}")
    return [
        {
            "id": "mock_place_1",
            "displayName": "Mock Museum",
            "formattedAddress": "123 Mock St",
            "types": ["museum", "point_of_interest"],
            "rating": 4.7,
            "userRatingCount": 150,
            "priceLevel": 2,
            "location": {"latitude": 40.7128, "longitude": -74.006},
            "websiteUri": "http://mockmuseum.example.com"
        },
        # add more mock places if needed
    ][:max_results]

def details(place_id: str, *, field_mask=None):
    print(f"[Mock Google Places] details called with place_id='{place_id}'")
    return {
        "id": place_id,
        "displayName": {"text": "Mock Museum"},
        "formattedAddress": "123 Mock St",
        "types": ["museum", "point_of_interest"],
        "rating": 4.7,
        "userRatingCount": 150,
        "priceLevel": 2,
        "location": {"latitude": 40.7128, "longitude": -74.006},
        "websiteUri": "http://mockmuseum.example.com",
        "editorialSummary": "A wonderful place for art lovers.",
    }
