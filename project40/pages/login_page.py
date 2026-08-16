

class LoginPage:
    def __init__(self,page):
        self.page = page
        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.login_button = page.locator("button.radius")
    def login(self,username,password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

