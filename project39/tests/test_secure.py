from pages.secure_page import SecurePage
def test_secure_page(logged_in_page):
    secure_page = SecurePage(logged_in_page)
    message = secure_page.get_secure_message()
    assert "You logged into a secure area!" in message
    assert "/secure" in logged_in_page.url
    print("Done!")
 