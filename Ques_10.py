from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org")

time.sleep(2)

search_box = driver.find_element(By.ID, "searchInput")
search_box.send_keys("Selenium (software)")

search_box.submit()

time.sleep(3)
print("Page Title:", driver.title)

driver.quit()
