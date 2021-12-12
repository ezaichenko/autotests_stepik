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
driver.find_element_by_xpath("//li[3]/a/span").click()
driver.find_element_by_xpath("//a[@id='ldap-master']/span").click()
driver.find_element_by_xpath("(//button[@type='button'])[85]").click()
driver.find_element_by_xpath("//li[@id='tab_phonebook_tab_1-link']/a[2]").click()
driver.find_element_by_id("createSingleRecord_tab_1").click()
driver.find_element_by_xpath("//form[@id='defForm_1']/label").click()
driver.find_element_by_id("name_input_create_1").click()
driver.find_element_by_id("name_input_create_1").clear()
driver.find_element_by_id("name_input_create_1").send_keys(u"Тестовая запись")
Select(driver.find_element_by_id("regionSelect_create_1")).select_by_visible_text(u"Северо-Запад")
driver.find_element_by_id("regionSelect_create_1").click()
Select(driver.find_element_by_id("locationSelect_create_1")).select_by_visible_text(u"Санкт-Петербург")
driver.find_element_by_id("locationSelect_create_1").click()
driver.find_element_by_id("numberInput_create_1").click()
driver.find_element_by_id("numberInput_create_1").clear()
driver.find_element_by_id("numberInput_create_1").send_keys("2222")
Select(driver.find_element_by_id("prioritySelect_create_1")).select_by_visible_text("4")
driver.find_element_by_id("prioritySelect_create_1").click()
Select(driver.find_element_by_id("roleSelect_create_1")).select_by_visible_text(u"Диспетчер")
driver.find_element_by_id("roleSelect_create_1").click()
driver.find_element_by_id("ipInput_create_1").click()
driver.find_element_by_id("ipInput_create_1").clear()
driver.find_element_by_id("ipInput_create_1").send_keys("1.2.3.4:5060")
driver.find_element_by_id("halfDuplex_create_1").click()
driver.find_element_by_id("singleSave_create_1").click()
self.assertEqual(u"Сохранение успешно", self.close_alert_and_get_its_text())

def is_element_present(self, how, what):
    try: self.driver.find_element(by=how, value=what)
    except NoSuchElementException as e: return False
    return True

def is_alert_present(self):
    try: self.driver.switch_to_alert()
    except NoAlertPresentException as e: return False
    return True

def close_alert_and_get_its_text(self):
    try:
        alert = self.driver.switch_to_alert()
        alert_text = alert.text
        if self.accept_next_alert:
            alert.accept()
        else:
            alert.dismiss()
        return alert_text
    finally: self.accept_next_alert = True

def tearDown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
