from selenium import webdriver
import time
url="http://www.baidu.com"

driver=webdriver.Chrome()
driver.get(url)

print(driver.current_url)
print(driver.title)
time.sleep(2)
driver.get("http://www.douban.com")

# print(driver.page_source)
time.sleep(2)
driver.back()

time.sleep(2)
driver.forward()

time.sleep(2)
driver.close()