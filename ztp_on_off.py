# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

capabilities = {
    "browserName": "chrome",
    "browserVersion": "91.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
}

driver = webdriver.Remote(command_executor="http://10.10.19.242:4444/wd/hub",desired_capabilities=capabilities)

try:
    driver.get("http://10.171.0.10/ztp")
    driver.find_element_by_link_text("ZTP").click()
    driver.find_element_by_xpath("//a[@id='ZTP']/span").click()
    driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div[3]/input").click()
    driver.find_element(By.ID, "select2-region__tab_1-container").click()
    driver.find_element(By.ID, "select2-location__tab_1-container").click()
    driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div/input").click()
    driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div/input").click()
    driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div/input").click()
    driver.find_element_by_xpath("//div[@id='tab_1']/div/div[2]/button").click()
    assert "Сохранение успешно"
    
finally:
    driver.quit()
