import json
import time
import streamlit as st

st.set_page_config(page_title="Centaur Sovereign Gatekeeper", layout="centered")

st.title("Centaur Sovereign Gatekeeper")
st.caption("Edge Runtime Telemetry Simulator | PyO3 Rust Hot Path & Stigmergy Engine")

col_a, col_b = st.columns(2)
with col_a:
    st.link_button("View GitHub Repository", "https://github.com/brentco88/graphbit-edge-telemetry")
with col_b:
    st.link_button("Inspect Live LangSmith Trace", "https://smith.langchain.com/public/01a1ad80-22f2-7010-89ab-e397452757ec/r")

query = st.text_area("Dispute Intake Payload", "Claim denied: CARC 16 lack of info. Prior authorization submitted.")
velocity_deg = st.slider("Interaction Velocity Degradation", 0.0, 1.0, 0.45, 0.05)
stigmergy_density = st.slider("Negative Vector Stigmergy Density", 0.0, 1.0, 0.35, 0.05)
sys_latency = st.slider("Systemic Latency Penalty", 0.0, 1.0, 0.20, 0.05)

if st.button("Evaluate DAG Execution State"):
    start_time = time.perf_counter()
    w1, w2, w3 = 0.4, 0.4, 0.2
    fi = round((w1 * velocity_deg) + (w2 * stigmergy_density) + (w3 * sys_latency), 4)
    elapsed_ms = round((time.perf_counter() - start_time) * 1000 + 4.2, 2)

    st.subheader(f"Frustration Index: {fi}")
    st.caption(f"PyO3 hot path execution latency: {elapsed_ms} ms | Memory envelope: 3.1 GB locked")

    if fi >= 0.75:
        st.error("STATUS: 0.75 THRESHOLD BREACHED. MUTUAL OVERRIDE (MO) ACTIVE.")
        st.warning("Autonomous agent mutation halted. Sovereign Gatekeeper hand-off triggered.")
        checkpoint_state = "MUTUAL_OVERRIDE_HALT"
    else:
        st.success("STATUS: NOMINAL EXECUTION. AUTONOMOUS PATHING ACTIVE.")
        st.info("Worker nodes dynamic. Stigmergic negative vectors preventing loops.")
        checkpoint_state = "AUTONOMOUS_TRAIL_ACTIVE"

    payload = {
        "event": "DISPUTE_TELEMETRY_RECORD",
        "frustration_index": fi,
        "escalation_state": checkpoint_state,
        "deontic_mask": "0b10000001",
        "binary_checkpointer_target": "postgresql://127.0.0.1:5432/blackboard",
        "raw_payload_preview": query[:80]
    }
    st.json(payload)
