# Centaur Sovereign Gatekeeper: Edge Multi-Agent Telemetry Core

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://graphbit-edge-telemetry-87ewhoqbpfdomnvr5wfch2.streamlit.app/)
[![LangSmith Trace](https://img.shields.io/badge/LangSmith-Public_Trace-orange)](https://smith.langchain.com/public/01a1ad80-22f2-7010-89ab-e397452757ec/r)
[![Hardware](https://img.shields.io/badge/Target-NVIDIA_Jetson_8GB-green)](https://developer.nvidia.com/)

Deterministic human-in-the-loop (HITL) runtime designed for enterprise edge orchestration. Mitigates multi-turn agentic amnesia, halts autonomous tool drift, and defends enterprise Net Retention Revenue (NRR).

---

## 1. Executive Summary

Enterprise support bots prioritize ticket deflection over resolution quality. When an autonomous model fails on complex workflows, it enters repetitive loops, burns token budgets, and drives customer churn.

The Centaur Sovereign Gatekeeper resolves this deterministically:
- Centaur Architecture: 80% autonomous baseline processing paired with 20% high-leverage human strategic oversight.
- Deterministic Escalation: Calculates an interaction Frustration Index in real time. When friction crosses 0.75, autonomous mutation halts in under 200ms, handing verified context to human operators.
- Edge Economics: Deploys local small language models on 8GB edge hardware, eliminating cloud egress costs on baseline queries and locking RAM under 3.1 GB.

---

## 2. Technical Architecture & Live Verification

- Runtime Core: GraphBit DAG executor with native PyO3 Rust hot paths, reducing orchestrator footprint to 0.116 MB.
- State Management: PostgreSQL 14 binary JSONB checkpointer ensuring persistence across multi-turn interactions.
- Negative Stigmergy: Environmental decay vectors block loop hallucinations, cutting token churn factor to 0.31.
- Governance: Conforms to NIST AI 600-1 Action-Consequence standards and OWASP Agentic Top 10 guidelines.

### Live Verification Assets
- Interactive Simulator: [Streamlit Live Sandbox](https://graphbit-edge-telemetry-87ewhoqbpfdomnvr5wfch2.streamlit.app/)
- Telemetry Trace: [Public LangSmith Trace](https://smith.langchain.com/public/01a1ad80-22f2-7010-89ab-e397452757ec/r)

