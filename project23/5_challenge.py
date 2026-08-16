'''
from playwright.sync_api import sync_playwright

# We brought back Robin!
def test_headers_challenges():
    with sync_playwright() as p:
        request = p.request.new_context()
        
        # ==========================================
        # 🎯 CHALLENGES 1 & 2: Response Headers
        # ==========================================
        print("--- 1 & 2: Inspecting Response Headers ---")
        response = request.get(
            "https://httpbin.org/response-headers?Content-Type=application/json"
        )
        print("Status:", response.status)
        
        # Challenge 1: Verify the content-type
        # Playwright makes header names lowercase so they always match!
        assert "application/json" in response.headers["content-type"]
        print("✅ Challenge 1 Passed: content-type is application/json!")
        
        # Challenge 2: Loop through ALL headers
        print("\nAll Response Headers:")
        for name, value in response.headers.items():
            print(f"  {name} : {value}")
        print("✅ Challenge 2 Passed: Inspected all headers!")
        
        # ==========================================
        # 🎯 CHALLENGES 3 & 4: Request Headers
        # ==========================================
        print("\n--- 3 & 4: Sending Custom Request Headers ---")
        response2 = request.get(
            "https://httpbin.org/headers",
            headers={
                "X-Test-User": "Kabir"  # <--- Our custom ID badge!
            }
        )
        data = response2.json()
        
        # Let's look at exactly how the server saw our headers
        print("Server saw these headers:", data["headers"])
        
        # Challenge 4: Verify our custom header made it to the server!
        # httpbin returns headers exactly as it received them.
        assert data["headers"]["X-Test-User"] == "Kabir"
        print("✅ Challenges 3 & 4 Passed: Server received X-Test-User: Kabir!")
        
        # ==========================================
        # 🎯 CHALLENGE 5: Content-Type + JSON Body
        # ==========================================
        print("\n--- 5: POST with Content-Type Header ---")
        response3 = request.post(
            "https://httpbin.org/post",
            headers={
                "Content-Type": "application/json"
            },
            data='{"name":"Kabir"}'  # <--- We are sending raw JSON text!
        )
        print("Status:", response3.status)
        assert response3.status == 200
        
        data3 = response3.json()
        # httpbin echoes back what we sent. Let's verify the server got the JSON body!
        assert data3["json"]["name"] == "Kabir"
        print("✅ Challenge 5 Passed: Server received the JSON body!")
        
        print("\n🎉 ALL HEADER CHALLENGES PASSED! YOU ARE A NETWORK MASTER! 🎉")
        
        request.dispose()
'''

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    request = p.request.new_context()
    # ==========================================
    # Challenge 1 — Response Header
    # ==========================================
    response = request.get(
        "https://httpbin.org/response-headers?Content-Type=application/json"
    )
    print("Status:", response.status)
    assert "application/json" in response.headers["content-type"]
    print("✅ Challenge 1 Done!")
    # ==========================================
    # Challenge 2 — All Response Headers
    # ==========================================
    for name, value in response.headers.items():
        print(name, ":", value)
    print("✅ Challenge 2 Done!")
    # ==========================================
    # Challenge 3 & 4 — Request Header
    # ==========================================
    response2 = request.get(
        "https://httpbin.org/headers",
        headers={
            "X-Test-User": "Kabir"
        }
    )
    data = response2.json()
    print(data["headers"])
    assert data["headers"]["X-Test-User"] == "Kabir"
    print("✅ Challenge 3 & 4 Done!")
    # ==========================================
    # Challenge 5 — POST + Content-Type
    # ==========================================
    response3 = request.post(
        "https://httpbin.org/post",
        headers={
            "Content-Type": "application/json"
        },
        data='{"name":"Kabir"}'
    )
    print("Status:", response3.status)
    assert response3.status == 200
    data = response3.json()
    assert data["json"]["name"] == "Kabir"
    print("✅ Challenge 5 Done!")
    request.dispose()
    print("🎉 All Project 23 Challenges Done!")
