from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')

# 显式等待
WebDriverWait(driver, 20, 0.5).until(
    EC.presence_of_element_located((By.LINK_TEXT, '好123')))
# 参数20表示最长等待20秒
# 参数0.5表示0.5秒检查一次规定的标签是否存在
# EC.presence_of_element_located((By.LINK_TEXT, '好123')) 表示通过链接文本内容定位标签
# 每0.5秒一次检查，通过链接文本内容定位标签是否存在，如果存在就向下继续执行；如果不存在，直到20秒上限就抛出异常

print(driver.find_element_by_link_text('好123').get_attribute('href'))
driver.quit()