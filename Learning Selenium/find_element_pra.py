from selenium import webdriver
import time
import os

chrome = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('checkbox.html')
chrome.get(file_path)

checkboxes = chrome.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxes:
    checkbox.click()
time.sleep(2)

chrome.find_elements_by_css_selector('input[type=checkbox]').pop().click()
time.sleep(2)

chrome.quit()
