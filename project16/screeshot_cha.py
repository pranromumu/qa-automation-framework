from playwright.sync_api import sync_playwright

# We brought back Robin!
def test_screenshot_challenges():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        
        # ==========================================
        # 🏆 CHALLENGES 1, 2, & 3: Successful Login
        # ==========================================
        print("--- Testing Successful Login ---")
        page.goto("https://the-internet.herokuapp.com/login")
        
        # Login steps
        page.locator("#username").fill("tomsmith")
        page.locator("#password").fill("SuperSecretPassword!")
        page.locator("button[type='submit']").click()
        
        # Wait a tiny bit for the green success banner
        page.wait_for_timeout(1000)
        
        # Verify success
        success_message = page.locator("#flash").inner_text()
        assert "You logged into a secure area" in success_message
        print("Login verified!")
        
        # 📸 Take a screenshot with a meaningful name!
        page.screenshot(path="login_success.png")
        print("Saved: login_success.png")
        
        # ==========================================
        # 🏆 CHALLENGE 4: Failed Login
        # ==========================================
        print("\n--- Testing Failed Login ---")
        page.goto("https://the-internet.herokuapp.com/login")
        
        # Login with WRONG password
        page.locator("#username").fill("tomsmith")
        page.locator("#password").fill("WrongPassword123!") # Oops! Wrong password!
        page.locator("button[type='submit']").click()
        
        # Wait a tiny bit for the red error banner
        page.wait_for_timeout(1000)
        
        # Verify error message
        error_message = page.locator("#flash").inner_text()
        assert "Your password is invalid" in error_message
        print("Error verified!")
        
        # 📸 Take a screenshot of the failure!
        page.screenshot(path="login_failed.png")
        print("Saved: login_failed.png")
        
        browser.close()


from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # -------------------------
    # Successful Login
    # -------------------------
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button[type='submit']").click()
    success_message = page.locator("#flash").inner_text()
    assert "You logged into a secure area" in success_message
    print("✅ Login verified!")
    page.screenshot(path="login_success.png")
    print("📸 Success screenshot saved")
    # -------------------------
    # Failed Login
    # -------------------------
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("wrongpassword123")
    page.locator("button[type='submit']").click()
    error_message = page.locator("#flash").inner_text()
    assert "Your password is invalid" in error_message
    print("✅ Error message verified!")
    page.screenshot(path="login_failed.png")
    print("📸 Failed screenshot saved")
    browser.close()