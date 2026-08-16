
'''
from playwright.sync_api import sync_playwright

# We brought back Robin!
def test_api_mocking():
    with sync_playwright() as p:
        # We can use headless=True because we are just reading text from the body!
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        target_url = "https://jsonplaceholder.typicode.com/posts/1"
        
        # ==========================================
        # 🎯 CHALLENGES 2 & 3: Fulfill a Fake 200 Post
        # ==========================================
        def fulfill_fake_post(route):
            print("Intercepted! Sending FAKE POST...")
            route.fulfill(
                status=200,
                content_type="application/json",
                body='{"id": 1, "title": "FAKE POST"}'
            )
        
        # Tell the page to use our fake fulfiller
        page.route(target_url, fulfill_fake_post)
        
        # Go to the page (it will get our fake response!)
        page.goto(target_url)
        text = page.locator("body").inner_text()
        print("Browser received:", text)
        
        assert "FAKE POST" in text
        print("✅ Challenges 2 & 3 Passed: Mocked successful post!\n")
        
        # ==========================================
        # 🎯 CHALLENGE 4: Mock a 500 Server Error
        # ==========================================
        def fulfill_server_error(route):
            print("Intercepted! Sending 500 ERROR...")
            route.fulfill(
                status=500,
                content_type="application/json",
                body='{"error": "Internal Server Error"}'
            )
        
        # We unroute the old one, and route the new one!
        page.unroute(target_url, fulfill_fake_post)
        page.route(target_url, fulfill_server_error)
        
        page.goto(target_url)
        text = page.locator("body").inner_text()
        print("Browser received:", text)
        
        assert "Internal Server Error" in text
        print("✅ Challenge 4 Passed: Mocked server error!\n")
        
        # ==========================================
        # 🏆 CHALLENGE 5: Mock Empty Data
        # ==========================================
        def fulfill_empty_data(route):
            print("Intercepted! Sending EMPTY DATA...")
            route.fulfill(
                status=200,
                content_type="application/json",
                body="[]"
            )
        
        # Swap the routes one last time!
        page.unroute(target_url, fulfill_server_error)
        page.route(target_url, fulfill_empty_data)
        
        page.goto(target_url)
        text = page.locator("body").inner_text()
        print("Browser received:", text)
        
        assert "[]" in text
        print("✅ Challenge 5 Passed: Mocked empty data!")
        
        print("\n🎉🎉🎉 ALL MOCKING CHALLENGES PASSED! YOU ARE A NETWORK WIZARD! 🎉🎉🎉")
        
        browser.close()
'''

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    target_url = "https://jsonplaceholder.typicode.com/posts/1"
    # ==========================================
    # Challenge 2 & 3
    # Fake successful response
    # ==========================================

    def fulfill_fake_post(route):

        print("Intercepted: sending fake POST...")

        route.fulfill(
            status=200,
            content_type="application/json",
            body='{"id": 1, "title": "fake POST"}'
        )

    page.route(target_url, fulfill_fake_post)
    page.goto(target_url)
    text = page.locator("body").inner_text()
    print(text)
    assert "fake POST" in text
    print("✅ Challenge 2 & 3 Done!")
    # ==========================================
    # Challenge 4
    # Fake 500 Server Error
    # =========================================
    def fulfill_server_error(route):
        print("Intercepted: sending 500 ERROR...")
        route.fulfill(
            status=500,
            content_type="application/json",
            body='{"error": "Internal Server Error"}'
        )
    page.unroute(target_url)
    page.route(target_url, fulfill_server_error)
    page.goto(target_url)
    text = page.locator("body").inner_text()
    print(text)
    assert "Internal Server Error" in text
    print("✅ Challenge 4 Done!")
    # ==========================================
    # Challenge 5
    # Fake Empty Data
    # ==========================================
    def fulfill_empty_data(route):

        print("Intercepted: sending EMPTY DATA...")

        route.fulfill(
            status=200,
            content_type="application/json",
            body="[]"
        )
    page.unroute(target_url)
    page.route(target_url, fulfill_empty_data)
    page.goto(target_url)
    text = page.locator("body").inner_text()
    print(text)
    assert text == "[]"
    print("✅ Challenge 5 Done!")
    print("🎉 Project 25 Completed!")
    browser.close()

