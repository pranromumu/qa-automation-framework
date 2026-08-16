from playwright.sync_api import sync_playwright
'''
# 🏆 CHALLENGE 5: Create a reusable helper function!
def check_status(page, link_text, expected_status):
    # We wait for the response that matches the specific status code URL
    with page.expect_response(f"**/status_codes/{link_text}") as response_info:
        # Click the link that matches the text (e.g., "200" or "404")
        page.locator(f"text={link_text}").first.click()
    
    # Grab the response out of the net
    response = response_info.value
    print(f"Clicked {link_text} -> Status: {response.status}")
    
    # Assert the expected status
    assert response.status == expected_status
    print(f"✅ Verified {expected_status}!")
    
    # Go back to the main status_codes page so we can click the next one
    page.go_back()


# We brought back Robin!
def test_network_challenges():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        
        # 🎯 CHALLENGES 1 & 2: Capture main page load
        print("--- Main Page Load ---")
        with page.expect_response("**/") as response_info:
            page.goto("https://the-internet.herokuapp.com/")
        
        response = response_info.value
        print("Status:", response.status)
        print("URL:", response.url)
        assert response.status == 200
        assert "the-internet.herokuapp.com" in response.url
        print("✅ Challenges 1 & 2 Passed!")
        
        # 🎯 CHALLENGES 3, 4, & 5: Check Status Codes
        print("\n--- Status Codes Page ---")
        page.goto("https://the-internet.herokuapp.com/status_codes")
        
        # Use our helper function! It clicks the link, checks the status, and goes back!
        # 🎯 Challenge 3
        check_status(page, "200", 200)
        
        # 🎯 Challenge 4
        check_status(page, "404", 404)
        
        print("\n🎉 ALL NETWORK CHALLENGES PASSED! 🎉")
        browser.close()
'''
'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # =====================================
    # Challenge 1 & 2 — Main page
    # =====================================
    with page.expect_response("**/") as response_info:
        page.goto("https://the-internet.herokuapp.com/")
    response = response_info.value
    print("Status:", response.status)
    print("URL:", response.url)
    assert response.status == 200
    assert "the-internet.herokuapp.com" in response.url
    print("✅ Main page response verified!")

    # =====================================
    # Challenge 3 — Status 200
    # =====================================
    page.goto("https://the-internet.herokuapp.com/status_codes")
    with page.expect_response("**/status_codes/200") as response_info:
        page.locator("a", has_text="200").click()
    response = response_info.value
    print("200 Test Status:", response.status)
    assert response.status == 200
    print("✅ 200 response verified!")
    # =====================================
    # Challenge 4 — Status 404
    # =====================================
    page.goto("https://the-internet.herokuapp.com/status_codes")
    with page.expect_response("**/status_codes/404") as response_info:
        page.locator("a", has_text="404").click()
    response = response_info.value
    print("404 Test Status:", response.status)
    assert response.status == 404
    print("✅ 404 response verified!")
    browser.close()
'''
from playwright.sync_api import sync_playwright
def check_status(page, expected_status):
    with page.expect_response(
        f"**/status_codes/{expected_status}") as response_info:
    page.locator("a",has_text=str(expected_status) ).click()
    response = response_info.value
    print("Expected:",expected_status,"Actual:",response.status)
    assert response.status == expected_status
    print("✅ Status verified!")
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # -----------------------------
    # Main page
    # -----------------------------
    with page.expect_response("**/") as response_info:
        page.goto( "https://the-internet.herokuapp.com/")
    response = response_info.value
    print("Main page status:", response.status)
    print("Main page URL:", response.url)
    assert response.status == 200
    print("✅ Main page verified!")
    # -----------------------------
     # Status codes
    # -----------------------------
    page.goto("https://the-internet.herokuapp.com/status_codes")
    check_status(page, 200)
    page.goto("https://the-internet.herokuapp.com/status_codes")
    check_status(page, 404)
    browser.close()