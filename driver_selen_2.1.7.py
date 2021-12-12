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
    link = "http://suninjuly.github.io/get_attribute.html"
    driver.get(link)

    # Ваш код, который заполняет обязательные поля
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    x_element = driver.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    
    search = driver.find_element_by_id("answer")
    search.send_keys(str(math.log(abs(12 * math.sin(int(x)))))) 
    chebox = driver.find_element_by_id("robotCheckbox").click()
    radio = driver.find_element_by_id("robotsRule").click()
    time.sleep(7)
    # ждем загрузки страницы
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    #assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # закрываем браузер после всех манипуляций
    driver.quit()

