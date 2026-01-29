# engine/policy/policy.py

def apply_policy(category, attacks, medical_intent, uncertainty=0.0):
    # Prompt injection → always block
    if attacks.get("prompt_injection"):
        return {"action": "BLOCK", "category": "PROMPT_INJECTION"}

    # Self harm
    if category == "SELF_HARM":
        return {"action": "BLOCK", "category": "SELF_HARM"}

    # Sexual / abuse
    if category == "SEXUAL":
        return {"action": "BLOCK", "category": "SEXUAL"}

    # Violence
    if category == "VIOLENCE":
        return {"action": "BLOCK", "category": "VIOLENCE"}

    # Illegal activities
    if category == "ILLEGAL":
        return {"action": "BLOCK", "category": "ILLEGAL"}

    # Medical logic
    if category == "MEDICAL":
        if medical_intent == "ADVICE":
            return {"action": "BLOCK", "category": "MEDICAL_ADVICE"}
        return {"action": "ALLOW", "category": "MEDICAL_INFO"}

    # High uncertainty → abstain
    if uncertainty >= 0.6:
        return {"action": "ABSTAIN", "category": "UNCERTAIN"}

    return {"action": "ALLOW", "category": "SAFE"}
