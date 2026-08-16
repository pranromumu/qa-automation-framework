

import pytest
from playwright.sync_api import sync_playwright
from login_page import LoginPage
from secure_page import SecurePage
@pytest.fixture
def page():
    playwright = sync_playwright().start()
    browser = playwrihgt.chromium.launch(headless=False)
    page = browser.new_page()
    yield page
    browser.close()
    playwrihgt.stop()
def test_login_and_verify(page):
    page.goto("https://the-internet.herokuapp.com/login")
    login_page = LoginPage(page)
    login_page.login("tomsmith", "SuperSecretPassword!")
    secure_page = SecurePage(page)
    message = secure_page.get_flash_message()
    assert "You logged into a secure area!" in message
    print("done")
