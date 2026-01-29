# 📄 MODEL CARD — AI Safety & Governance Engine (v2)

## 1. Model Summary
The **AI Safety & Governance Engine (v2)** is a modular governance system designed to control and evaluate LLM behavior. It operates through pre-generation safety analysis, uncertainty-aware abstention, and explainable policy enforcement. It is not a single model but a composite system of classifiers and logic engines.

## 2. Intended Use
This system is designed for specific research and experimental contexts:
- ✅ **Research**: Analyzing governance methodology.
- ✅ **AI Safety Experimentation**: Testing adversarial prompts and defense mechanisms.
- ✅ **Governance Evaluation**: Benchmarking policy enforcement consistency.

### Out of Scope Use
- ❌ **Not a Moderation Replacement**: Should not replace human moderation in consumer platforms.
- ❌ **Not Production-Ready**: Intended for prototype and research environments.
- ❌ **Not a Classifier Benchmark**: Optimized for system-level governance, not individual classifier SOTA.

## 3. System Components
The engine is composed of several specialized modules:
1.  **Rule-based Harm Detection**: Keyword and pattern matching for known threats.
2.  **Prompt-Injection Analysis**: Heuristics to detect jailbreak attempts.
3.  **Medical Intent Classifier**: Distinguishes between informational queries and dangerous advice requests.
4.  **Policy Decision Engine**: Logic layer that synthesizes signals into a final decision.
5.  **Uncertainty Estimator**: Calculates confidence to trigger abstention.
6.  **Explainability Generator**: Produces human-readable decision traces.

## 4. Decision Outputs
The system outputs one of three distinct states:
1.  **ALLOW**: The request is deemed safe.
2.  **BLOCK**: The request violates a specific policy.
3.  **ABSTAIN**: The system detects ambiguity or high uncertainty. *note: This is critical for safety-first systems.*

## 5. Evaluation Metrics
We report metrics transparently to encourage honest research:
- **Precision & Recall**
- **False Positive (FP) / False Negative (FN) Rates**
- **Per-prompt Audit Logs**

## 6. Ethical Considerations
- **Conservative Blocking**: The system is tuned to prefer blocking over allowing unsafe content (High Precision).
- **Explicit Abstention**: Ambiguity is handled by refusing to answer rather than guessing.
- **Human Oversight**: Use in high-stakes environments requires human-in-the-loop for FN (False Negative) cases.

## 7. Limitations
- **Keyword-based Detection**: Vulnerable to creative phrasing or obfuscaton.
- **No Semantic Embedding**: Currently lacks deep semantic matching capabilities.
- **Static Policy**: Does not yet support adaptive learning or dynamic policy updates.

## 8. Responsible Use
**WARNING**: This system is designed to *study* governance behavior. It should not be treated as an infallible safety guardrail. Users must maintain their own evaluation and oversight when using this tool.
