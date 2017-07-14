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
user_ele = driver.find_element_by_name("user_login_username");
pass_ele = driver.find_element_by_name("user_login_password");
login_button = driver.find_element_by_name("c2");
user_ele.sendKeys(USERNAME);
pass_ele.sendKeys(PASSWORD);
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
