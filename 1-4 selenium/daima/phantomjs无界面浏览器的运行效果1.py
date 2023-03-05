from selenium import webdriver
import warnings
#忽略Python使用PhantomJS时提示PhantomJS has been deprecated的警告信息
warnings.filterwarnings("ignore", message=".*PhantomJS has been deprecated.*", category=UserWarning)
# 指定driver的绝对路径
driver = webdriver.PhantomJS(executable_path='phantomjs')
# driver = webdriver.Chrome(executable_path='/home/worker/Desktop/driver/chromedriver')

# 向一个url发起请求
driver.get("http://www.itcast.cn/")

# 把网页保存为图片
driver.save_screenshot("itcast.png")
print(driver.title) # 打印页面的标题
# 退出模拟浏览器
driver.quit() # 一定要退出！不退出会有残留进程！