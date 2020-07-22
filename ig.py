from selenium import webdriver
from time import sleep
options = webdriver.ChromeOptions()
options.add_argument('log-level=3')
options.add_argument("--window-size=100,1080")
driver = webdriver.Chrome(options=options)
url="https://www.instagram.com/accounts/login/"
driver.get(url)
sleep(6)
username_input = '//input[@class="_2hvTZ pexuQ zyHYP"]'
elements = driver.find_element_by_xpath(username_input)
elements.send_keys("your_user_name")
password_input = '//input[@class="_2hvTZ pexuQ zyHYP"]'
driver.find_element_by_xpath(password_input).send_keys("your_password")
login_submit = '//div[@class="                    Igw0E     IwRSH      eGOV_         _4EzTm    bkEs3                          CovQj                  jKUp7          DhRcB                                                    "]'
driver.find_element_by_xpath(login_submit).click()
