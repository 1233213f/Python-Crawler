from selenium import webdriver
url="http://www.baidu.com"
driver=webdriver.Chrome()
driver.get(url)

# driver.find_element_by_xpath('//*[@id="kw"]').send_keys("python3")
# driver.find_element_by_css_selector('#kw').send_keys("python3")
# driver.find_element_by_name('wd').send_keys("python3")

driver.find_element_by_class_name('s_ipt').send_keys("pyhton3")

driver.find_element_by_id('su').click()

# driver.find_element_by_class_name('class="s-tab-item s-tab-video').click()
# driver.find_element_by_link_text()('').click()

driver.find_element_by_partial_link_text("视").click()

# driver.find_element_by_css_selector('#s_tab > div > a.s-tab-item.s-tab-pic').click()
# driver.find_element_by_id('wrapper_wrapper').click()

