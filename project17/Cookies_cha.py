'''
from playwright.sync_api import sync_playwright

# We brought back Robin!
def test_cookie_challenges():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        
        # 1. Open page
        page.goto("https://the-internet.herokuapp.com/")
        
        # 2 & 3. Add TWO cookies at the same time!
        context.add_cookies([
            {
                "name": "user",
                "value": "Kabir",
                "domain": "the-internet.herokuapp.com",
                "path": "/"
            },
            {
                "name": "language",
                "value": "English",
                "domain": "the-internet.herokuapp.com",
                "path": "/"
            }
        ])
        
        # 4 & 5. (Done above!)
        
        # 6. Read cookies
        cookies = context.cookies()
        print("\n--- Cookies Found ---")
        print(cookies)
        
        # 7 & 8. Verify both cookies!
        # The cookies come back as a list of dictionaries. 
        # Let's look through them to find ours.
        user_cookie = None
        lang_cookie = None
        
        for cookie in cookies:
            if cookie["name"] == "user":
                user_cookie = cookie
            elif cookie["name"] == "language":
                lang_cookie = cookie
                
        assert user_cookie is not None
        assert user_cookie["value"] == "Kabir"
        print("Verified: user cookie is Kabir!")
        
        assert lang_cookie is not None
        assert lang_cookie["value"] == "English"
        print("Verified: language cookie is English!")
        
        # 9. Clear cookies!
        context.clear_cookies()
        print("\nCookies cleared!")
        
        # 10. Verify they are gone!
        cookies_after = context.cookies()
        print("Cookies after clearing:", cookies_after)
        
        # len() is a magic spell that counts how many things are in a list.
        # If the list is empty, len() will be 0!
        assert len(cookies_after) == 0
        print("Verified: All cookies are gone!")
        
        browser.close()
'''

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/")
    # Create cookies
    context.add_cookies([
        {
            "name": "user",
            "value": "Kabir",
            "domain": "the-internet.herokuapp.com",
            "path": "/"
        },
        {
            "name": "language",
            "value": "English",
            "domain": "the-internet.herokuapp.com",
            "path": "/"
        }
    ])
    # Read cookies
    cookies = context.cookies()
    print("Cookies:", cookies)
    # Find cookies
    user_cookie = None
    lang_cookie = None
    for cookie in cookies:
        if cookie["name"] == "user":
            user_cookie = cookie
        elif cookie["name"] == "language":
            lang_cookie = cookie
    # Verify user cookie
    assert user_cookie is not None
    assert user_cookie["value"] == "Kabir"
    print("✅ Verified: user cookie is Kabir!")
    # Verify language cookie
    assert lang_cookie is not None
    assert lang_cookie["value"] == "English"
    print("✅ Verified: language cookie is English!")
    # Clear cookies
    context.clear_cookies()
    print("🧹 Cookies cleared")
    # Check cookies again
    cookies_after = context.cookies()
    print("Cookies after clearing:", cookies_after)
    assert len(cookies_after) == 0
    print("✅ All cookies are gone!")
    browser.close()