import re

def clean_keywords(keywords):
    cleaned = []
    for k in keywords:
        if not isinstance(k, str):
            continue
        s = k.strip().lower()
        s = re.sub(r'\s+', ' ', s)
        if s:
            cleaned.append(s)
    seen = set()
    result = []
    for item in cleaned:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
