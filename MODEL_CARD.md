# 📄 MODEL CARD — AI Global Governance Engine (v2.5)

## 1. System Summary
The **AI Global Governance Engine (v2.5)** is a modular, model-agnostic governance system designed to control and evaluate Large Language Model (LLM) behavior. It operates through pre-generation safety analysis, policy enforcement, post-generation verification, and explainable decision tracing. It functions as an evaluation layer capable of raw vs. governed model comparison across multiple base models (e.g., GPT-2, DistilGPT-2, Phi-2).

## 2. Intended Use
This system is designed for specific research, benchmarking, and experimental contexts:
- ✅ **Research**: Analyzing and measuring governance methodology and harm mitigation.
- ✅ **AI Safety Experimentation**: Testing adversarial prompts, prompt-injection, and defense mechanisms.
- ✅ **Governance Evaluation**: Benchmarking policy enforcement consistency across different LLM architectures.

### Out of Scope Use
- ❌ **Not a Moderation Replacement**: Should not replace human moderation in production consumer platforms without rigorous adaptation.
- ❌ **Not Production-Ready**: Intended primarily for prototype, benchmarking, and research environments.
- ❌ **Not a Classifier Benchmark**: Optimized for system-level governance and harm reduction, not individual classifier SOTA.

## 3. System Components
The engine is composed of several specialized, deterministic and intention-driven modules:
1.  **Rule-based Harm Detection**: Keyword, euphemism expansion, and pattern matching for known threats.
2.  **Prompt-Injection Analysis**: Heuristics to detect jailbreaks and split-prompt attacks.
3.  **Medical Intent Classifier**: Distinguishes between informational queries (INFO) and dangerous advice requests (ADVICE).
4.  **Policy Decision Engine**: Logic layer that synthesizes signals into a final decision (BLOCK / ABSTAIN / ALLOW).
5.  **Uncertainty Estimator**: Calculates confidence to trigger abstention.
6.  **Explainability Generator**: Produces human-readable decision traces.
7.  **Dynamic Model Switcher layer (v2.5)**: Enables direct comparison between raw LLM outputs and governed outputs.

## 4. Decision Outputs
The system outputs one of three explicit states prior to or during generation:
1.  🟢 **ALLOW**: The request is deemed safe and proceeds to the model.
2.  🔴 **BLOCK**: The request violates a specific policy and is withheld.
3.  🟡 **ABSTAIN**: The system detects ambiguity or high uncertainty, withholding the request for review. *(Critical for safety-first systems)*

## 5. Evaluation Metrics & Benchmarking
We report metrics transparently to encourage honest research. Evaluation mode in v2.5 includes Raw vs Governed comparison:
- **Precision & Recall**
- **False Positive Rate (FPR) / False Negative Rate (FNR)**
- **Raw Unsafe Rate vs Governed Block Rate**
- **Harm Reduction Measurement**
- **Per-prompt Audit Logs & Explainability Traces**

## 6. Ethical Considerations
- **Conservative Blocking**: The system is tuned to prefer blocking over allowing unsafe content (aiming for high precision).
- **Explicit Abstention**: Ambiguity is handled by refusing to answer rather than guessing.
- **Model Agnosticism**: Governance is applied uniformly, identifying vulnerabilities across varying base models.
- **Human Oversight**: Use in high-stakes environments requires a human-in-the-loop for FN (False Negative) cases.

## 7. Limitations
- **Rule/Keyword-based Detection Core**: Vulnerable to highly creative paraphrasing or novel obfuscation techniques.
- **English-Focused**: Prompts and evaluations are primarily validated in English.
- **Context Window**: Currently does not support deep cross-turn memory or constitutional reasoning (planned for v3).

## 8. Responsible Use
**WARNING**: This system is designed to *study and benchmark* governance behavior. It should not be treated as an infallible safety guardrail for public-facing deployments. Users must maintain their own evaluation, safety testing, and oversight when using this tool.
