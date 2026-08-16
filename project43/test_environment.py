

def test_homepage(page,base_url):
    page.goto(base_url)
    assert "The Internet" in page.title()
    print(f"\n environment URL:{base_url}")
def test_authenticated_user(authenticated_page):
    assert "/secure"in authenticated_page.url
    print("\n Authentication test passed")