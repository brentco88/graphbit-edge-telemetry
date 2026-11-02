import json
import os
import sys
import jsonschema
import antigen_engine

FIXTURES_DIR = "/home/hhais/tests/fixtures/phase6"
SCHEMA_FILE = os.path.join(FIXTURES_DIR, "claim_denial_schema.json")

TEST_FILES = [
    ("vector_a_dialectal.json", "NOMINAL_AUTONOMOUS", 0.0, 0.49),
    ("vector_b_schema_mutation.json", "ELEVATED_HEURISTIC", 0.50, 0.74),
    ("vector_c_sovereign_lock.json", "SOVEREIGN_HUMAN_LOCK", 0.75, 1.0)
]

def load_json(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def run_suite():
    print("============================================================")
    print("PHASE 6: ADVERSARIAL HEALTH LITERACY HARNESS VERIFICATION")
    print("============================================================\n")

    schema = load_json(SCHEMA_FILE)
    w1, w2, w3 = 0.30, 0.60, 0.10

    all_passed = True

    for filename, expected_directive, min_fi, max_fi in TEST_FILES:
        filepath = os.path.join(FIXTURES_DIR, filename)
        payload = load_json(filepath)

        try:
            jsonschema.validate(instance=payload, schema=schema)
            print(f"[SCHEMA PASS] {filename}")
        except jsonschema.exceptions.ValidationError as e:
            print(f"[SCHEMA FAIL] {filename}: {e.message}")
            all_passed = False
            continue

        telemetry_block = {
            "interaction_velocity_delta": payload["telemetry_state"]["interaction_velocity_delta"],
            "system_latency_ms": 120.0,
            "active_antigens": payload["telemetry_state"]["negative_vector_antigens"],
            "sentiment_score": payload["telemetry_state"]["frustration_index"]
        }

        raw_result = antigen_engine.evaluate_telemetry_state(
            json.dumps(telemetry_block), w1, w2, w3
        )
        eval_result = json.loads(raw_result)

        fi = eval_result["frustration_index"]
        directive = eval_result["execution_directive"]

        print(f"  Payload Claim ID    : {payload['claim_id']}")
        print(f"  Calculated FI       : {fi:.4f}")
        print(f"  Directive Output    : {directive}")
        print(f"  Active Antigens     : {eval_result['emitted_antigens']}")

        if directive == expected_directive and min_fi <= fi <= max_fi:
            print(f"  --> VERIFICATION STATUS: [PASS]\n")
        else:
            print(f"  --> VERIFICATION STATUS: [FAIL] Expected {expected_directive} between {min_fi}-{max_fi}\n")
            all_passed = False

    if all_passed:
        print("RESULT: ALL ADVERSARIAL VECTORS CONFORM AND EXECUTE DETERMINISTICALLY.")
        sys.exit(0)
    else:
        print("RESULT: FAILURES DETECTED IN TEST SUITE.")
        sys.exit(1)

if __name__ == "__main__":
    run_suite()
