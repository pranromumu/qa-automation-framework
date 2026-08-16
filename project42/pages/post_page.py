

class PostPage:
    def __init__(self,page):
        self.page = page
        self.body_text = page.locator("body")
    def navigate_to_post(self,post_id):
        self.page.goto(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    def get_display_text(self):
        return self.body_text.inner_text()

    