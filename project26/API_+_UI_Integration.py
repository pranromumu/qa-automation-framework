'''
from playwright.sync_api import sync_playwright

# We brought back Robin!
def test_api_ui_integration():
    with sync_playwright() as p:
        # ==========================================
        # 🎯 CHALLENGE 1: GET API Request
        # ==========================================
        print("--- Challenge 1: API GET ---")
        request = p.request.new_context()
        response = request.get("https://jsonplaceholder.typicode.com/posts/1")
        api_data = response.json()
        
        print("Status:", response.status)
        assert response.status == 200
        assert api_data["id"] == 1
        print("✅ Challenge 1 Passed! API returned post #1.")
        
        # ==========================================
        # 🎯 CHALLENGE 2: Open in UI & Verify
        # ==========================================
        print("\n--- Challenge 2: UI Verification ---")
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        
        page.goto("https://jsonplaceholder.typicode.com/posts/1")
        ui_text = page.locator("body").inner_text()
        
        # Cross-check: Does the API title appear in the UI text?
        assert api_data["title"] in ui_text
        print("✅ Challenge 2 Passed! UI shows the same title as the API.")
        
        # ==========================================
        # 🎯 CHALLENGE 3: POST API Request (Create Data)
        # ==========================================
        print("\n--- Challenge 3: API POST ---")
        response_post = request.post(
            "https://jsonplaceholder.typicode.com/posts",
            data={
                "title": "My QA Test",
                "body": "Created by API",
                "userId": 10
            }
        )
        created_post = response_post.json()
        
        print("Status:", response_post.status)
        assert response_post.status == 201
        assert created_post["title"] == "My QA Test"
        print("✅ Challenge 3 Passed! API created the new post.")
        
        # ==========================================
        # 🎯 CHALLENGE 4 & 5: Use ID in UI & Verify
        # ==========================================
        print("\n--- Challenge 4 & 5: UI Verification of New Post ---")
        post_id = created_post["id"]
        print("New Post ID:", post_id)
        
        # We use an f-string (f"...") to inject the post_id variable into the URL!
        page.goto(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
        
        new_ui_text = page.locator("body").inner_text()
        print("UI Text:", new_ui_text)
        
        # Cross-check: Does the title we created appear in the UI?
        assert "My QA Test" in new_ui_text
        print("✅ Challenges 4 & 5 Passed! UI shows the newly created post!")
        
        print("\n🎉🎉🎉 ALL INTEGRATION CHALLENGES PASSED! YOU ARE A SENIOR QA ENGINEER! 🎉🎉🎉")
        
        browser.close()
        request.dispose()
'''

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    request = p.request.new_context()
    response = request.get("https://jsonplaceholder.typicode.com/posts/1")
    data= response.json()
    print("Status", response.status)
    assert response.status == 200
    assert data["id"] == 1
    print("Challenge 1 Done!")
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://jsonplaceholder.typicode.com/posts/1")
    text = page.locator("body").inner_text()
    print(text)
    assert ["title"] in text
    print("Challenge 2 Done!")
    respomse1 = request.post(
        "https://jsonplaceholder.typicode.com/posts/",
        data={
            "title": "My QA Test",
            "body": "Created by API",
            "userId": 10
        }
    ) 
    print("Status:",response1.status)
    assert response.status == 201
    assert data["title"] == "My QA Test"
    print("challenge 3 done!")
    # ==========================================
# Challenge 4 — API → UI
# ==========================================

    post_id = data1["id"]
    print("Created Post ID:", post_id)
    post_url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    page.goto(post_url)
    ui_text = page.locator("body").inner_text()
    print("UI Text:")
    print(ui_text)
    assert data1["title"] in ui_text
    print("Challenge 4 Done!")
    # ==========================================
# Challenge 5 — Complete API + UI Test
# ==========================================

    response2 = request.post(
    "https://jsonplaceholder.typicode.com/posts",
    data={
        "title": "Integration Test",
        "body": "Created through API",
        "userId": 10
    }
)
    assert response2.status == 201
    created_data = response2.json()
    print("API Response:", created_data)
    # Get ID from API
    post_id = created_data["id"]
    print("Post ID:", post_id)
    # Build browser URL
    post_url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    print("Opening:", post_url)
    # Open through browser
    page.goto(post_url)
    # Read UI
    ui_text = page.locator("body").inner_text()
    print("UI:")
    print(ui_text)
    # Verify API data appears in UI
    assert created_data["title"] in ui_text
    assert created_data["body"] in ui_text
    print("🎉 Challenge 5 Passed!")
    print("🎉 API + UI Integration Test Passed!")

    browser.close()
    request.dispose()
