from selenium import webdriver

options = webdriver.ChromeOptions() # 创建一个配置对象
options.add_argument('--proxy-server=http://124.205.155.150:9090') # 使用代理ip

driver = webdriver.Chrome(chrome_options=options) # 实例化带有配置的driver对象

driver.get('http://www.itcast.cn')
print(driver.title)
driver.quit()
