from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver.exe')

chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title

show_message_button = chrome_browser.find_element_by_class_name('btn-default')
print(show_message_button.get_attribute('innerHTML'))
print(show_message_button.text)

assert 'Show Message' in show_message_button.text

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
input_text = 'Hi This is Pranav'
user_message.send_keys(input_text)

show_message_button.click()

display_message = chrome_browser.find_element_by_css_selector('#display')

assert input_text in display_message.text

chrome_browser.quit()
# chrome_browser.close()