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

link = "http://10.171.0.10/ldap"
driver.get(link)
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='ГЛАВНАЯ'])[1]/following::span[1]").click()
driver.find_element_by_xpath("//a[@id='ldap-master']/span").click()
driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div/input").click()
driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div[4]/label[2]/input").click()
driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div[5]").click()
driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div[5]/input").click()
driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div[6]/label[2]/input").click()
driver.find_element_by_xpath("//form[@id='detail__tab_1']/div[3]/div[2]/button").click()
assert "Сохранение успешно"

driver.quit()

