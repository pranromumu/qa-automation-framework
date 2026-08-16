import json
import os
import pytest
from playwright.sync_api import sync_playwright
@pytest.fixture
def users():
    file_path = os.path.join(os.path.dirname(__file__), "test_data", "users.json")
    with open("test_data/users.json", "r") as file:
        return json.load(file)
@pytest.fixture
def page():
    playwright= sync_playwright().start()
    browser= playwright.chromium.launch(headless=False)
    page = browser.new_page()
    print(f"\n worker page created:{page}")
    yield page
    browser.close()
    playwright.stop()