

import pytest
from playwright.sync_api import sync_playwright
from login_page import LoginPage
@pytest.fixture
def page():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    yield page
    browser.close()
    playwright.stop()
def test_login_page_with_pom(page):
    page.goto("https://the-internet.herokuapp.com/login")
    login_page = LoginPage(page)
    login_page.enter_username("tomsmith")
    login_page.enter_password("SuperSecretPassword!")
    login_page.click_login()
    message = page.locator("#flash").inner_text()
    assert "You logged into a secure area!" in message
    print("Test passed")