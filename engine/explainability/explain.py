def explain(cat,action,attacks,phi):
    return {
        "decision_trace":[
            f"Category: {cat}",
            f"Action: {action}",
            f"Triggered: {[k for k,v in attacks.items() if v]}",
            f"PHI: {phi}"
        ]
    }
