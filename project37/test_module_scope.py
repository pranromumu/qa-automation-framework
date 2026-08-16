


import pytest
from playwright.sync_api import sync_playwright
@pytest.fixture(scope="module")
def browser_page():
    print("\n=== Creating browser ===")
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    yield page
    print("\n=== Closing browser ===")
    browser.close()
    playwright.stop()

def test_google(browser_page):
    browser_page.goto("https://www.google.com")
    assert "Google" in browser_page.title()
    print("Google test passed")
def test_bing(browser_page):
    browser_page.goto("https://www.bing.com")
    assert "bing" in browser_page.title().lower()
    print("Bing test passed")
def test_wikipedia(browser_page):
    browser_page.goto("https://www.wikipedia.org")
    assert "Wikipedia" in browser_page.title()
    print("Wikipedia test passed")