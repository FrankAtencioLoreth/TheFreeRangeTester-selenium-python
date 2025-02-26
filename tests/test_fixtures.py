import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(params=["Playwright", "Selenium", "Cypress"])
def search_by_term(request):
  return request.param

@pytest.fixture
def browser():
  service = Service(EdgeChromiumDriverManager().install())
  driver = webdriver.Edge(service=service)
  driver.get("https://www.google.com")
  yield driver
  driver.quit()

def test_google_search(browser, search_by_term):
  search_box = browser.find_element("name", "q")
  search_box.send_keys(search_by_term + Keys.ENTER)
  results = browser.find_element("id", "search")

  assert (len(results.find_elements("xpath", ".//div")) > 0), "There search results"