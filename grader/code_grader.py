def contains_keyword(text, keywords):
    return any(k.lower() in text.lower() for k in keywords)


def grade(task, action):
    score = 0.0
    expected = task["expected"]

    matched_issues = 0

    # ✅ 1. Issue Detection (multi-issue support)
    for issue in expected["issues"]:
        if any(issue.lower() in a.lower() for a in action.issues):
            matched_issues += 1
            score += 0.2

    # ✅ 2. Severity Check
    severity_map = {
        "low": 1,
        "medium": 2,
        "high": 3
    }

    pred = severity_map.get(action.severity.lower(), 0)
    exp = severity_map.get(expected["severity"], 0)

    # Allow near match
    if abs(pred - exp) <= 1:
        score += 0.2

    # ✅ 3. Suggestion Quality
    if contains_keyword(action.suggestion, expected["fix_keywords"]):
        score += 0.2

    # ✅ 4. Reasoning Quality
    if contains_keyword(action.reasoning, expected["concepts"]):
        score += 0.2

    # ❌ Penalty: no issues detected
    if len(action.issues) > len(expected["issues"]) + 1: 
        score -= 0.1
    
    # ❌ Penalty: hallucinated too many issues
    if len(action.issues) > len(expected["issues"]) + 1:
        score -= 0.1

    # Clamp score between 0 and 1
    score = max(0.0, min(score, 1.0))

    return score