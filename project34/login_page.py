

class LoginPage:
    def __init__(self,page):
        self.page = page
        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.login_button =page.locator("button.radius")
    def enter_username(self,username):
        self.username.fill(username)
    def enter_password(self,password):
        self.password.fill(password)
    def click_login(self):
        self.login_button.click()
    def login(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()


        