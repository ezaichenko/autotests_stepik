from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

    # Отправляем заполненную форму
    troll = browser.find_element_by_css_selector('.trollface[type="submit"]').click()
    # Вызываем весь список вкладок, которые есть
    new_window = browser.window_handles[1]
    # Переходим на вторую вкладку
    browser.switch_to.window(new_window)
    print('new_window')
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    search = browser.find_element_by_id("answer")
    search.send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    check = browser.find_element_by_class_name("btn-primary").click()
    time.sleep(4)
    alert = browser.switch_to.alert
    alert.accept()
    # Вызываем весь список вкладок, которые есть   
    first_window = browser.window_handles[0]
    # Возвращаемся на первую вкладку
    browser.switch_to.window(first_window)
    time.sleep(5)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

