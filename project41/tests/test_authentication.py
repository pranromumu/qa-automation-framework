from pages.secure_page import SecurePage

def test_authenticated_user(authenticated_page):
    assert "/secure" in authenticated_page.url
def test_authenticated_message(authenticated_page):
    secure_page = SecurePage(authenticated_page)
    message = secure_page.get_secure_message()
    assert "You logged into a secure area!" in message
    
