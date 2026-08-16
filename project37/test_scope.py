



import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser_page():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    yield page
    browser.close()
    playwright.stop()
def test_one(browser_page):
    browser_page.goto("https://www.google.com")
    assert "Google" in browser_page.title()
def test_two(browser_page):
    browser_page.goto("https://www.bing.com")
    assert "bing" in browser_page.title().lower()
def test_three(browser_page):
    browser_page.goto("https://www.wikipedia.org")
    assert "Wikipedia" in browser_page.title()