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
    link = "http://suninjuly.github.io/registration2.html"
    driver.get(link)

    # Ваш код, который заполняет обязательные поля
    ...

    # Отправляем заполненную форму
    button = driver.find_element_by_css_selector("button.btn")
    button.click()
    input1 = driver.find_element(By.TAG_NAME, "input").send_keys("Ivan")
    input2 = driver.find_element_by_css_selector('.second[required]').send_keys("Petrov")
    input3 = driver.find_element_by_class_name("third").send_keys("testing@mail.ru")
    #input4 = driver.find_element_by_id("country").send_keys("88007777755")
    button = driver.find_element_by_xpath('//button[contains(text(),"Submit")]').click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()

