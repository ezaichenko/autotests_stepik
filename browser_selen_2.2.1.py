from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
import math


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который берёт цифры и кладёт их в текст
    num1 = browser.find_element_by_css_selector('.nowrap[id="num1"]').text
    num2 = browser.find_element_by_css_selector('.nowrap[id="num2"]').text
    # Считаем и переводим в строку сумму
    final = str(int(num1) + int(num2))
    #print(final)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(final)) # ищем элемент с текстом final
    push = browser.find_element_by_css_selector('button[type="submit"]').click()
    time.sleep(10)
    # ждем загрузки страницы

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

