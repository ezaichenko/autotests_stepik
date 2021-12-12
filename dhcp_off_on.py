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

link = "http://10.171.128.10/dhcp"
driver.get(link)
driver.find_element_by_link_text("DHCP").click()
driver.find_element_by_xpath("//a[@id='tester_dhcp_server']/span").click()
driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div").click()
driver.find_element_by_xpath("//form[@id='detail__tab_1']/div/div/input").click()
driver.find_element_by_link_text("tester_dhcp_server").click()
driver.find_element_by_xpath("//li[@id='tab_1-link']/a[2]").click()
driver.find_element_by_id("tab_1-save").click()
driver.alert = browser.switch_to.alert
driver.alert_text = alert.text
driver.alert.accept()
#alert "Сохранение успешно"

#try:
#    driver.find_element(by=how, value=what)
#    except NoSuchElementException as e: return False
#    return True
#    driver.switch_to_alert()
#    except NoAlertPresentException as e: return False
#    return True
driver.quit()
