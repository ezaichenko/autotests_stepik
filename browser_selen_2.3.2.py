from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

    # Отправляем заполненную форму
    alert1 = browser.find_element_by_class_name("btn-primary").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    search = browser.find_element_by_id("answer")
    search.send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    check = browser.find_element_by_class_name("btn-primary").click()
    time.sleep(5)
    alert = browser.switch_to.alert
    alert.accept()
    #alert_text = alert.text
    #print(alert_text)
    # assert "Congratulations! You have successfully registered!" == welcome_text
    # "Congrats, you've passed the task! Copy this code as the answer for Stepik quiz" 


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    #time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

