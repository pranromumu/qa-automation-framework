'''
# 
# ==========================================
# 📄 FILE 1: test_basic.py
# ==========================================

# 🎯 CHALLENGE 1 & 2: Addition Test
# 'def' means we are creating a function (a recipe).
# The name MUST start with 'test_' so Robin (Pytest) knows it's a test to run!
def test_addition():
    # We do the math action
    result = 2 + 3
    
    # The Verification! 
    # We tell Robin: "Check if result is 5."
    # If it is 5, Robin gives a green dot (.) 
    # If it is NOT 5, Robin gives a red F and stops the test.
    assert result == 5  
    # (In Challenge 2, you changed this to 10 to see the red F!)


# 🎯 CHALLENGE 3: Multiple Tests (A Test Suite!)
# We can put as many tests as we want in one file.
# Pytest will find all of them because they start with 'test_'.

def test_subtraction():
    # Here we do the math and the assert all on one line!
    assert 10 - 5 == 5
    
def test_multiplication():
    # Another test for Robin to check.
    assert 4 * 5 == 20

# When you type 'pytest' in the terminal, Robin runs all 3 tests.
# You will see '...' which means 3 tests passed!
'''

def test_addition():
    result = 2+3
    assert result == 5