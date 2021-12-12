from selenium import webdriver
import time
import math


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    search = browser.find_element_by_id("answer")
    search.send_keys(str(math.log(abs(12 * math.sin(int(x)))))) 
    chebox = browser.find_element_by_id("robotCheckbox").click()
    radio = browser.find_element_by_css_selector('input[id="robotsRule"]').click()
    push = browser.find_element_by_css_selector('button[type="submit"]').click()
    time.sleep(10)
    # ждем загрузки страницы
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    #assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

