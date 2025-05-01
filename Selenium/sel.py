from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--start-maximized")

chrome_driver_path = r"c:\Users\rohit\OneDrive\Desktop\devops\selenium\chromedriver-win64\chromedriver.exe"

driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

try:
    driver.get("https://www.google.com")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("devops practical")

    search_box.send_keys(Keys.RETURN)

    time.sleep(2)
    print("Page Title after search:", driver.title)

finally:
    time.sleep(60)
    driver.quit()
