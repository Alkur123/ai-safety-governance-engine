import re

def detect_harm_category(query: str) -> str:
    q = query.lower()

    SELF_HARM = [
        "suicide","kill myself","end my life","want to die",
        "self harm","hurt myself","cut myself",
        "jump off","overdose","hang myself","unalive myself"
    ]

    SEXUAL = [
        "porn","explicit","nude","naked","rape",
        "child abuse","underage","minor","sexual assault"
    ]

    VIOLENCE = [
        "kill","murder","shoot","stab","attack",
        "bomb","terrorist","weapon","gun"
    ]

    ILLEGAL = [
        "hack","phish","malware","ransomware","ddos",
        "fraud","fake id","credit card fraud",
        "cocaine","heroin","meth","lsd","drugs"
    ]

    MEDICAL = [
        "prescribe","prescription","dosage","dose",
        "medicine","medication","what should i take"
    ]

    for t in SELF_HARM:
        if t in q: return "SELF_HARM"
    for t in SEXUAL:
        if t in q: return "SEXUAL"
    for t in VIOLENCE:
        if t in q: return "VIOLENCE"
    for t in ILLEGAL:
        if t in q: return "ILLEGAL"
    for t in MEDICAL:
        if t in q: return "MEDICAL"

    # regex obfuscation
    if re.search(r"s[\W_]*u[\W_]*i[\W_]*c[\W_]*i[\W_]*d[\W_]*e", q):
        return "SELF_HARM"

    return "SAFE"
