
'''
from playwright.sync_api import sync_playwright

# We brought back Robin!
def test_key_presses():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/key_presses")
        
        # 🎯 CHALLENGE 4: Create a list of keys!
        keys = ["A", "B", "Enter", "Escape"]
        
        # Loop through the list
        for key in keys:
            # Click the body to make sure the page is ready
            page.locator("body").click()
            
            # Press the current key
            page.keyboard.press(key)
            
            # Wait a tiny bit for the text to update
            page.wait_for_timeout(500)
            
            # Read the result
            result = page.locator("#result").text_content()
            
            # Print the result
            print(f"Pressed {key} -> Result: {result}")
            
            # 🎯 CHALLENGES 1, 2, & 3: Verify the result!
            # The website prints everything in UPPERCASE (e.g., "ENTER").
            # So we use .upper() to make our key uppercase before we check it!
            assert key.upper() in result
            print(f"Verified {key} successfully!\n")
            
        print("🎉 ALL KEY PRESS CHALLENGES PASSED! 🎉")
        browser.close()
'''

from playwright.sync_api import sync_playwright
def keyboard_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/key_presses")
        keys = ["A", "B", "Enter", "Escape"]
        for key in keys:
            page.locator("body").click()
            page.keyboard.press(key)
            result = page.locator("#result").text_content()
            print(f"Key: {key}")
            print("Result:", result)
            assert key.upper() in result.upper()
            print(f"✅ {key} successfully verified")
        print("🎉 All keyboard challenges passed!")
        browser.close()

keyboard_test()
