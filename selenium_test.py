from selenium import webdriver
from selenium.webdriver.common.by import By
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

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    driver.get(link)

    input1 = driver.find_element_by_tag_name("input").send_keys("Ivan")
    input2 = driver.find_element_by_name("last_name").send_keys("Petrov")
    input3 = driver.find_element_by_class_name("form-control.city").send_keys("Smolensk")
    input4 = driver.find_element_by_id("country").send_keys("Russia")
    button = driver.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла


