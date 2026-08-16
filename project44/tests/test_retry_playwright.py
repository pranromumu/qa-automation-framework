

import pytest

# 🎯 CHALLENGE 6: The Flaky Marker!
# We put @pytest.mark.flaky directly on the test. 
# This tells Robin: "If this test fails, retry it 2 times, and wait 1 second between retries."
@pytest.mark.flaky(reruns=2, reruns_delay=1)
def test_google(page):
    page.goto("https://www.google.com")
    assert "Google" in page.title()
    print("\n✅ Google test passed!")
    