import re

PATTERNS = {
    "EMAIL": r"\b[\w\.-]+@[\w\.-]+\.\w+\b",
    "PHONE": r"\b\d{10}\b",
    "SSN": r"\b\d{3}-\d{2}-\d{4}\b"
}

def redact_phi(text):
    found=[]
    for k,p in PATTERNS.items():
        if re.search(p,text):
            found.append(k)
            text=re.sub(p,f"[REDACTED_{k}]",text)
    return text, found
