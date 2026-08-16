
'''
from playwright.sync_api import sync_playwright

# We brought back Robin!
def test_storage_challenges():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/")
        
        print("--- 🏆 LOCAL STORAGE CHALLENGES ---")
        
        # Challenge 1 & 2: Create user and language, read and print
        page.evaluate("localStorage.setItem('user', 'Kabir')")
        page.evaluate("localStorage.setItem('language', 'English')")
        
        user_val = page.evaluate("localStorage.getItem('user')")
        lang_val = page.evaluate("localStorage.getItem('language')")
        
        print(f"User: {user_val}")
        print(f"Language: {lang_val}")
        
        # Assert both
        assert user_val == "Kabir"
        assert lang_val == "English"
        print("✅ Verified both LocalStorage items!")
        
        # Challenge 3: Remove user item
        page.evaluate("localStorage.removeItem('user')")
        
        # Read user again
        user_after_remove = page.evaluate("localStorage.getItem('user')")
        print("User after remove:", user_after_remove)
        
        # Verify it is None (Python's word for JavaScript null)
        assert user_after_remove is None
        print("✅ Verified user is gone (None)!")
        
        # Challenge 4: Clear Everything
        # Let's put user back just to make sure clear() wipes everything
        page.evaluate("localStorage.setItem('user', 'Kabir')")
        page.evaluate("localStorage.clear()")
        
        user_after_clear = page.evaluate("localStorage.getItem('user')")
        lang_after_clear = page.evaluate("localStorage.getItem('language')")
        
        assert user_after_clear is None
        assert lang_after_clear is None
        print("✅ Verified everything is cleared!")
        
        
        print("\n--- 🔥 SESSION STORAGE CHALLENGE ---")
        
        # Challenge 5: Session Storage
        # SessionStorage works exactly like LocalStorage, but it disappears 
        # the moment you close the browser tab!
        page.evaluate("sessionStorage.setItem('session_user', 'Kabir')")
        
        session_val = page.evaluate("sessionStorage.getItem('session_user')")
        print("Session User:", session_val)
        
        assert session_val == "Kabir"
        print("✅ Verified SessionStorage item!")
        
        print("\n🎉 ALL STORAGE CHALLENGES PASSED! 🎉")
        browser.close()
 '''
'''
Open browser
      ↓
Open website
      ↓
Create localStorage:
user = Kabir
      ↓
Create localStorage:
language = English
      ↓
Read both
      ↓
Assert both
      ↓
Remove user
      ↓
Verify user is gone
      ↓
Create sessionStorage:
session_user = Kabir
      ↓
Read it
      ↓
Assert it
'''

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/")
    print("🙌 Local Storage Challenge!")
    # -----------------------------
    # Challenge 1 & 2
    # -----------------------------
    page.evaluate("localStorage.setItem('user', 'Kabir')")
    page.evaluate("localStorage.setItem('language', 'English')")
    user_val = page.evaluate(
        "localStorage.getItem('user')"
    )
    user_lan = page.evaluate(
        "localStorage.getItem('language')"
    )
    print("User:", user_val)
    print("Language:", user_lan)
    assert user_val == "Kabir"
    assert user_lan == "English"
    print("✅ Storage verified!")
    # -----------------------------
    # Challenge 3
    # -----------------------------
    page.evaluate(
        "localStorage.removeItem('user')"
    )
    user_after_remove = page.evaluate(
        "localStorage.getItem('user')"
    )
    print("After removing user:", user_after_remove)
    assert user_after_remove is None
    print("✅ User successfully removed!")
    # -----------------------------
    # Challenge 4
    # -----------------------------
    page.evaluate(
        "localStorage.setItem('user', 'Kabir')"
    )
    page.evaluate(
        "localStorage.clear()"
    )
    user_after_clear = page.evaluate(
        "localStorage.getItem('user')"
    )
    lang_after_clear = page.evaluate(
        "localStorage.getItem('language')"
    )
    assert user_after_clear is None
    assert lang_after_clear is None
    print("✅ Local Storage completely cleared!")
    # -----------------------------
    # Challenge 5
    # -----------------------------
    print("\n---- Session Storage Challenge ----")
    page.evaluate(
        "sessionStorage.setItem('session_user', 'Kabir')"
    )
    session_val = page.evaluate(
        "sessionStorage.getItem('session_user')"
    )
    print("Session User:", session_val)
    assert session_val == "Kabir"
    print("✅ Session Storage verified!")
    browser.close()
