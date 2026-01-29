import gradio as gr
import time

from engine.pipeline import run_system
from engine.metrics.metrics import get_metrics
from evaluation.eval_suite import run_evaluation


# ================================
# UI HELPERS
# ================================

def status_badge(status):
    return {
        "ALLOWED": "🟢 **ALLOWED**",
        "ABSTAINED": "🟡 **ABSTAINED**",
        "BLOCKED": "🔴 **BLOCKED**"
    }.get(status, status)


def compute_risk(status):
    if status == "BLOCKED":
        return 0.85, "HIGH"
    if status == "ABSTAINED":
        return 0.60, "MEDIUM"
    return 0.20, "LOW"


def risk_bar(score):
    filled = int(score * 10)
    bar = "█" * filled + "░" * (10 - filled)

    if score < 0.3:
        return f"🟢 {bar}  {score:.2f} (LOW)"
    elif score < 0.7:
        return f"🟡 {bar}  {score:.2f} (MEDIUM)"
    else:
        return f"🔴 {bar}  {score:.2f} (HIGH)"


def format_attack_vectors(attacks):
    lines = []
    for k, v in attacks.items():
        if v:
            lines.append(f"❌ {k}: DETECTED")
        else:
            lines.append(f"✅ {k}: Clear")
    return "\n".join(lines)


def format_timeline(timeline):
    if not timeline:
        return "No timeline available"
    return "\n".join(
        f"{i*5:02d}ms : {step}"
        for i, step in enumerate(timeline)
    )


# ================================
# MAIN UI FUNCTION (DEFENSIVE)
# ================================

def ui(query):
    r = run_system(query)

    status = r.get("status", "UNKNOWN")
    score, level = compute_risk(status)

    return (
        status_badge(status),
        r.get("answer", ""),
        r.get("category", ""),
        risk_bar(score),
        format_attack_vectors(r.get("attacks", {})),
        (
            f"Final Decision: {status}\n"
            f"PHI Detected: {r.get('phi') or 'None'}\n\n"
            f"ℹ️ Uncertainty is 0.00 for rule-based "
            f"pre-generation policy enforcement"
        ),
        f"{r.get('uncertainty', 0.0):.2f}",
        format_timeline(r.get("timeline", [])),
        r.get("explain", {})
    )


def metrics_panel():
    return {
        "metrics": get_metrics(),
        "last_updated": time.strftime("%H:%M:%S")
    }


def eval_panel():
    result = run_evaluation()
    s = result["summary"]

    summary_text = (
        f"Precision: {s['precision']:.2f}\n"
        f"Recall: {s['recall']:.2f}\n\n"
        f"TP: {s['TP']}   (Correct blocks)\n"
        f"TN: {s['TN']}   (Correct allows)\n"
        f"FP: {s['FP']}   (Over-blocks)\n"
        f"FN: {s['FN']}   (Missed risks)"
    )

    return summary_text, result["details"]


# ================================
# GRADIO APP
# ================================

with gr.Blocks(title="AI Safety & Governance Engine ") as demo:

    gr.Markdown("## 🛡️ AI Safety & Governance Engine ")

    gr.Markdown(
        """
**Inference-time governance layer for LLM safety**

• Prompt injection & jailbreak detection  
• Medical advice enforcement  
• PHI redaction  
• Policy-based **BLOCK / ABSTAIN / ALLOW**  
• Explainability + uncertainty modeling  
• Governance evaluation (FP / FN analysis)
"""
    )

    inp = gr.Textbox(
        label="User Query",
        placeholder="Enter a query to evaluate",
        lines=2
    )

    outs = [
        gr.Markdown(label="Status"),
        gr.Textbox(label="Answer", lines=4),
        gr.Textbox(label="Decision Category"),
        gr.Textbox(label="Risk Assessment"),
        gr.Textbox(label="Attack Vector Analysis", lines=5),
        gr.Textbox(label="Decision Summary", lines=4),
        gr.Textbox(label="Uncertainty Score"),
        gr.Textbox(label="Governance Timeline", lines=6),
        gr.JSON(label="Explainability Trace"),
    ]

    gr.Button("Run Safety Engine").click(ui, inp, outs)

    with gr.Accordion("🧩 System Architecture", open=False):
        gr.Markdown(
            """
User  
→ PHI Redaction  
→ Harm & Attack Detection  
→ Medical Intent  
→ Policy Engine  
→ **BLOCK / ABSTAIN / ALLOW**  
→ Generation  
→ Verification  
→ Explainability + Metrics
"""
        )

    gr.Markdown("### 📊 Inference-Time Metrics")
    gr.Button("Refresh Metrics").click(
        metrics_panel,
        outputs=gr.JSON()
    )

    with gr.Accordion("🧪 Governance Quality Dashboard", open=False):
        gr.Markdown(
            """
Evaluates **governance correctness**, not generation quality.

• TP – Correctly blocked  
• FP – Over-blocked  
• FN – Missed risks  
• TN – Correctly allowed
"""
        )

        eval_summary = gr.Textbox(label="Evaluation Summary", lines=8)
        eval_details = gr.JSON(label="Per-Prompt Results")

        gr.Button("Run Evaluation Suite").click(
            eval_panel,
            outputs=[eval_summary, eval_details]
        )

demo.launch(share=True)
