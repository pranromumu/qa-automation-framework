'''
import pytest
from playwright.sync_api import sync_playwright

# ==========================================
# 🎯 CHALLENGES 1 to 4: Pure Python Assertions
# ==========================================

# 🎯 Challenge 1: Equality (== means "Exactly equal to")
def test_equality():
    result = 10
    # "Hey Robin, make sure 'result' is exactly 10!"
    assert result == 10

# 🎯 Challenge 2: Not equal (!= means "Is NOT equal to")
def test_not_equal():
    result = 10
    # "Hey Robin, make sure 'result' is NOT 5!"
    assert result != 5

# 🎯 Challenge 3: Checking text (in means "Is this word hiding inside this text?")
def test_text():
    message = "Login successful"
    assert "Login" in message
    assert "successful" in message

# 🎯 Challenge 4: Boolean (is True / is False)
def test_boolean():
    logged_in = True
    # "Hey Robin, make sure the user IS logged in!"
    assert logged_in is True

def test_not_logged_in():
    logged_in = False
    # "Hey Robin, make sure the user IS NOT logged in!"
    assert logged_in is False


# ==========================================
# 🛠️ THE FIXTURE: Our Personal Assistant
# ==========================================
# We need this Assistant to hand us a fresh browser for the Playwright tests below.
@pytest.fixture
def page():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    yield page
    browser.close()
    playwright.stop()


# ==========================================
# 🎯 CHALLENGES 5 to 7: Playwright Assertions
# ==========================================

# 🎯 Challenge 5: Multiple Validations in one test!
def test_login_page(page):
    page.goto("https://the-internet.herokuapp.com/login")
    
    # 1. Verify the browser tab title
    assert page.title() == "The Internet"
    
    # 2. Verify the big heading on the page
    assert "Login Page" in page.locator("h2").inner_text()
    
    # 3. Verify the boxes and button are visible to the human eye
    assert page.locator("#username").is_visible()
    assert page.locator("#password").is_visible()
    assert page.locator("button.radius").is_visible()

# 🎯 Challenge 6: Positive Scenario (Happy Path)
# Does the website do what it's supposed to do when we do everything right?
def test_successful_login(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button.radius").click()
    
    # Verify the green success banner appears
    message = page.locator("#flash").inner_text()
    assert "You logged into a secure area!" in message
    
    # Verify the URL changed to /secure
    assert "/secure" in page.url

# 🎯 Challenge 7: Negative Scenario (Sad Path)
# Does the website show an error when we type the WRONG password?
def test_failed_login(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("wrongpassword") # Oops! Wrong password!
    page.locator("button.radius").click()
    
    # Verify the red error banner appears
    message = page.locator("#flash").inner_text()
    assert "Your password is invalid!" in message

'''
#============================================================
import pytest
from playwright.sync_api import sync_playwright

def test_ equality():
    result = 10
    assert result == 10
def test_notequal():
    result = 10
    assert result!= 5
def test_text():
    message = "Login Successfull"
    assert "Login" in message
    assert "Successfull" in message
def test_boolean()
    logged_in = True
    assert logged_in is True
def test_not_logged_in();
    logged_in = False
    assert logged_in is False
@pytest.fixture
def page():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    yield page
    browser.close()
    playwright.stop()
def test_login_page(page):
    page.goto("https://the-internet.herokuapp.com/login")
    assert page."title" == "The Internet"
    assert "Login Page" in page.locator("h2").inner_text()
    assert page.locator("usrname").is_visible
    assert page.locator("password").is_visible
    assert page.locator("button.radius").is_visible
def test_successful_login(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button.radius").click()
    message = page.locator("#flash").inner_text()
    assert "You logged into a secure area!" in message
    assert"/ secure" in page.url
def test_unsuccessfull_login(page)
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("wrongname")
    page.locator("#password").fill("wrongpassword")
    page.locator("button.rsdius").click()
    message = page.locator("#flash").inner_text()
    assert " Your username is invalid!" in message
#======================================
#CHALLENGE 8
#++++++++++++++++++++++++++++++++++++++
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
def test_login_page(page):
    page.goto("https://the-internet.herokuapp.com/login")
    assert "Login Page" in page.locator("h2").inner_text()
    assert page.locator("#username").is_visible()
    assert page.locator("#password").is_visible()
    assert page.locator("button.radius").is_visible()
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button.radius").click()
    message = page.locator("#flash").inner_text()
    assert "You logged into a secure area!" in message
    assert "/secure" in page.url

    