import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
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
  driver.implicitly_wait(10)
  driver.get("https://thefreerangetester.github.io/sandbox-automation-testing/")
  yield driver
  driver.quit()
 

def test_checkbox(browser: WebDriver):
    try:
       container_checkboxes = browser.find_element(By.CLASS_NAME, "mt-3")
       hamburger_checkbox = container_checkboxes.find_element(By.ID, "checkbox-1")
       
       if not hamburger_checkbox.is_selected:
            hamburger_checkbox.click()

       assert True, hamburger_checkbox.is_selected()

    except NoSuchAttributeException:
       assert False, "An error has ocurried"
    except NoSuchElementException:
       assert False, "An error has ocurried"

def test_hover_button(browser: WebDriver):
    try:
      button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Enviar')]")))

      color_before_hover = button.value_of_css_property("background-color")

      ActionChains(browser).move_to_element(button).perform()
      
      WebDriverWait(browser, 10).until(
        lambda d: button.value_of_css_property("background-color") != color_before_hover
      )

      color_after_hover = button.value_of_css_property("background-color")

      assert color_before_hover != color_after_hover

    except NoSuchAttributeException:
       assert False, "An error has ocurried"
    except NoSuchElementException:
       assert False, "An error has ocurried"