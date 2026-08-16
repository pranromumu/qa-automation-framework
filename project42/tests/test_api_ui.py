
from pages.post_page import PostPage

def test_get_api_and_ui(api_request, page):
    response = api_request.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data

    api_title = data["title"]
    api_userid = data["userId"]
    print(f"\n Title: {api_title}")
    print(f"\n User Id: {api_userid}")

    page.goto("https://jsonplaceholder.typicode.com/posts/1")
    ui_body = page.locator("body").inner_text()
    print(f"\n Ui-Body: {ui_body}")
    assert api_title in ui_body
    assert str(api_userid) in ui_body
    print("API + UI successfully Dode!")
