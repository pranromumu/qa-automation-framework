
'''
import pytest
from playwright.sync_api import sync_playwright

# Because we don't have conftest.py yet, we have to copy the fixture here too!
@pytest.fixture
def page():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    yield page
    browser.close()
    playwright.stop()

# ✅ Discovered!
def test_login_page(page):
    page.goto("https://the-internet.herokuapp.com/login")
    assert "Login Page" in page.locator("h2").inner_text()
'''



#=============================================================
import pytest
from playwright.sync_api import sync_playwright
@pytest.fixture
def page():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    peage = browser.new_page()
    yield page
    browser.close()
    playwright.stop()
def test_login_page(page):
    page.goto("https://the-internet.herokuapp.com/login")
    assert "Login Page" in page.locator.inner_text()