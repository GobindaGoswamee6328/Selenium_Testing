import time

from selenium import webdriver
#from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://trytestingthis.netlify.app/")
firstName = driver.find_element(By.ID,"fname")
firstName.send_keys("Gobinda")

lastName = driver.find_element(By.ID, "lname")
lastName.send_keys("Goswamee")
time.sleep(2)


#driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/form/fieldset/button").click()

driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()

time.sleep(2)
