

from playwright.sync_api import sync_playwright
with sync_playwright()as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page= context.new_page()
    page.goto("https://the-internet.herokuapp.com/windows")
    with context.expect_page() as new_page_info:
        page.locator("text=Click Here").click()
    new_page = new_page_info.value
    new_page.wait_for_load_state("domcontentloaded")
    print("New page title :",new_page.title())
    text=new_page.locator("h3").text_content()
    print("New page text:", text)
    first_title= page.title()
    print("first title is:",first_title)  # first challenge
    second_title= new_page.title()   # second challenge
    print("seconr page title:",second_title)
    new_page.close()                         # challenge 3 
    print("second tab closed")
    assert "New Window" in text
    print("2nd verified")
    assert page.title() == "The Internet"
    print("return to first page")
    browser.close()