import time
from selenium import webdriver
url = 'https://jn.58.com/'

driver = webdriver.Chrome()
driver.get(url)

el=driver.find_element_by_partial_link_text('租房')

el.click()

print(driver.current_url)
print(driver.window_handles)

driver.switch_to.window(driver.window_handles[-1])

el_list=driver.find_elements_by_xpath('/html/body/div[6]/div[2]/ul/li/div[2]/h2/a')

print(len(el_list))