'''
from playwright.sync_api import sync_playwright

# We brought back Robin!
def test_crud_operations():
    with sync_playwright() as p:
        # No browser needed! Pure speed API testing.
        request = p.request.new_context()
        
        # ==========================================
        # 1️⃣ READ (GET) - Challenge 1
        # ==========================================
        print("--- 1. GET (Read) ---")
        response = request.get("https://jsonplaceholder.typicode.com/posts/5")
        data = response.json()
        
        print("Status:", response.status)
        assert response.status == 200
        assert data["id"] == 5
        print("✅ GET Passed! Read post #5.")
        
        # ==========================================
        # 2️⃣ CREATE (POST) - Challenge 2
        # ==========================================
        print("\n--- 2. POST (Create) ---")
        response = request.post(
            "https://jsonplaceholder.typicode.com/posts",
            data={
                "title": "QA Automation",
                "body": "Playwright API testing",
                "userId": 5
            }
        )
        data = response.json()
        
        print("Status:", response.status)
        assert response.status == 201
        assert data["title"] == "QA Automation"
        assert data["userId"] == 5
        print("✅ POST Passed! Created new post.")
        
        # ==========================================
        # 3️⃣ UPDATE (PUT) - Challenge 3
        # ==========================================
        print("\n--- 3. PUT (Update) ---")
        response = request.put(
            "https://jsonplaceholder.typicode.com/posts/2",
            data={
                "id": 2,
                "title": "Updated Post",
                "body": "Learning PUT",
                "userId": 2
            }
        )
        data = response.json()
        
        print("Status:", response.status)
        assert response.status == 200
        assert data["id"] == 2
        assert data["title"] == "Updated Post"
        print("✅ PUT Passed! Updated post #2.")
        
        # ==========================================
        # 4️⃣ DELETE (DELETE) - Challenge 4
        # ==========================================
        print("\n--- 4. DELETE (Delete) ---")
        response = request.delete("https://jsonplaceholder.typicode.com/posts/3")
        
        print("Status:", response.status)
        assert response.status == 200
        print("✅ DELETE Passed! Deleted post #3.")
        
        print("\n🎉🎉🎉 ALL CRUD CHALLENGES PASSED! YOU ARE AN API MASTER! 🎉🎉🎉")
        
        # Clean up
        request.dispose()
'''

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    request = p.request.new_context()
    # ==========================================
    # Challenge 1 — GET
    # ==========================================
    response = request.get(
        "https://jsonplaceholder.typicode.com/posts/5"
    )
    print("GET Status:", response.status)
    data = response.json()
    assert response.status == 200
    assert data["id"] == 5
    print("✅ Challenge 1 Done!")
    # ==========================================
    # Challenge 2 — POST
    # ==========================================
    response = request.post(
        "https://jsonplaceholder.typicode.com/posts/",
        data={
            "title": "QA Automation",
            "body": "Playwright API testing",
            "userId": 5
        }
    )
    print("POST Status:", response.status)
    data = response.json()
    assert response.status == 201
    assert data["title"] == "QA Automation"
    assert data["userId"] == 5
    print("✅ Challenge 2 Done!")
    # ==========================================
    # Challenge 3 — PUT
    # ==========================================
    response = request.put(
        "https://jsonplaceholder.typicode.com/posts/2",
        data={
            "id": 2,
            "title": "Updated Post",
            "body": "Learning PUT",
            "userId": 2
        }
    )
    print("PUT Status:", response.status)
    data = response.json()
    assert response.status == 200
    assert data["id"] == 2
    assert data["title"] == "Updated Post"
    print("✅ Challenge 3 Done!")
    # ==========================================
    # Challenge 4 — DELETE
    # ==========================================
    response = request.delete(
        "https://jsonplaceholder.typicode.com/posts/3"
    )
    print("DELETE Status:", response.status)
    assert response.status == 200
    print("✅ Challenge 4 Done!")
    request.dispose()
    print("🎉 All HTTP method challenges completed!")