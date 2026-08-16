

from pages.login_page import LoginPage
from pages.secure_page import SecurePage
def test_login_and_verify(page):
    page.goto("https://the-internet.herokuapp.com/login")
    login_page = LoginPage(page)
    login_page.login("tomsmith", "SuperSecretPassword!")
    secure_page =SecurePage(page)
    message = secure_page.get_secure_message()
    assert "You logged into a secure area!" in message
    print("Done!")