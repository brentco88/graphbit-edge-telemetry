import os
import json
import time
from datetime import datetime, timezone
import antigen_engine

FIXTURES_DIR = "/home/hhais/graphbit-edge-core/tests/fixtures/phase6"
OUTPUT_FILE = "/home/hhais/graphbit-edge-core/tests/phase6_telemetry_manifest.json"

TEST_FILES = [
    ("vector_a_dialectal.json", "NOMINAL_AUTONOMOUS"),
    ("vector_b_schema_mutation.json", "ELEVATED_HEURISTIC"),
    ("vector_c_sovereign_lock.json", "SOVEREIGN_HUMAN_LOCK")
]

w1, w2, w3 = 0.30, 0.60, 0.10

def freeze_telemetry():
    print("============================================================")
    print("FREEZING PHASE 6 VERIFIED TELEMETRY TO LOCAL AUDIT MANIFEST")
    print("============================================================\n")
    
    manifest = {
        "benchmark_suite": "Phase 6 Adversarial Health Literacy Denial Harness",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "hardware_target": "NVIDIA Jetson Orin Nano Developer Kit (8GB LPDDR5)",
        "governance_engine": "PyO3 Native Rust Extension (antigen_engine v0.1.0)",
        "weights": {"w1_velocity": w1, "w2_antigens": w2, "w3_latency": w3},
        "results": []
    }

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

        trace_entry = {
            "fixture": filename,
            "claim_id": payload["claim_id"],
            "denial_category": payload["denial_metadata"]["denial_reason_category"],
            "calculated_frustration_index": round(eval_result["frustration_index"], 4),
            "expected_directive": expected_directive,
            "emitted_directive": eval_result["execution_directive"],
            "active_antigens": eval_result["emitted_antigens"],
            "breach_detected": eval_result["breach_detected"],
            "evaluation_latency_ms": round(latency_ms, 4),
            "pass": eval_result["execution_directive"] == expected_directive
        }
        
        manifest["results"].append(trace_entry)
        status_label = "[PASS]" if trace_entry["pass"] else "[FAIL]"
        print(f"{status_label} {filename} -> FI: {trace_entry['calculated_frustration_index']} | Directive: {trace_entry['emitted_directive']}")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        json.dump(manifest, out, indent=2)

    print(f"\nManifest successfully written to: {OUTPUT_FILE}")

if __name__ == "__main__":
    freeze_telemetry()
