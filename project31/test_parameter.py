

import pytest
from playwright.sync_api import sync_playwright

# ==========================================
# 🎯 CHALLENGES 1 & 2: Pure Python Parameterization
# ==========================================

# The magic spell is @pytest.mark.parametrize
# The first part is a string with the names of our ingredients: "number"
# The second part is a list of the actual ingredients: [1, 2, 3, 4]
@pytest.mark.parametrize("number", [1, 2, 3, 4])
def test_number(number):
    # Pytest will run this test 4 times! Once for each number.
    assert number > 0

# We can pass multiple ingredients too!
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (10, 5, 15),
        (4, 6, 10)
    ]
)
def test_addition(a, b, expected):
    # Pytest runs this 3 times with different math equations.
    assert a + b == expected


# ==========================================
# 🛠️ THE FIXTURE: Our Personal Assistant
# ==========================================
@pytest.fixture
def page():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    yield page
    browser.close()
    playwright.stop()


# ==========================================
# 🏆 CHALLENGES 5 & 6: Playwright + Parameterization (Master Level)
# ==========================================
# We are testing 3 different login scenarios at the same time!
@pytest.mark.parametrize(
    "username, password, should_succeed",
    [
        # Scenario 1: Correct login (Should succeed = True)
        ("tomsmith", "SuperSecretPassword!", True),
        
        # Scenario 2: Wrong username (Should succeed = False)
        ("wronguser", "wrongpassword", False),
        
        # Scenario 3: Correct username, wrong password (Should succeed = False)
        ("tomsmith", "wrongpassword", False)
    ]
)
# IMPORTANT: The parameters in the spell MUST match the arguments in the function below!
def test_login_scenarios(page, username, password, should_succeed):
    # 1. Go to the login page
    page.goto("https://the-internet.herokuapp.com/login")
    
    # 2. Fill the boxes using the ingredients from our conveyor belt!
    page.locator("#username").fill(username)
    page.locator("#password").fill(password)
    
    # 3. Click login
    page.locator("button.radius").click()
    
    # 4. The If/Else Verification!
    # If should_succeed is True, we check for the green success message.
    if should_succeed:
        message = page.locator("#flash").inner_text()
        assert "You logged into a secure area!" in message
        print(f"\n✅ Success Test Passed for user: {username}")
        
    # If should_succeed is False, we check for the red error message.
    else:
        message = page.locator("#flash").inner_text()
        # .lower() makes the text lowercase so it's easier to check
        assert "invalid" in message.lower()
        print(f"\n✅ Failure Test Passed for user: {username}")

#==================================================================
#==================================================================
import pytest
from playwright.sync_api import sync_playwright
@pytest.fixture
def page():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page= browser.new_page()
    yield page
    browser.close
    playwright.stop()
@pytest.mark.parametrize("number"[1,2,3,4])
def test_number(number):
    assert number > 0

@pytest.mark.parametrize("a,b,expected",[
    (3,2,5),
    (10,5,15),
    (4,6,10)
    (20,10,30)
])
def test_addition(a,b,expected):
    assert a = b == expected

@pytest.mark.parametrize(
    "usernane ,password",[
        ("tomsmith","SuperSecretPassword!"),
        ("wronguse","wrongpassword"),
        ("tomsmith","wrongpassword!")
    ]
)
def test_login_data(username,password):
    assert ("testing", username,password)

@pytest.mark.parametrize(
    "username,password,expected",[
        ("tomsmith","SuperSecretPassword!",True),
        ("wronguser","wrongpassword",False),
        ("tomsmith","wrongpasswor!",False)
    ]
)
def test_login(username,password,expected):
    print(username,password,expected)


#===========================================
#CHALLENGE 6
#===========================================
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    yield page
    browser.close()
    playwright.stop()
@pytest.mark.parametrize(
    "username,password,should_success",
    [
        ("tomsmith", "SuperSecretPassword!", True),
        ("wronguser", "wrongpassword", False),
        ("tomsmith", "wrongpassword", False)
    ]
)
def test_login(page, username, password, should_success):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill(username)
    page.locator("#password").fill(password)
    page.locator("button.radius").click()
    if should_success:
        message = page.locator("#flash").inner_text()
        assert "You logged into a secure area!" in message
    else:
        message = page.locator("#flash").inner_text()
        assert "invalid" in message.lower()