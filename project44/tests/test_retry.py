attempt = 0

def test_retry_once():
    # 'global' tells Python: "Use the attempt variable from the outside, don't make a new one inside"
    global attempt
    attempt += 1
    
    print(f"\nAttempt number: {attempt}")
    
    # First time this runs: attempt is 1. 1 >= 2 is False, so it FAILS.
    # Second time this runs: attempt is 2. 2 >= 2 is True, so it PASSES.
    assert attempt >= 2