


import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="class")
def browser_page():
    print("\n=== Creating browser ===")
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    yield page
    print("\n=== Closing browser ===")
    browser.close()
    playwright.stop()
class TestSearchEngine:
    def test_google(self, browser_page):
        browser_page.goto("https://www.google.com")
        assert "Google" in browser_page.title()
    def test_bing(self, browser_page):
        browser_page.goto("https://www.bing.com")
        assert "bing" in browser_page.title().lower()
class TestEncyclopedia:
    def test_wikipedia(self, browser_page):
        browser_page.goto("https://www.wikipedia.org")
        assert "Wikipedia" in browser_page.title()