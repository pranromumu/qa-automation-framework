

class FlashMessage:
    def __init__(self,page):
        self.page =page
        self.message = page.locator("#flash")
    def get_message(self):
        return self.message.inner_text()
      