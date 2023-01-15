from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json

DRIVER_PATH = '/path/to/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

with open('Credentials.json') as jsonFile:
        data = json.load(jsonFile)

time.sleep(1)

driver.get('https://avenue.cllmcmaster.ca/d2l/le/calendar/6605')

time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/d2l-html-block/div/table/tbody/tr[1]/td/p[2]/span/strong/a').click()
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div/div[1]/ul/li[1]/a').click()
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]').send_keys(data["USERNAME"]+"@mcmaster.ca" + "\n")
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input').send_keys(data["PASSWORD"] + "\n")
time.sleep(2)
twofactor = True
while twofactor: 
    try:
        driver.find_element(By.XPATH,'/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input').click()
        twofactor = False
    except:
        twofactor = True


time.sleep(5)
driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/div[1]/div/ul/li[5]/a').click()
time.sleep(5)
driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[1]/div/div[2]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/a').click()
time.sleep(1)
str_num = driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[1]/div/div[2]/div[3]/div[2]/div[2]/form/div/div/div[1]/span[2]/span').text
date = driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[1]/div/div[2]/div[3]/div[2]/div[2]/form/div/div/ul/li[1]/div[2]/div/div/div[2]/div[1]').text

num = int(str_num)

for i in range(num):
    name = driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[1]/div/div[2]/div[3]/div[2]/div[2]/form/div/div/ul/li['+str(i+1)+']/div[2]/div/div/div[1]/div[2]').text
    date = driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[1]/div/div[2]/div[3]/div[2]/div[2]/form/div/div/ul/li['+str(i+1)+']/div[2]/div/div/div[2]/div[1]').text
    print(name + " | " + date)
time.sleep(2)
driver.quit()

