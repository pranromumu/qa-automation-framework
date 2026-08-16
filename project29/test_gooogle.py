

'''
import pytest
from playwright.sync_api import sync_playwright

# Here is our Assistant (Fixture) from Project 28!
@pytest.fixture
def page():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    yield page
    browser.close()
    playwright.stop()

# ✅ Discovered!
def test_google_title(page):
    page.goto("https://www.google.com")
    assert "Google" in page.title()

# ✅ Discovered!
def test_google_url(page):
    page.goto("https://www.google.com")
    assert "google" in page.url.lower()
'''

#============================================
import pytest
from playwright.sync_api import sync_playwright
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
def test_page_url(page):
    page.goto("https://www.google.com")
    assert "google" in page.url.lower()

    