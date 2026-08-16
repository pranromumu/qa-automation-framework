import pytest
from playwright.sync_api import sync_playwright
from config import ENVIRONMENTS
from pages.login_page import LoginPage
@pytest.fixture
def page():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    yield page
    browser.close()
    playwright.stop()
@pytest.fixture
def base_url():
    environment = "staging"
    url = ENVIRONMENTS[environment]
    return url
@pytest.fixture
def authenticated_page(page,base_url):
    page.goto(f"{base_url}/login")
    login_page = LoginPage(page)
    login_page.login("tomsmith", "SuperSecretPassword!")
    yield page