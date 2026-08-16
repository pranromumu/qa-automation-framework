

import logging
class LoginPage:
    def __init__(self,page):
        self.page = page
        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.login_button = page.locator("button.radius")
    def login(self,username,password):
        logging.info("entering username")
        self.username.fill(username)
        logging.info("entering password")
        self.password.fill(password)
        logging.info("click login button")
        self.login_button.click()
        logging.info("Login button clicked")