

import logging
import pytest
from playwright.sync_api import sync_playwright

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@pytest.fixture
def page():
    playwright= sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page =browser.new_page()
    yield page
    browser.close()
    playwright.stop()
