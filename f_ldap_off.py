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
    "browserVersion": "92.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
}

driver = webdriver.Remote(command_executor="http://10.10.11.30:4444/wd/hub",desired_capabilities=capabilities)

link = "http://10.171.0.10/ldap"
driver.get(link)
driver.find_element_by_xpath("//a[@id='ldap-master']/span").click()
driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div[4]/label[2]/input")
driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div[6]/label[2]/input").click()
driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div[4]/input").click()
driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div[4]/input").click()
driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div[6]/input").click()
driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div[6]/input").click()
driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div[6]/input").click()
driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div[7]/input").click()
driver.find_element_by_id("select2-region__tab_1-container").click()
driver.find_element_by_id("select2-location__tab_1-container").click()
driver.find_element_by_xpath("//form[@id='detail__tab_1']/div[3]/div[2]/button").click()
assert "Сохранение успешно"
    
driver.quit()
