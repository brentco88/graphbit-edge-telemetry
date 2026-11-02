import native_telemetry as telemetry

def test_nominal_distribution():
    probs = [0.95, 0.02, 0.01, 0.01, 0.01]
    hs = telemetry.compute_shannon_entropy(probs)
    passed, mask = telemetry.evaluate_deontic_mask(0)
    fi = telemetry.compute_frustration_index(0.1, 0.0, 0.1, hs)
    print(f"Test 1 Nominal -> Pass: {passed}, Hs: {hs:.3f}, FI: {fi:.3f}")
    assert passed is True
    assert fi < 0.75

def test_deontic_halt():
    payload_flags = 1 << 1
    passed, triggered_bits = telemetry.evaluate_deontic_mask(payload_flags)
    print(f"Test 2 Deontic Halt -> Pass: {passed}, Triggered Bits: {bin(triggered_bits)}")
    assert passed is False
    assert triggered_bits == 2

def test_shannon_frustration_breach():
    probs = [0.25, 0.25, 0.25, 0.25]
    hs = telemetry.compute_shannon_entropy(probs)
    fi = telemetry.compute_frustration_index(0.8, 1.0, 0.8, hs)
    print(f"Test 3 Confusion Spike -> Hs: {hs:.3f}, FI: {fi:.3f}")
    assert fi >= 0.75

if __name__ == "__main__":
    test_nominal_distribution()
    test_deontic_halt()
    test_shannon_frustration_breach()
    print("All three DESP unit tests passed successfully.")
