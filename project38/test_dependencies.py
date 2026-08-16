

import pytest
from playwright.sync_api import sync_playwright
@pytest.fixture
def browser():
    print("\n SETUP:  starting browser")
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    yield browser
    print("\n CLEANUP: broser close")
    browser.close()
    playwright.stop()

@pytest.fixture  #Depand on browser
def page(browser):
    print("\n SETUP: creating page")
    page = browser.new_page()
    yield page
@pytest.fixture
def logged_in_page(page):
    print("\n SETUP: start logged in..")
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button.radius").click()
    yield page
def test_secure_page(logged_in_page):
    print("\n Veryfy: logged in")
    message = logged_in_page.locator("#flash").inner_text()
    assert "You logged into a secure area!" in message
    assert "/secure" in logged_in_page.url
    print("Done!")



