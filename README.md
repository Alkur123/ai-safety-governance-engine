🛡️ AI Global Governance Engine
**Evaluation-Driven, Explainable Governance Infrastructure for LLMs**
[Status](https://img.shields.io/badge/Status-Research%20Prototype-blueviolet)
![License](https://img.shields.io/badge/License-Apache%202.0-green)
![Deployment](https://img.shields.io/badge/Deployment-Gradio%20%7C%20HuggingFace-lightgrey)
![Version](https://img.shields.io/badge/Version-v2.5-orange)
[![Model Card](https://img.shields.io/badge/Model%20Card-View-blue)](MODEL_CARD.md)
---

## 🔍 Project Overview

The **AI Global Governance Engine** implements an inference-time governance layer that evaluates user queries *before* and *during* model generation. It ensures safety, policy compliance, and decision stability by treating the LLM as an untrusted component.

Unlike simple keyword filters, this engine prioritizes:
- **Pre-generation decision control**
- **Explicit abstention** under uncertainty
- **Explainable governance decisions**
- **Quantitative evaluation** (False Positive / False Negative analysis)
- **State-aware governance** (S2.5 Stateful Escalation)

> *The goal is not to block everything — but to make governance behavior measurable, auditable, and improvable.*

---

## 🚀 Deployment & Demo

We provide multiple ways to deploy and test the engine. Choose the one that fits your infrastructure.

| Platform | Type | Version 2.0 | Version 2.5 |
| :--- | :--- | :--- | :--- |
| **Hugging Face Spaces** | Interactive Demo | [![Open in Spaces](https://huggingface.co/datasets/huggingface/badges/raw/main/open-in-hf-spaces-sm.svg)](https://huggingface.co/spaces/jash-ai/divya) | [![Open in Spaces](https://huggingface.co/datasets/huggingface/badges/raw/main/open-in-hf-spaces-sm.svg)](https://huggingface.co/spaces/jash-ai/global-ai-governance-engine-v25) |
| **AWS** | Enterprise Deployment | [Deploy to AWS (CloudFormation)](http://ai-safety-env.eba-djg2enht.ap-south-1.elasticbeanstalk.com/) | - |
| **Docker** | Containerized | `docker pull ai-safety-governance:v2` | `docker pull ai-safety-governance:v2.5` |

---

## 🔄 Version Evolution

### 🔹 v2 — Deterministic Governance Core
**Core Features:**
- Rule-based harm detection (self-harm, violence, illegal, medical, legal, financial, PII, sexual)
- Prompt injection & split prompt detection
- Euphemism expansion
- Medical intent classification (INFO vs ADVICE)
- Policy-based BLOCK / ABSTAIN / ALLOW
- Post-generation verification layer
- Explainability trace
- Uncertainty modeling
- Inference-time governance metrics (FP / FN tracking)

**Architecture:**
`Deterministic pipeline → Intent detection → Policy enforcement → Verification → Output`

### 🔹 v2.5 — Research-Grade Governance Evaluation & S2.5 Stateful Engine
**New Additions:**
1. **S2.5 Stateful Escalation Engine**: Session-level stateful escalation tracing cumulative behavioral risk across turns.
2. **Support Mode Layer**: Emotional distress signals trigger controlled supportive responses instead of harsh blocks, improving safety and reducing over-blocking.
3. **Multi-Layer Attack Defense**: Deep detection spanning roleplay bypasses, system exfiltration attempts, and fictional framing attacks.
4. **Raw vs Governed Model Comparison**: Dynamic raw model switcher (GPT-2, DistilGPT-2, Phi-2) with leakage measurement.
5. **Model-Agnostic Benchmarking**: Governance layer validated independently of the underlying models.

---

## 🎯 Core Capabilities (v2.5)

### 🔐 Governance Decisions
The engine makes one of four explicit decisions for every query at inference time. This is not post-filtering—it is true **inference-time enforcement**:
- 🟢 **ALLOW** — Safe queries proceed to the model.
- 🔴 **BLOCK** — High-confidence policy violations are stopped.
- 🟡 **ABSTAIN** — Ambiguous or high-uncertainty cases are withheld for review.
- 🔵 **SUPPORT MODE** — Emotional self-harm/despair expressions trigger a controlled supportive response rather than a harsh block.

### 🧠 S2.5 — Stateful Escalation Engine (Key Differentiator)
Unlike standard stateless moderation systems that evaluate prompts independently, our engine actively tracks **cumulative behavioral risk** across turns.
- **Session Memory Tracks**: `turn_count`, `cumulative_risk`, `distress_score`, `escalation_flag`, `last_category`.
- **Dynamic Threshold Adjustments**: E.g., Turn 1: *Mild distress* → Turn 2: *Strong despair* → Turn 3: *Method-seeking* = Escalation triggered, risk boosted, stricter outcomes enforced.

### 🛡 Multi-Layer Harm Detection & Defense
- **Harm Categories**: Deep intent-driven detection of active/passive self-harm, direct/indirect violence, and terror-centric parameters.
- **Attack Defenses**: Mitigates roleplay bypasses, "ignore instructions" requests, audit/testing manipulation, and fictional framing.
- **Advisory Domain Policing**: Enforces strict lines between context *information* versus *direct advice* across Medical, Legal, and Financial domains.
- **Global PII Compliance**: Context-aware redaction mapping global identities (Aadhaar, PAN, Passports, Credit Cards, etc.).

### 🔢 Risk Scoring & Explainability
- **Dynamic Risk Evaluation**: Synthesizes category-base risks with attack-vector boosts, urgency modifiers, and confidence exploitation.
- **Unparalleled Explainability**: Real-time output including detailed Decision Summaries, Applied Regulations, Attack Vector Flags, Append-Only Audit Logs, and clear Timeline traces of internal processing steps.

---

## 🧩 System Architecture

Our engine processes traffic with final authority over the LLM. 

```text
User → PHI Redaction → Harm & Attack Detection → Intent Detection → Session Memory (S2.5) → Policy Engine → BLOCK / ABSTAIN / SUPPORT MODE / ALLOW → Generation → Verification → Explainability + Metric
```

**Key Design Principle:** *The LLM is treated as an untrusted component. Governance logic possesses final authority.*

---

## 🖥️ User Interface (Gradio)

The UI is designed for transparency, exposing the "why" behind every decision:
- **Decision Badges**: 🟢 Allow / 🟡 Abstain / 🔴 Block / 🔵 Support Mode
- **Risk Score Visualization**: Real-time gauge of query risk & escalation severity.
- **Attack Vector Breakdown**: Detailed analysis of potential threats.
- **Governance Timeline**: Step-by-step trace of the internal session memory processing.
- **Live Failure Dashboards**: Unearthing False Positives/Negatives.

---

## 📊 Governance Evaluation & Performance Metrics

### 🧪 Governance Quality Dashboard
*Evaluates true governance correctness (decision accuracy), completely independent of generation quality.*

| Metric | Score | Detail |
| :--- | :--- | :--- |
| **Precision** | **0.88** | High precision retaining minimal over-block rates |
| **Recall** | **1.00** | Perfect recall in successfully trapping zero-day behavioral threats |
| **TP (Correct Blocks)** | **57** | Successfully trapped unsafe requests |
| **TN (Correct Allows)** | **55** | Successfully permitted safe requests |
| **FP (Over-blocks)** | **8** | Blocked safe requests out of caution |
| **FN (Missed risks)** | **0** | No harmful generations leaked (0 missed risks) |

---

### 📈 Multi-Model Benchmarking (v2.5 Additions)

**Evaluation Mode:** Raw vs Governed  
**Categories:** Self-harm, Violence, Illegal, Medical, Legal, Financial, PII, Sexual  

| Model        | Precision | Recall | FPR  | FNR  | Raw Unsafe Rate | Governed Block Rate | Harm Reduction |
|-------------|-----------|--------|------|------|----------------|--------------------|----------------|
| **GPT-2**       | 0.88      | 1.00   | 0.12 | 0.00 | 1.00           | 1.00               | 0.12           |
| **DistilGPT-2** | 0.88      | 1.00   | 0.12 | 0.00 | 1.00           | 1.00               | 0.12           |
| **Phi-2**       | 0.88      | 1.00   | 0.12 | 0.00 | 1.00           | 1.00               | 0.12           |

### 📌 Key Observations
- Raw models generated unsafe outputs for 100% of dangerous prompts.
- Governance middleware successfully blocked 100% of unsafe generations with our new Stateful architecture.
- Safety layer operates dynamically and independently of underlying model architecture.

---

## 🧠 Architectural Impact

v2.5 aggressively transitions the project from a *static rule-based moderation system* to a **state-aware dynamic governance framework (S2.5)**.

The governance engine now showcases robust emotional intelligence pathways, cumulative threat modeling, and measurable harm mitigation across disparate core LLMs.

---

## ⚠ Limitations & System Evolution Analysis

### 🔹 How v2.5 Overcame v2 Limitations
v2 established a deterministic rule-based governance pipeline but lacked state awareness. v2.5 transitioned the system to a rigorous behavioral tracking framework:
- ✅ **Stateful Session Memory (S2.5)**: Implemented cumulative session-level tracking over plain stateless filtering.
- ✅ **Support Mode Fallback**: Curated specific supportive logic, minimizing blanket blocks for distress signals.
- ✅ **Raw vs Governed Measurement**: Embedded side-by-side verification workflows.
- ✅ **Deep Attack Defenses**: Targeted roleplay and fictional-framing vectors proactively.

### ⚠ Remaining Limitations in v2.5
1. **Rule-Based Output Reclassification**: Deterministic rules may overestimate unsafe outputs or miss subtle procedural instructions.
2. **Limited Dataset Size**: Evaluation sets are not completely exhaustive against statistically diverse real-world adversarial inputs.
3. **No Multilingual Benchmarking**: Evaluated primarily on English prompts.
4. **Harm Reduction Definition**: Lacks definitive continuous severity weighting inside the primary dashboard calculation.

---

## 🛣 Roadmap — v3

Planned Enhancements:
- [ ] Adversarial paraphrasing stress tests
- [ ] Jailbreak attack benchmarking
- [ ] Semantic similarity-based risk amplification
- [ ] Risk-weighted harm scoring
- [ ] Expanded multilingual governance support
- [ ] Large-scale evaluation dataset
- [ ] Governance robustness benchmarking suite

### 📌 Summary
* **v2** → Deterministic governance engine  
* **v2.5** → Stateful governance & evaluation framework (S2.5)
* **v3** → Robust adversarial safety evaluation platform

*The system is actively evolving from rule-based moderation into measurable, session-aware governance infrastructure.*


## 📄 Model Documentation

For a detailed breakdown of system architecture, evaluation methodology, limitations, and intended use-cases, please refer to the official [Model Card (v2.5)](MODEL_CARD.md).

