import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

def test_validate_equal_text(driver):
    element = driver.find_element_by_id("element_id")
    expect_text = "example"

    assert element.text == expect_text

def test_validate_contains_text(driver):
    element = driver.find_element_by_id("element_id")
    expect_text = "example"

    assert element.text in expect_text

def test_validate_not_equal_text(driver):
    element = driver.find_element_by_id("element_id")
    expect_text = "example"

    assert element.text != expect_text

def test_validate_list_is_not_empty(driver):
    elements = driver.find_elements_by_class_name("element_classes")

    assert len(elements) > 0

def test_validate_element_is_enabled(driver):
    element = driver.find_element_by_id("element_id")

    assert element.is_enabled()

def test_validate_element_is_not_enabled(driver):
    element = driver.find_element_by_id("element_id")
   
    assert not element.is_enabled()

def test_validate_element_is_visible(driver):
    element = driver.find_element_by_id("element_id")
   
    assert element.is_displayed()

def test_validate_element_is_not_visible(driver):
    element = driver.find_element_by_id("element_id")
   
    assert not element.is_displayed()