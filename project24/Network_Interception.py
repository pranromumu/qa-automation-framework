
'''
from playwright.sync_api import sync_playwright

# We brought back Robin!
def test_network_interception():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        
        # 🏆 CHALLENGE 4: Create our counter
        blocked_images = 0
        
        # 🎯 CHALLENGE 3: Create the Interceptor Function!
        def handle_route(route):
            # We need 'nonlocal' so we can change the blocked_images variable from outside!
            nonlocal blocked_images 
            
            # Check if the request is asking for an image
            if route.request.resource_type == "image":
                print("🛑 Blocking image:", route.request.url)
                blocked_images += 1
                route.abort() # Stop it!
            else:
                # Let everything else (HTML, CSS, JavaScript) go through
                route.continue_()
        
        # Tell the page to use our Interceptor for ALL requests ("**/*")
        page.route("**/*", handle_route)
        
        # Go to the Hovers page (which has 3 profile images)
        print("\n--- Loading Page ---")
        page.goto("https://the-internet.herokuapp.com/hovers")
        
        # Print the total count
        print(f"\nTotal images blocked: {blocked_images}")
        
        # 🧪 CHALLENGE 5: Verify normal requests still work
        # Even though we blocked images, the HTML page should still load!
        assert page.title() == "The Internet"
        print("✅ Page title verified! Normal requests still work.")
        
        # Let's also assert that we actually blocked something!
        assert blocked_images > 0
        print(f"✅ Verified we successfully blocked {blocked_images} images!")
        
        browser.close()
'''

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # ==========================================
    # Challenge 1 — Observe Requests
    # ==========================================
    def handle_request(request):
        print(
            "REQUEST:",
            request.method,
            request.url
        )
    page.on("request", handle_request)
    page.goto("https://the-internet.herokuapp.com/")
    print("✅ Challenge 1 Done!")
    # ==========================================
    # Challenge 2 — Observe Responses
    # ==========================================
    def handle_response(response):
        print(
            "RESPONSE:",
            response.status,
            response.url
        )
    page.on("response", handle_response)
    page.goto("https://the-internet.herokuapp.com/")
    print("✅ Challenge 2 Done!")
    # ==========================================
    # Challenge 3 & 4 — Block and Count Images
    # ==========================================
    blocked_images = [0]
    def handle_route(route):
        if route.request.resource_type == "image":
            blocked_images[0] += 1
            print(
                "🚫 Blocking image:",
                route.request.url
            )
            route.abort()
        else:
            route.continue_()
    page.route("**/*", handle_route)
    page.goto(
        "https://the-internet.herokuapp.com/hovers"
    )
    print(
        "Total images blocked:",
        blocked_images[0]
    )
    print("✅ Challenge 3 Done!")
    print("✅ Challenge 4 Done!")
    # ==========================================
    # Challenge 5 — Verify Page
    # ==========================================
    assert page.title() == "The Internet"
    print("✅ Challenge 5 Done!")
    print("🎉 ALL PROJECT 24 CHALLENGES DONE!")
    browser.close()