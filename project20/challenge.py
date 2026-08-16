'''
from playwright.sync_api import sync_playwright

# We brought back Robin!
def test_api_challenges():
    with sync_playwright() as p:
        # We can use headless=True for API tests because we don't need to watch a browser click buttons!
        # But I left it False just in case you want to see the raw JSON on the screen.
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        
        # ==========================================
        # 🎯 CHALLENGES 1, 2, & 3: Post 1
        # ==========================================
        print("--- Testing Post 1 ---")
        response = page.goto("https://jsonplaceholder.typicode.com/posts/1")
        print("Status:", response.status)
        
        # Turn the response into a Python dictionary
        data = response.json()
        print("User ID:", data["userId"])
        print("Post ID:", data["id"])
        
        assert response.status == 200
        assert data["userId"] == 1
        assert data["id"] == 1
        print("✅ Challenges 1-3 Passed!")
        
        # ==========================================
        # 🎯 CHALLENGE 4: Post 2
        # ==========================================
        print("\n--- Testing Post 2 ---")
        response2 = page.goto("https://jsonplaceholder.typicode.com/posts/2")
        print("Status:", response2.status)
        
        data2 = response2.json()
        print("User ID:", data2["userId"])
        print("Post ID:", data2["id"])
        
        assert response2.status == 200
        assert data2["userId"] == 1  # User 1 wrote the first 10 posts!
        assert data2["id"] == 2
        print("✅ Challenge 4 Passed!")
        
        # ==========================================
        # 🏆 CHALLENGE 5: The Missing Posts (404 Error)
        # ==========================================
        print("\n--- Testing Missing Posts ---")
        
        # Try 9999
        response3 = page.goto("https://jsonplaceholder.typicode.com/posts/9999")
        print("Status for 9999:", response3.status)
        # When a post doesn't exist, the server returns an empty dictionary {}
        # and a 404 status code (which means "Not Found")
        assert response3.status == 404
        print("✅ 9999 returns 404!")
        
        # Try 99999
        response4 = page.goto("https://jsonplaceholder.typicode.com/posts/99999")
        print("Status for 99999:", response4.status)
        assert response4.status == 404
        print("✅ 99999 returns 404!")
        
        print("\n🎉 ALL API CHALLENGES PASSED! 🎉")
        browser.close()
'''

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # --------------------------------
    # Challenge 1-3
    # --------------------------------
    response = page.goto(
        "https://jsonplaceholder.typicode.com/posts/1"
    )
    print("Status:", response.status)
    data = response.json()
    print("User ID:", data["userId"])
    print("Post ID:", data["id"])
    assert response.status == 200
    assert data["userId"] == 1
    assert data["id"] == 1
    print("✅ Challenge 1-3 done!")
    # --------------------------------
    # Challenge 4
    # --------------------------------
    response2 = page.goto(
        "https://jsonplaceholder.typicode.com/posts/2"
    )
    print("Status:", response2.status)
    data2 = response2.json()
    print("User ID:", data2["userId"])
    print("Post ID:", data2["id"])
    assert response2.status == 200
    assert data2["userId"] == 1
    assert data2["id"] == 2
    print("✅ Challenge 4 done!")
    # --------------------------------
    # Challenge 5
    # --------------------------------
    response3 = page.goto(
        "https://jsonplaceholder.typicode.com/posts/9999"
    )
    print("9999 status:", response3.status)
    assert response3.status == 404
    print("✅ Challenge 5 done!")
    print("🎉 All challenges done!")
    browser.close()
