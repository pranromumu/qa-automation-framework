


import logging
from pages.login_page import LoginPage
from pages.secure_page import SecurPage

def test_login_and_verify(page):
    logging.info("Opening login page")
    page.goto("https://the-internet.herokuapp.com/login")
    login_page = LoginPage(page)
    login_page.login("tomsmith", "SuperSecretPassword!")
    logging.info("login completed")
    secure_page = SecurPage(page)
    logging.info("Geting secure message")
    message = secure_page.get_secure_message()
    logging.info("validating Secure message")
    assert "You logged into a secure area!" in message
    logging.info("done!")