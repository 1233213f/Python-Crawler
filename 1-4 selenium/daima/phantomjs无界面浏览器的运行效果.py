from selenium import webdriver

# prepare the option for the chrome driver
options = webdriver.ChromeOptions()
options.add_argument('headless')

# start chrome browser
browser = webdriver.Chrome(chrome_options=options)
browser.get('http://www.itcast.cn/')
print(browser.current_url)

print(browser.title) # 打印页面的标题
# 退出模拟浏览器
browser.quit()# 一定要退出！不退出会有残留进程！



