

import logging
from pages.login_page import LoginPgae
from pages.secure_page import SecurePage

def test_login(page):
    logging.info("Opening login page")
    page.goto("https://the-internet.herokuapp.com/login")

    login_page = LoginPgae(page)
    logging.info("Loggin in")
    login_page.login("tomsmith", "SuperSecretPassword!")

    logging.info("Secure page")
    secure_page = SecurePage(page)

    logging.info("Checking secure message")
    message = secure_page.get_secure_message()
    assert "You logged into a secure area!" in message
    logging.info("Test complete")