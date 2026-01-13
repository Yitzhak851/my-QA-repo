from tests.pages.login_page import LoginPage
from tests.pages.dashboard_page import DashboardPage

def test_search_found(driver, base_url):
    login = LoginPage(driver)
    dash = DashboardPage(driver)

    login.open(base_url)
    login.login("admin", "1234")
    dash.wait_loaded()

    dash.search("rad")
    assert "radar" in dash.results_text()

def test_search_no_results(driver, base_url):
    login = LoginPage(driver)
    dash = DashboardPage(driver)

    login.open(base_url)
    login.login("admin", "1234")
    dash.wait_loaded()

    dash.search("zzzz")
    assert dash.results_text() == ["No results"]
