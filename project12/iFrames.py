from playwright.sync_api import sync_playwright

# 1. We brought back Robin!
def test_iframes_challenges():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/iframe")
        
        # Go inside the secret box
        editor = page.frame_locator("#mce_0_ifr")
        
        # 2. THE FIX: Use .focus() to wake up the keyboard without clicking!
        editor.locator("p").focus()
        
        # CHALLENGE 1: Write your name
        page.keyboard.type("Kabir")
        print("Challenge 1 Done!")
        
        # CHALLENGE 3: Clear the editor, then write new text
        # We use the keyboard to clear because .clear() doesn't work here!
        page.keyboard.press("Control+A")
        page.keyboard.press("Delete")
        page.keyboard.type("Playwright is awesome!")
        print("Challenge 3 Done!")
        
        # CHALLENGE 2: Print the editor text (using 'editor', not 'page')
        text = editor.locator("#tinymce").inner_text()
        print("Challenge 2 Done -> The text is:", text)
        
        # CHALLENGE 4: Verify the text is EXACTLY right
        assert text == "Playwright is awesome!"
        print("Challenge 4 Done! All tests passed!")
        
        browser.close()