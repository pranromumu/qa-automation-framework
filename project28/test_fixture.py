

'''
import pytest

@pytest.fixture
def number():
    return 10
def test_number(number):

    assert number == 10
'''
'''
import pytest
from playwright.sync_api import sync_playwright

# ==========================================
# 🎯 CHALLENGE 1: Your First Fixture (Pure Python)
# ==========================================
# @pytest.fixture is a magic tag. It tells Robin: "This is not a test. This is an Assistant."
@pytest.fixture
def number():
    # The assistant prepares the number 10
    return 10

# We pass the name of the fixture (number) into the test parentheses!
def test_number(number):
    # The test receives the number 10 and checks it.
    assert number == 10


# ==========================================
# 🎯 CHALLENGES 2, 3 & 4: The Reusable Page Fixture
# ==========================================
@pytest.fixture
def page():
    # --- SETUP ---
    # The assistant starts Playwright and opens the browser
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    
    # --- PAUSE BUTTON ---
    # Hand the page to the test, and wait for the test to finish.
    yield page
    
    # --- CLEANUP ---
    # The test is done! Close the browser and stop Playwright.
    browser.close()
    playwright.stop()

# Notice we don't have 'sync_playwright' or 'browser.launch' in these tests anymore!
def test_google_title(page):
    page.goto("https://www.google.com")
    assert "Google" in page.title()

def test_google_url(page):
    page.goto("https://www.google.com")
    assert "google" in page.url.lower()

def test_google_page(page):
    page.goto("https://www.google.com")
    assert page.locator("body").is_visible()

def test_login_page(page):
    page.goto("https://the-internet.herokuapp.com/login")
    # Note: The actual <title> of this page is "The Internet", not "Login Page"!
    # So we check the h2 text instead to make sure we are on the right page.
    assert "Login Page" in page.locator("h2").inner_text()


# ==========================================
# 🏆 CHALLENGE 5: Fixture with Login!
# ==========================================
# This is Master Level. We create an Assistant that logs in for us!
@pytest.fixture
def logged_in_page():
    # --- SETUP ---
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    
    # The assistant does the boring login steps
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button.radius").click()
    
    # --- PAUSE BUTTON ---
    # Hand the ALREADY LOGGED IN page to the test!
    yield page
    
    # --- CLEANUP ---
    browser.close()
    playwright.stop()

# This test is super short because the Assistant did all the hard work!
def test_secure_area(logged_in_page):
    # The page is already logged in. We just check the green success banner.
    message = logged_in_page.locator("#flash").inner_text()
    assert "You logged into a secure area!" in message
'''
#==============================================
#==============================================
import pytest
from playwright.sync_api import sync_playwright
@pytest.fixture
def number():
    return  10
def test_number(number):
    assert number == 10
@pytest.fixture
def page():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page= browser.new_page()
    yield page
    browser.close()
    playwright.stop()
def test_google_title(page):
    page.goto("https://www.google.com")
    assert "Google" in page.title()
def test_google_url(page):
    page.goto("https://www.google.com")
    assert "google" in page.url.lower()
def test_google_page(page):
    page.goto("https://www.google.com")
    assert page.locator("body").is_visible()
def test_login_page(page):
    page.goto("https://the-internet.herokuapp.com/login")
    assert "Login Page" in page.locator("h2").inner_text()
@pytest.fixture
def logged_in_page():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button.radius").click()
    yield page
    browser.close()
    playwright.stop()
def test_secure_are(logged_in_page):
    message = logged_in_page.locator("#flash").inner_text()
    assert ("You logged into a secure area!") in message
