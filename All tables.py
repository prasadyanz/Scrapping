import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl


s = Service(r'C:\Users\Prasad\Desktop\chromedriver.exe')
driver = webdriver.Chrome(service = s)
codename = "INFY"
path = 'https://www.screener.in/company/' + codename

driver.get(path)

# button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(by = By.XPATH, value= "//button[text()='button-plain']"))
# button.click()

data = driver.find_elements(by=By.XPATH, value="*")
for x in data:
    print(x.text)

driver.close()