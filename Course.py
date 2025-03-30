from logging import exception

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service(r"I:\My Drive\IT SAFE\PT COURSE\Python\chromedriver-win64\chromedriver.exe")
browser = webdriver.Chrome(service=s)
url = 'https://www.google.com'
browser.get(url)
try:
    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Gmail")))
    element.click()
    time.sleep(2)
    element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.label-tracker[data-g-action='create an account']"))
    )
    element.click()

    time.sleep(20)
except Exception as e:
    print("Error in code:\n {0}".format(e))
finally:
    browser.quit()


