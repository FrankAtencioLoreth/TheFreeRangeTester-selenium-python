import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

def test_validate_equal_text(driver):
    try:
        element = driver.find_element_by_id("element_id")
        expect_text = "example"

        assert element.text == expect_text
    except NoSuchElementException:
        assert False, "Could not find the element with the supplied locator"
