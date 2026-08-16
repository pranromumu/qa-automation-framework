
from components.flash_message import FlashMeggase
class SecurePage:
    def __init__(self,page):
        self.page = page
        self.flash_message =FlashMessase(page)
    def get_secure_message(self):
        return self.flash_message.get_message()
