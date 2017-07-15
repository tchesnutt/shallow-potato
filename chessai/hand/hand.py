from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
from pprint import pprint
with open('../util/login.json') as data_file:
    data = json.load(data_file)

USERNAME = data['username']
PASSWORD = data['password']

chromedriver = "/Users/chesnutt/Documents/chessai/chessai/hand/chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get("http://www.chess.com")
user_ele = driver.find_element_by_id("user_login_username")
pass_ele = driver.find_element_by_id("user_login_password")
login_button = driver.find_element_by_tag_name('button')
print(login_button)
user_ele.send_keys(USERNAME)
pass_ele.send_keys(PASSWORD)
login_button.click()
driver.close()
