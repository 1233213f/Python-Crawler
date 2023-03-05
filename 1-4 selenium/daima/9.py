import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.itcast.cn/")
time.sleep(1)

js = 'window.scrollTo(0,document.body.scrollHeight)' # js语句
driver.execute_script(js) # 执行js的方法

time.sleep(5)
driver.quit()