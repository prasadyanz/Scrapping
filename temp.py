from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


s = Service(r'C:\Users\Prasad\Desktop\chromedriver.exe')
driver = webdriver.Chrome(service = s)

driver.get("https://www.bseindia.com/corporates/results.aspx?Code=500209&Company=INFOSYS+LTD.&qtr=113.50&RType=c")
elems_site_1 = driver.find_elements(by = By.XPATH, value = "//a[@href]")
for elem_site_1 in elems_site_1:
    print(elem_site_1.get_attribute("href"))