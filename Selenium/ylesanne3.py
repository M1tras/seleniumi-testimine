from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

time.sleep(2)

add_button = driver.find_element(By.TAG_NAME, "button")
add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")

for _ in range(5):
    add_button.click()
    time.sleep(0.5)

delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")

add_button.click()
for button in delete_buttons:
    button.click()
    time.sleep(0.5)

input()
input("Vajuta Enter brauseri sulgemiseks...")

driver.quit()