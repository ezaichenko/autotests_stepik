from selenium.webdriver.common.by import By
from selenium import webdriver
import time

capabilities = {
    "browserName": "chrome",
    "browserVersion": "92.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
}

driver = webdriver.Remote(command_executor="http://10.10.11.30:4444/wd/hub",desired_capabilities=capabilities)

link = "http://suninjuly.github.io/huge_form.html"

try:
    driver.get(link)
    elements = driver.find_elements_by_css_selector("[type='text']")
    for element in elements:
        element.send_keys("testing")

    button = driver.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(12)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла

