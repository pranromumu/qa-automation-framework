import json
import pytest
from playwright.sync_api import sync_playwright

with open ("test_data.json","r") as file:
    user_data = json.load(file)
    print(user_data)
@pytest.fixture
def page():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    yield page
    browser.close()
    playwright.stop()
@pytest.mark.parametrize("user",user_data)
def test_login(page ,user):
    username = user["username"]
    password = user["password"]
    should_succeed = user["expected"]
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill(username)
    page.locator("#password").fill(password)
    page.locator("butuon.radius").click()
    if should_succeed:
        message = page.locator("#flash").inner_text()
        assert "You logged into a secure area!" in message
    else:
        message  = page.locator("#flash").inner_text()
        assert "your password is invalid!" in message.lower()