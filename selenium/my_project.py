from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_browser = webdriver.Chrome('./chromedriver.exe')

def select(selector):
    chrome_browser.find_element_by_css_selector(selector)

chrome_browser.maximize_window()
chrome_browser.get('localhost:4200')

username = chrome_browser.find_element_by_css_selector('#username')
username.send_keys('your email')

password = chrome_browser.find_element_by_css_selector('#password')
password.send_keys('password')

login_btn = chrome_browser.find_element_by_css_selector('#login')
login_btn.click()

try:
    element = WebDriverWait(chrome_browser, 100).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'.ui-table-tbody>tr:nth-child(3)>td'))
    )
finally:
    # chrome_browser.quit()
    pass

element.click()