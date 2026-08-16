
'''
# We need to import the Playwright magic wand
from playwright.sync_api import sync_playwright

# 🎯 CHALLENGE 4: Your First Playwright + Pytest Test
def test_google_title():
    # We wake up the robot using the 'with' block
    with sync_playwright() as p:
        # Open the Chromium browser (headless=False means we can see it)
        browser = p.chromium.launch(headless=False)
        # Open a brand new blank page
        page = browser.new_page()
        
        # Tell the robot to go to Google
        page.goto("https://www.google.com")
        
        # The Verification!
        # page.title() grabs the text on the browser tab.
        # We tell Robin: "Check if the word 'Google' is in the title."
        assert "Google" in page.title()
        
        # Always clean up and close the browser to save computer memory!
        browser.close()


# 🎯 CHALLENGE 5: Two Playwright Tests in one file!
# Pytest will run the test above, and then it will run this one below it.
def test_google_url():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.google.com")
        
        # This time we are checking the URL (the website address).
        # page.url grabs the address (e.g., "https://www.google.com")
        # .lower() makes it all lowercase so we don't have to worry about capitals.
        # We tell Robin: "Check if 'google' is in the website address."
        assert "google" in page.url.lower()
        
        browser.close()
'''
# When you type 'pytest' in the terminal, Robin will run both tests!
# You will see '..' which means 2 tests passed!

from playwright.sync_api import sync_playwright
def test_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.google.com")
        assert "Google" in page.title()
        browser.close()
def test_check_url():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.google.com")
        assert "google" in page.url.lower()
        browser.close()