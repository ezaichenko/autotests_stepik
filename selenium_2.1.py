from selenium import webdriver
import time
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
    link = "http://suninjuly.github.io/math.html"
    driver.get(link)

    # Ваш код, который заполняет обязательные поля
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    x_element = driver.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    print(y)
    search = driver.find_element_by_id("answer")
    search.send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    
    chebox = driver.find_element_by_id("robotCheckbox").click()
    radio = driver.find_element_by_css_selector('input[id="robotsRule"]').click()

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)

finally:
    # закрываем браузер после всех манипуляций
    driver.quit()

