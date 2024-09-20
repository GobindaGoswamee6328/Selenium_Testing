import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://google.com")

googleSearchBox = driver.find_element(By.ID,"APjFqb")
googleSearchBox.send_keys("Automation")
#driver.find_element(By.NAME,"btnK").submit()

googleSearchBox.send_keys(Keys.RETURN)
time.sleep(2)
