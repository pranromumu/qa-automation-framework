

import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

@pytest.fixture
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()
    playwright.stop()
@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
@pytest.fixture
def logged_in_page(page):
    page.goto("https://the-internet.herokuapp.com/login")
    login_page = LoginPage(page)
    login_page.login("tomsmith", "SuperSecretPassword!")
    yield page


