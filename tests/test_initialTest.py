import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

def test_initialTest():
    driver.maximize_window()
    driver.get("https://www.freerangetesters.com/")
    title = driver.title
    assert title == "Free Range Testers"