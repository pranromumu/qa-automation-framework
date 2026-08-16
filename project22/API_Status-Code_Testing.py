'''
from playwright.sync_api import sync_playwright

# 🏆 CHALLENGE 5: Create a reusable helper function!
def check_status(request, url, expected_status):
    # 1. Send request
    response = request.get(url)
    
    # 2. Get response status
    actual_status = response.status
    
    # 3. Print actual status
    print(f"Expected: {expected_status} | Actual: {actual_status}")
    
    # 4. Assert expected == actual
    assert actual_status == expected_status
    print(f"✅ Passed!\n")


# We brought back Robin!
def test_http_status_codes():
    with sync_playwright() as p:
        # No browser needed! Pure API speed.
        request = p.request.new_context()
        
        # 🎯 Challenge 1: Test 200 (Success)
        print("--- Challenge 1 ---")
        check_status(
            request,
            "https://httpbin.org/status/200",
            200
        )
        
        # 🎯 Challenge 2: Test 404 (Not Found)
        print("--- Challenge 2 ---")
        check_status(
            request,
            "https://httpbin.org/status/404",
            404
        )
        
        # 🎯 Challenge 3: Test 400 (Bad Request)
        print("--- Challenge 3 ---")
        check_status(
            request,
            "https://httpbin.org/status/400",
            400
        )
        
        # 🎯 Challenge 4: Test 500 (Internal Server Error)
        print("--- Challenge 4 ---")
        check_status(
            request,
            "https://httpbin.org/status/500",
            500
        )
        
        print("🎉 ALL STATUS CODE CHALLENGES PASSED!")
        
        # Clean up
        request.dispose()
'''

from playwright.sync_api import sync_playwright
def check_status(request, url, expected_status):
    response = request.get(url)
    actual_status = response.status
    print(
        f"Expected: {expected_status}, "
        f"Actual: {actual_status}"
    )
    assert actual_status == expected_status
    print("Challenge 5 Done!")
with sync_playwright() as p:
    request = p.request.new_context()
    # Challenge 1
    check_status(
        request,
        "https://httpbin.org/status/200",
        200
    )
    print("Challenge 1 Done!")
    # Challenge 2
    check_status(
        request,
        "https://httpbin.org/status/404",
        404
    )
    print("Challenge 2 Done!")
    # Challenge 3
    check_status(
        request,
        "https://httpbin.org/status/400",
        400
    )
    print("Challenge 3 Done!")
    # Challenge 4
    check_status(
        request,
        "https://httpbin.org/status/500",
        500
    )
    print("Challenge 4 Done!")
    print("🎉 All Challenges Done!")
    request.dispose()