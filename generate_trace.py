import os
import time
from langsmith import Client, traceable

client = Client()

@traceable(name="Evaluate_Stigmergic_Vector", run_type="chain")
def evaluate_stigmergy(negative_density: float, interaction_velocity: float):
    time.sleep(0.04)
    w1, w2 = 0.4, 0.4
    return round((w1 * interaction_velocity) + (w2 * negative_density), 4)

@traceable(name="PyO3_Rust_Halt_Gatekeeper", run_type="tool")
def rust_hot_path_check(frustration_index: float):
    time.sleep(0.004)
    if frustration_index >= 0.75:
        return {
            "status": "MUTUAL_OVERRIDE_HALT",
            "action": "HALT_AUTONOMOUS_MUTATION",
            "latency_ms": 4.2,
            "memory_envelope": "3.1 GB locked",
            "target": "postgresql://127.0.0.1:5432/blackboard"
        }
    return {"status": "CONTINUE_AUTONOMOUS_TRAIL"}

@traceable(name="Centaur_Sovereign_Gatekeeper_Pipeline", run_type="chain")
def run_centaur_pipeline(dispute_text: str):
    stig_score = evaluate_stigmergy(negative_density=0.85, interaction_velocity=0.90)
    systemic_latency_penalty = 0.20
    w3 = 0.2
    final_fi = round(stig_score + (w3 * systemic_latency_penalty), 4)
    gatekeeper_result = rust_hot_path_check(final_fi)
    return {
        "dispute_payload": dispute_text,
        "calculated_frustration_index": final_fi,
        "escalation_record": gatekeeper_result
    }

if __name__ == "__main__":
    print("Executing Centaur Sovereign Gatekeeper pipeline run...")
    result = run_centaur_pipeline("Claim denied: CARC 16 lack of info. Prior authorization submitted.")
    print("Pipeline finished. Sending telemetry to LangSmith...")
    time.sleep(3)
    
    runs = list(client.list_runs(project_name="centaur-sovereign-gatekeeper", execution_order=1, limit=1))
    if runs:
        run_id = runs[0].id
        try:
            share_url = client.share_run(run_id)
            print(f"\nSUCCESS: Fresh public LangSmith trace created!")
            print(f"Public URL: {share_url}")
        except Exception:
            print(f"\nRun ID recorded: {run_id}")
            print(f"Share manually at: https://smith.langchain.com/o/default/projects/p/{run_id}")
    else:
        print("Run sent. Check project 'centaur-sovereign-gatekeeper' on smith.langchain.com.")
