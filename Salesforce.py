from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd
 
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://absatt.lightning.force.com/lightning/page/home')
driver.maximize_window()
input()
 
BUIDS = {}
excel_input = pd.read_excel('salesforce_input.xlsx', "Sheet1")
for id in excel_input['Id']:
    try:
        search_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="oneHeader"]/div[2]/div[2]/div/button')))
        search_box.click()
    except Exception as e:
        print(e)
 
    try:
        search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[2]/div/div/div[1]/div/div[1]/lightning-input/div/div/input')))
        search_box.send_keys(id)
        search_box.send_keys(Keys.RETURN)
    except Exception as e:
        print(e)
   
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="brandBand_2"]/div/div/div[2]/div/div[2]/div/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/header/div[2]/h2/a'))).click()
    except Exception:
        try:
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div/div/div[3]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/table/tbody/tr[1]/th/span/a'))).click()
        except Exception as e:
            print(e)
 
    driver.switch_to.new_window('tab')
    driver.get('https://absatt.lightning.force.com/lightning/page/home')
 
print('done')