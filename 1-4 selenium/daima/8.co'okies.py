from selenium import webdriver
url="http://www.baidu.com"

driver=webdriver.Chrome()
driver.get(url)

print(driver.get_cookies())

cookies={data['name']:data['value']for data in driver.get_cookies()}

print(cookies)