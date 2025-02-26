import pytest
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(params=["Playwright", "Selenium", "Cypress"])
def search_by_term(request: object):
  """
  Fxiture that manage search terms
  """
  return request.param

def read_search_terms():
  """
  Auxiliar function that read a csv file a extract search terms except the firts row
  """
  with open("testData/data.csv", newline='') as csvfile:
    data = list(csv.reader(csvfile))
  return [row[0] for row in data[1:]]

@pytest.fixture(params=read_search_terms())
def search_by_terms_using_csv(request: object):
  """
  Fxiture that manage search terms from csv file
  """
  return request.param

@pytest.fixture 
def browser():
  """
  Fxiture that configure a browser
  """
  service = Service(EdgeChromiumDriverManager().install())
  driver = webdriver.Edge(service=service)
  driver.get("https://www.google.com")
  yield driver
  driver.quit()

@pytest.mark.regression #tagname
def test_google_search(browser, search_by_term):
  """
  Test that do search by terms and check if exist results
  """
  search_box = browser.find_element("name", "q")
  search_box.send_keys(search_by_term + Keys.ENTER)
  results = browser.find_element("id", "search")

  assert (len(results.find_elements("xpath", ".//div")) > 0), "There search results"