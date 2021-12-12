from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)

    # Ваш код, который заполняет обязательные поля
    ...

    # Отправляем заполненную форму
    #button = browser.find_element_by_css_selector("button.btn")
    #button.click()
    input1 = browser.find_element_by_name("firstname").send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname").send_keys("Petrov")
    input3 = browser.find_element_by_name("email").send_keys("testing@mail.ru")
    current_dir = os.path.abspath(os.path.dirname('/home/evgenii/virtarea/'))
    #print(os.path.abspath(os.path.dirname(__file__)))
    #print(os.path.abspath('/home/evgenii/virtarea/'))
    file_path = os.path.join(current_dir, '1test.txt')           # добавляем к этому пути имя файла
    inputfile = browser.find_element_by_id("file")
    inputfile.send_keys(file_path)
    button = browser.find_element_by_xpath('//button[contains(text(),"Submit")]').click()

    
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

