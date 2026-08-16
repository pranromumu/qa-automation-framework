

import pytest
from playwright.sync_api import sync_playwright
@pytest.fixture
def api_request():
    playwright= sync_playwright().start()
    request= playwright.request.new_context()
    yield request
    request.dispose()
    playwright.stop()
@pytest.fixture
def page():
    playwright= sync_playwright().start()
    browser= playwright.chromium.launch(headless=False)
    page= browser.new_page()
    yield page
    browser.close()
    playwright.stop()

    