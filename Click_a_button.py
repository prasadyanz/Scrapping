from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


s = Service(r'C:\Users\Prasad\Desktop\chromedriver.exe')
driver = webdriver.Chrome(service = s)
driver.get("https://www.bseindia.com/corporates/results.aspx?Code=500209&Company=INFOSYS%20LTD.&qtr=113.50&RType=c")

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='divmain']//a[@id='ContentPlaceHolder1_lnkDetailed']"))).click()


