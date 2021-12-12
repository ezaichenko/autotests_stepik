# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

capabilities = {
    "browserName": "chrome",
    "browserVersion": "92.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
}

driver = webdriver.Remote(command_executor="http://10.10.11.30:4444/wd/hub",desired_capabilities=capabilities)

try:

    link = "http://10.171.0.10/ldap"
    driver.get(link)
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='ZTP'])[1]/following::span[1]").click()
    driver.find_element_by_xpath("//a[@id='FTP']/span").click()
    driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div/input").click()
    driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div[3]/input").click()
    driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div[3]/input").clear()
    driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div[3]/input").send_keys("")
    driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div[3]/input").clear()
    driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div[3]/input").send_keys(u"тестовый ФТП")
    driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div[4]/input").click()
    driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div[4]/input").clear()
    driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div[4]/input").send_keys("27")
    driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div[5]/input").click()
    driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div[5]/input").clear()
    driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div[5]/input").send_keys("500")
    driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div[6]/input").click()
    driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div[6]/input").clear()
    driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div[6]/input").send_keys("12")
    driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/button/b").click()
    driver.find_element_by_id(By.ID, "add-user-modal")
    driver.find_element_by_id("//div[@id='add-user-modal']/div/div/div[2]/form/div/input").clear()
    driver.find_element_by_xpath("//div[@id='add-user-modal']/div/div/div[2]/form/div/input").send_keys("super")
    driver.find_element_by_xpath("//div[@id='add-user-modal']/div/div/div[2]/form/div[2]/input").click()
    driver.find_element_by_xpath("//div[@id='add-user-modal']/div/div/div[2]/form/div[2]/input").clear()
    driver.find_element_by_xpath("//div[@id='add-user-modal']/div/div/div[2]/form/div[2]/input").send_keys("duper")
    driver.find_element_by_xpath("//div[@id='add-user-modal']/div/div/div[3]/button[2]").click()
    self.assertEqual(u"Сохранение успешно", self.close_alert_and_get_its_text())
    driver.find_element_by_xpath("//form[@id='detail__tab_1']/div[2]/div[2]/button").click()
    self.assertEqual(u"Сохранение успешно", self.close_alert_and_get_its_text())

finally:
    driver.quit()
