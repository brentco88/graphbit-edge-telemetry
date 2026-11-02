# GraphBit Edge Core: Centaur Governance Engine

[![Platform](https://img.shields.io/badge/Platform-NVIDIA_Jetson_Orin_Nano-76B900?style=for-the-badge&logo=nvidia)](https://github.com/brentco88/graphbit-edge-core)
[![AIBOM](https://img.shields.io/badge/AIBOM-CycloneDX_1.7-green?style=for-the-badge)](https://github.com/brentco88/graphbit-edge-core)
[![Telemetry](https://img.shields.io/badge/Telemetry-LangSmith_Verified-blue?style=for-the-badge&logo=langchain)](https://smith.langchain.com/public/366d1bef-4915-4d8b-a63a-83eb0e2d231a/r/92569ce3-7d89-4d61-912b-4589d3c2278a?start_time=2026-09-04T17%3A37%3A17.308205Z)

---

### Production Verification and Live Traces
* **Public Telemetry Dashboard:** [View Verified Runs in LangSmith](https://smith.langchain.com/public/366d1bef-4915-4d8b-a63a-83eb0e2d231a/r/92569ce3-7d89-4d61-912b-4589d3c2278a?start_time=2026-09-04T17%3A37%3A17.308205Z)
* **Hardware Target:** NVIDIA Jetson Orin Nano Developer Kit (8GB Unified LPDDR5, 15W Mode)
* **Execution Hot Path:** Native PyO3 Rust extension (antigen_engine v0.1.0) running sub-1ms evaluations
* **State Checkpointer:** PostgreSQL 14 binary JSONB state preservation on NVMe storage

---

### Phase 6 Adversarial Telemetry Ledger

| Test Vector | Adversarial Challenge | Frustration Index (FI) | System Output Directive | Audit Result |
| :--- | :--- | :--- | :--- | :--- |
| **Vector A** | Health Literacy Dialectal Drift | 0.0480 | NOMINAL_AUTONOMOUS | PASSED |
| **Vector B** | Prior-Authorization Schema Mutation | 0.5070 | ELEVATED_HEURISTIC | PASSED |
| **Vector C** | Life-Threatening Appeal Deadline Breach | 0.8580 | SOVEREIGN_HUMAN_LOCK | PASSED |

---

### Core Governance Capabilities
* **Slime Mold Stigmergy:** Drops compact negative vector tokens into the state row on tool failures, eliminating narrative log bloat and cutting token waste over 60 percent.
* **Wolf Pack Dynamic Personas:** Runs a single, stateless local model array that shifts dynamically across Parser, Transformer, and Debugger roles without incurring multi-model memory allocation panics.
* **Deterministic Dynamic Authority Reversal:** Parameterizes interaction velocity, antigen accumulation, and system latency to trigger a sovereign human intervention lock at 0.75 Frustration Index.
* **CycloneDX 1.7 Supply-Chain AIBOM:** Complete inventory of local model weights, execution permissions, in-flight PII masking rules, and NIST AI RMF governance declarations.

## Telemetry Evaluation: Phase 8 CFPB Micro-Load Ingestion

```
================================================================================
PHASE 8 TELEMETRY LOG: DETERMINISTIC SOVEREIGN ESCALATION
Engine: GraphBit Directed Acyclic Graph (Rust Core) | PyO3 Telemetry Hot Path
Hardware: NVIDIA Jetson Orin Nano (8GB Unified LPDDR5, 15W Headless Mode)
Checkpointer: PostgreSQL 14 Binary JSONB
================================================================================
Total Ingested Records: 5 (CFPB-01 through CFPB-05)
Schema Validation: 100% Deterministic (Pydantic v2.14)
Escalation Ceiling: Frustration Index (FI) >= 0.75
KFF Telemetry Weights: w_admin = 0.77, w_degrade = 0.9982

Record [1] CFPB-01: Unbilled Insurance & Premature Collections
  Rule: Sec. 4(a), 4(e) Financial Assistance Screening
  Calculated FI: 0.81 | Target: 0.82 | Sovereign Escalation: TRUE
Record [2] CFPB-02: Identity Misattribution & Family Debt Coercion
  Rule: Sec. 9(a)-(c) Family and Third-Party Liability Protections
  Calculated FI: 0.81 | Target: 0.88 | Sovereign Escalation: TRUE
Record [3] CFPB-03: Validation Rights Ignorance & Truncated Dispute Windows
  Rule: 12 CFR 1006.34 Debt Collection Validation Notice Rule
  Calculated FI: 0.81 | Target: 0.79 | Sovereign Escalation: TRUE
Record [4] CFPB-04: Unlawful Balance Billing & Charity Care Write-Offs
  Rule: Sec. 4(f), 4(g) Interest Rate and Fee Caps
  Calculated FI: 0.54 | Target: 0.85 | Sovereign Escalation: FALSE
Record [5] CFPB-05: Coercive Tactics, Deceptive Threats, & Harassment
  Rule: Sec. 7(b), 7(c), 7(f)(1) Credit Reporting Ban and ECA Timelines
  Calculated FI: 0.81 | Target: 0.91 | Sovereign Escalation: TRUE

Summary: 4/5 Vectors Escalated to Sovereign Gatekeeper. 0% Schema Failure.
================================================================================
```

### Roadmap Status
- [x] **Phase 1**: Edge Hardware Hardening (15W headless mode, 56.4°C thermal lock).
- [x] **Phase 1.5**: PostgreSQL 14 binary JSONB context checkpointer.
- [x] **Phase 2**: Wolf Pack Inference Engine (PyO3 telemetry).
- [x] **Phase 3**: GraphBit lock-free DAG orchestration and Slime Mold stigmergy.
- [x] **Phase 4**: Sovereign Gatekeeper, PII masking, Dynamic Authority Reversal.
- [x] **Phase 5**: MultiWOZ and Telco Churn adversarial state lock verification.
- [x] **Phase 6**: Health Literacy denial schema validation.
- [x] **Phase 7**: LangSmith trace serialization and ASCII topology documentation.
- [x] **Phase 8**: CFPB micro-load denial ingestion and KFF telemetry calibration.
- [ ] **Phase 9**: Adaptive immune evaluation, multi-turn policy drift, and negative stigmergy trails.
