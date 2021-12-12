from selenium import webdriver
from selenium.webdriver.common.by import By

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
    link = "http://suninjuly.github.io/simple_form_find_task.html"
    driver.get(link)
    driver.find_element(By.ID, "submit_button").click()

finally:
    # закрываем браузер после всех манипуляций
    driver.quit()
