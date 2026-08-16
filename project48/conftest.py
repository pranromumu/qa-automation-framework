

import os
import pytest
import logging
from playwright.sync_api import sync_playwright

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s -%(levelname)s - %(message)s"
)

@pytest.fixture
def page():
    playwright=sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    yield page
    browser.close()
    playwright.stop()

# 3. THE SPIDER WEB (The Hook)!
# This magic spell runs after every single test.
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Wait for the test to finish
    outcome = yield
    report = outcome.get_result()
    
    # Check: Did the test just fail?
    if report.when == "call" and report.failed:
        # Grab the page from the fixture
        page = item.funcargs.get("page")
        if page:
            # Make sure the screenshots folder exists
            os.makedirs("screenshots", exist_ok=True)
            
            # Save the picture with the name of the test!
            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path, full_page=True)
            
            print(f"\n📸 Screenshot saved: {screenshot_path}")