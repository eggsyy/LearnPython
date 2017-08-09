# coding=utf-8
from selenium import webdriver
import time

browser = webdriver.Chrome()                # 打开浏览器
browser.maximize_window()                   # 浏览器最大化

# first_url = 'http://www.baidu.com'
# browser.get(first_url)
# time.sleep(2)
#
# second_rul = 'http://www.sina.com'
# browser.get(second_rul)
# time.sleep(2)
#
# browser.back()
# time.sleep(1)
#
# browser.forward()
# time.sleep(2)


# url = 'http://www.baidu.com'
# browser.get(url)
# print "now access %s" % url
# print browser.title
# browser.find_element_by_id('kw').send_keys('selenium')
# browser.find_element_by_id('su').click()
# time.sleep(3)
# browser.set_window_size(480, 800)           # 设置浏览器宽、高

browser.get('http://www.baidu.com')
time.sleep(2)
browser.find_element_by_link_text('贴吧').click()
time.sleep(3)

browser.quit()
