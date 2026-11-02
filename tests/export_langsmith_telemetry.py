import os
import json
import time
import uuid
from dotenv import load_dotenv
from langsmith import Client
import antigen_engine

load_dotenv("/home/hhais/graphbit-edge-core/.env", override=True)

client = Client(api_key=os.getenv("LANGCHAIN_API_KEY"))
project_name = os.getenv("LANGCHAIN_PROJECT", "centaur-governance-telemetry")

FIXTURES_DIR = "/home/hhais/graphbit-edge-core/tests/fixtures/phase6"
TEST_FILES = [
    ("vector_a_dialectal.json", "NOMINAL_AUTONOMOUS"),
    ("vector_b_schema_mutation.json", "ELEVATED_HEURISTIC"),
    ("vector_c_sovereign_lock.json", "SOVEREIGN_HUMAN_LOCK")
]

w1, w2, w3 = 0.30, 0.60, 0.10

def run_and_log():
    print(f"Streaming Phase 6 verified telemetry traces to project: {project_name}\n")
    
    for filename, expected_directive in TEST_FILES:
        filepath = os.path.join(FIXTURES_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            payload = json.load(f)

        telemetry_block = {
            "interaction_velocity_delta": payload["telemetry_state"]["interaction_velocity_delta"],
            "system_latency_ms": 120.0,
            "active_antigens": payload["telemetry_state"]["negative_vector_antigens"],
            "sentiment_score": payload["telemetry_state"]["frustration_index"]
        }

        start_time = time.perf_counter()
        raw_result = antigen_engine.evaluate_telemetry_state(
            json.dumps(telemetry_block), w1, w2, w3
        )
        latency_ms = (time.perf_counter() - start_time) * 1000.0
        eval_result = json.loads(raw_result)

        run_id = uuid.uuid4()
        client.create_run(
            id=run_id,
            name=f"Phase6_Adversarial_{payload['claim_id']}",
            inputs={"payload": payload, "weights": {"w1": w1, "w2": w2, "w3": w3}},
            outputs={
                "calculated_fi": eval_result["frustration_index"],
                "directive": eval_result["execution_directive"],
                "active_antigens": eval_result["emitted_antigens"],
                "sovereign_escalation": eval_result["breach_detected"]
            },
            run_type="chain",
            project_name=project_name,
            extra={
                "metadata": {
                    "hardware": "NVIDIA Jetson Orin Nano 8GB",
                    "runtime": "PyO3 Native Rust Extension",
                    "observed_latency_ms": round(latency_ms, 4),
                    "target_directive": expected_directive
                }
            }
        )
        print(f"Logged {filename} -> Run ID: {run_id} | FI: {eval_result['frustration_index']} | Directive: {eval_result['execution_directive']}")

    print("\nAll telemetry traces streamed successfully.")

if __name__ == "__main__":
    run_and_log()
