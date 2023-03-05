from selenium import webdriver

options = webdriver.ChromeOptions() # 创建一个配置对象
options.add_argument('--user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4430.93 Mobile Safari/537.36') # 替换User-Agent

driver = webdriver.Chrome('chromedriver', chrome_options=options)

driver.get('http://www.itcast.cn')
print(driver.title)
driver.quit()
