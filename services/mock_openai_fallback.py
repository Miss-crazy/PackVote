# mock_openai_fallback.py
def summarize_to_recs(context_line, items, *, force=False):
    print(f"[Mock OpenAI] summarize_to_recs called with context_line='{context_line}' and {len(items)} items")
    return [
        {
            "title": "Mock Trip Recommendation",
            "summary": "A fantastic mock recommendation to try out.",
            "estimated_cost": "$100 - $300",
            "best_time_to_visit": "Spring",
            "ideal_trip_length": "3 days",
            "highlight_bullets": ["Great for groups", "Easy local transport"]
        }
    ]
