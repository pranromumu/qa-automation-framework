

from components.flash_message import FlashMessage

class SecurPage:
    def __init__(self,page):
        self.page = page
        self.flash_message =FlashMessage(page)
    def get_secure_message(self):
        return self.flash_message.get_message()
