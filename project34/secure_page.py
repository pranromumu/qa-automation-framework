

class SecurePage:
    def __init__(self,page):
        self.page = page
        self.flash_message = page.locator("#flash")
    def get_secure_message(self):
        return self.flash_message.inner_text()