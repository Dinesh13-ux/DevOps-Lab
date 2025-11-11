from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("http://127.0.0.1:3000/index.html") 


driver.find_element(By.ID, "name").send_keys("John Doe")
driver.find_element(By.ID, "email").send_keys("john@example.com")
driver.find_element(By.CSS_SELECTOR, "input[value='Drama']").click()


driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()


time.sleep(1)
alert = driver.switch_to.alert
print("Alert Message:",alert.text) 
alert.accept()


time.sleep(1)
driver.quit()
