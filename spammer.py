

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
times=int(input("Kitne Baar karna hai: "))
phone=input("Enter Name or Phone Number: ")
message=input("Enter Message: ")

dpath="/home/akash139/Downloads/chromedriver"
# dpath = "D:/edgedriver_win64/msedgedriver.exe"

driver = webdriver.Chrome(dpath)


driver.get("http://web.whatsapp.com/")

wait = WebDriverWait(driver, 1000)

search_box = wait.until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]')))
search_box.send_keys(phone+Keys.ENTER)

for i in range(times):
    input_box = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')))
    input_box.send_keys(message+Keys.ENTER)

