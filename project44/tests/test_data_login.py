import json
import pytest
from pages.login_page import LoginPage
import os
file_path = os.path.join(os.path.dirname(__file__), "..", "test_data", "users.json")
with open(file_path, "r") as file:
    user_data = json.load(file)
@pytest.mark.parametrize("user", user_data)
def test_login_with_json(page, user):
    page.goto("https://the-internet.herokuapp.com/login")
    login_page = LoginPage(page)
    login_page.login(user["username"], user["password"])
    
    message = page.locator("#flash").inner_text()
    
    if user["expected"]:
        assert "You logged into a secure area!" in message
        print(f"\n✅ Success test passed for: {user['username']}")
    else:
        assert "invalid" in message.lower()
        print(f"\n✅ Expected failure test passed for: {user['username']}")