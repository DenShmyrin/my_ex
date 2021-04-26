from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import log, sin
import time

def what(x):
    return log(abs(12*sin(x)))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    browser.find_element_by_id('book').click()

    an = what(int(browser.find_element_by_id("input_value").text))

    browser.find_element_by_id('answer').send_keys(str(an))  # вставляем ответ как строку
    browser.find_element_by_css_selector('[type="submit"]').click()  # клик

finally:
    time.sleep(5)  # ожидание, чтобы визуально оценить результаты прохождения скрипта
    browser.quit()  # закрываем браузер после всех манипуляций
