from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    context = browser.new_context()

    page = context.new_page()

    page.goto("https://the-internet.herokuapp.com/windows")

    with context.expect_page() as new_page_info:
        page.locator("text=Click Here").click()

    new_page = new_page_info.value

    new_page.wait_for_load_state("domcontentloaded")

    first_title = page.title()
    second_title = new_page.title()

    print("First Page:", first_title)
    print("Second Page:", second_title)

    text = new_page.locator("h3").text_content()

    print(text)

    assert "New Window" in text

    print("✅ Second page verified")

    new_page.close()

    assert page.title() == "The Internet"

    print("✅ Returned to first page")

    browser.close()