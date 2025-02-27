import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.common.exceptions import NoSuchElementException, NoSuchAttributeException
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.webdriver import WebDriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture 
def browser():
  """
  Fxiture that configure a browser
  """
  service = Service(EdgeChromiumDriverManager().install())
  driver = webdriver.Edge(service=service)
  driver.maximize_window()
  driver.get("https://www.freerangetesters.com/")
  yield driver
 

def test_nagitate_to(browser: WebDriver):
    try:
        browser.find_element(
            By.XPATH, "//a[normalize-space()='Cursos' and @href]"
        ).click
    except NoSuchAttributeException:
       assert False, "An error has ocurried"
    except NoSuchElementException:
       assert False, "An error has ocurried"
    

