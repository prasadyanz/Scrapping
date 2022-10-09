import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import openpyxl


s = Service(r'C:\Users\Prasad\Desktop\chromedriver.exe')
driver = webdriver.Chrome(service = s)
codename = "INFY"
path = 'https://www.screener.in/company/' + codename

driver.get(path)


button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//section[@id= 'quarters']//button[@class= 'button-plain']")))

button.click()

# WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
# "//body[@class= 'light flex-column']//main[@class= 'flex-grow container']//section[@id= 'quarters']//button[@class= 'button-plain']//button[@onclick= 'Cmpany.showSchedule('Sales', 'quarters', this)']"))).click()

# elements = driver.find_elements(by = By.LINK_TEXT, value = "Company.showSchedule('Sales', 'quarters', this)")
# for e in elements:
#     e.click()


data = driver.find_elements(by=By.XPATH, value="*")
for x in data:
    print(x.text)

driver.close()