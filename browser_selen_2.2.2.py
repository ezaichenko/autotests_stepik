from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
import math


try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который берёт цифры и кладёт их в текст
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    search = browser.find_element_by_id("answer")
    search.send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    # Прокрутка
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    chebox = browser.find_element_by_id("robotCheckbox").click()
    radio = browser.find_element_by_css_selector('input[id="robotsRule"]').click()
    push = browser.find_element_by_css_selector('button[type="submit"]').click()
    time.sleep(10)
    # ждем загрузки страницы

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

