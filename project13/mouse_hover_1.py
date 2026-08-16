
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/hovers")       
        profiles = page.locator(".figure")       
        for i in range(profiles.count()):
            current_profile = profiles.nth(i)
            current_profile.hover()
            current_caption = page.locator(".figcaption").nth(i)
            text = current_caption.inner_text()
            print(f"Profile {i+1} says:", text)
            if i == 1:
                assert "user2" in text
                print("Challenge 1 & 2 Passed: Found user2!")
            profile_link = current_caption.locator("a")
            is_it_visible = profile_link.is_visible()            
            assert is_it_visible == True
            print(f"Challenge 3 Passed: View profile is visible for profile {i+1}!")    
        print("🎉 ALL HOVER CHALLENGES PASSED! 🎉")
        browser.close()