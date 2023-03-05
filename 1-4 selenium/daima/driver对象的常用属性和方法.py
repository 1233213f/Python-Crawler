# # driver.page_source 当前标签页浏览器渲染之后的网页源代码
# # driver.current_url 当前标签页的url
# # driver.close() 关闭当前标签页，如果只有一个标签页则关闭整个浏览器
# # driver.quit() 关闭浏览器
# # driver.forward() 页面前进
# # driver.back() 页面后退
# # driver.screen_shot(img_name) 页面截图
# find_element_by_id                         (返回一个元素)
# find_element(s)_by_class_name             (根据类名获取元素列表)
# find_element(s)_by_name                 (根据标签的name属性值返回包含标签对象元素的列表)
# find_element(s)_by_xpath                 (返回一个包含元素的列表)
# find_element(s)_by_link_text             (根据连接文本获取元素列表)
# find_element(s)_by_partial_link_text     (根据链接包含的文本获取元素列表)
# find_element(s)_by_tag_name             (根据标签名获取元素列表)
# find_element(s)_by_css_selector         (根据css选择器来获取元素列表)
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://www.itcast.cn/')

ret = driver.find_elements_by_tag_name('h2')
print(ret[0].text) #

ret = driver.find_elements_by_link_text('黑马程序员')
print(ret[0].get_attribute('href'))

driver.quit()