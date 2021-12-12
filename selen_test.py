from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

capabilities = {
    "browserName": "chrome",
    "browserVersion": "95.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
}

driver = webdriver.Remote(command_executor="http://10.10.19.242:4444/wd/hub",desired_capabilities=capabilities)

try:

    link = "https://www.google.com"
    driver.get(link)
    driver.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys("webElement")

# Get attribute of current active element
    attr = driver.switch_to.active_element.get_attribute("title")
    print(attr)

finally:
# закрываем браузер после всех манипуляций
    driver.quit()

