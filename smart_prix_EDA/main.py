import pandas as pd 
import numpy as np 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 

options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
s = Service("/mnt/d/smart_prix_analysis/smart_prix_EDA/chromedriver")
driver = webdriver.Chrome(options=options,service=s)
driver.maximize_window()
driver.get("https://www.google.com/")

time.sleep(1)

user_input = driver.find_element(by = By.XPATH,value='//*[@id="APjFqb"]')
user_input.send_keys("smartprix")
user_input.send_keys(Keys.ENTER)
time.sleep(3)

link = driver.find_element(by = By.XPATH,value='//*[@id="rso"]/div[1]/div/div/div/table/tbody/tr[2]/td/div/div/div/div/h3/a')
link.click()

time.sleep(2)

link2 = driver.find_element(By.XPATH,value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input')
link2.click()

time.sleep(2)


old_height = driver.execute_script("return document.body.scrollHeight")
print("start_old --",old_height)


while True:

    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)

    new_height = driver.execute_script("return document.body.scrollHeight")
   
    print("new --",new_height)
    print("old",old_height)
    
    
    if new_height == old_height:
        break
    old_height = new_height

 #way to import html file with "write" , encoding = "utf-8" then write it into html file 
html = driver.page_source
with open("smartprix.html","w",encoding="utf-8") as f:
   f.write(html)