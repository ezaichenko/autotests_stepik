from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

# говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
    element_text = driver.find_element(By.ID, "price").text
    print(element_text)
    button = WebDriverWait(browser, 12).until(
        EC.element_to_be_clickable((By.ID, "book"))
    )
    button.click()
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    search = browser.find_element_by_id("answer")
    search.send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    check = browser.find_element_by_class_name("btn-primary").click()

    browser.quit()
    
