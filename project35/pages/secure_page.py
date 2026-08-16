

from flash_message import FlashMessage
class SecurePage:
    def __init__(self,page):
        self.page = page
        self.flash_message = FlashMessage(page)
    def get_secure_message(self):
        return self.flash_meaasge.get_message()
    