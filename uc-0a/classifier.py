def classify_complaint(row: dict) -> dict:
    text = (row.get("description") or "").lower()

    category = "Other"
    flag = ""

    if "pothole" in text:
        category = "Pothole"
    elif "flood" in text or "water" in text:
        category = "Flooding"
    elif "light" in text or "streetlight" in text:
        category = "Streetlight"
    elif "garbage" in text or "waste" in text:
        category = "Waste"
    elif "noise" in text:
        category = "Noise"
    elif "road" in text or "crack" in text:
        category = "Road Damage"
    elif "heritage" in text or "monument" in text:
        category = "Heritage Damage"
    elif "heat" in text:
        category = "Heat Hazard"
    elif "drain" in text or "sewage" in text:
        category = "Drain Blockage"
    else:
        flag = "NEEDS_REVIEW"

    urgent_keywords = [
        "injury", "child", "school", "hospital",
        "ambulance", "fire", "hazard", "fell", "collapse"
    ]

    priority = "Urgent" if any(k in text for k in urgent_keywords) else "Standard"

    # STRICT reason (must quote evidence)
    reason = f"Contains evidence: '{row.get('description','')}'"

    if category == "Other":
        flag = "NEEDS_REVIEW"

    return {
        "complaint_id": row.get("complaint_id", ""),
        "category": category,
        "priority": priority,
        "reason": reason,
        "flag": flag
    }