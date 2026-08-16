# ==========================================
# 🎯 CHALLENGES 1 & 6: Function Discovery
# ==========================================

# ✅ BEEP! Robin finds this because it starts with 'test_'
def test_login():
    assert True

# ✅ BEEP! Robin finds this too.
def test_logout():
    assert True

# ❌ NO BEEP. Robin ignores this because it says 'check_' instead of 'test_'
def check_profile():
    assert True

# ❌ NO BEEP. Even though it has the word 'test' in it, it doesn't START with 'test_'
def login_test():
    assert True

# ❌ NO BEEP. Same reason.
def my_test():
    assert True

# When you run 'pytest -v', Robin will only run test_login and test_logout!