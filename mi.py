#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# @Date    : 2018-09-01 20:21:07
# @Author  : Hume (102734075@qq.com)
# @Link    : https://humecry.wordpress.com/
# @Version : 1.0
# @Description: 参与小米钱包福利专区的抽奖
import os
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep, strftime
# 验证码识别模块
from PIL import Image
import re
from io import BytesIO
import tesserocr
from tesserocr import PyTessBaseAPI

# Mac脚本通知
def notify(title, text):
	os.system(
				"""
					osascript -e 'display notification "{0}" with title "{1}"'
				""".format(text, title)
			  )
# 验证码
def check():
	#获取截图
	driver.get_screenshot_as_file('screenshot.png')

	#获取指定元素位置
	element = driver.find_element_by_id('captcha-img')
	left = int(element.location['x']) + 250
	top = int(element.location['y']) +310
	right = int(element.location['x'] + element.size['width']) + 375
	bottom = int(element.location['y'] + element.size['height']) + 355

	# 通过Image处理图像
	im = Image.open('screenshot.png')
	im = im.crop((left, top, right, bottom))
	im.save('code.png')
# 主要程序
def mi(cookies):
	driver =webdriver.Chrome()
	# 隐性等待，最长等5秒
	driver.implicitly_wait(5)
	driver.set_window_size(400, 1170)
	driver.get('https://s.pay.xiaomi.com')

	for key, value in cookies.items():
		driver.add_cookie({
				'name': key,
				'value': value,
				'domain': '.xiaomi.com'
			})
		# driver.add_cookie({
		# 		'name': key,
		# 		'value': value,
		# 		'domain': 's.pay.xiaomi.com'
		# 	})
		# driver.add_cookie({
		# 		'name': key,
		# 		'value': value,
		# 		'domain': 'm.pay.xiaomi.com'
		# 	})
	driver.get('https://s.pay.xiaomi.com')

	# driver.find_element_by_id("username").send_keys("102734075@qq.com")
	# driver.find_element_by_id("pwd").send_keys("ibelieve5")
	# driver.find_element_by_id("login-button").click()
	while True:
		try:
			button = driver.find_element_by_link_text("立即参与")
		except:
			break
		button.click()
		try:
			sleep(1)
			# 换成招商银行卡支付
			driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)=''])[1]/following::span[4]").click()
		except:
			driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='一分钱拼好运优惠券'])[1]/following::button[1]").click()
			driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)=''])[1]/following::span[4]").click()
			pass
		for i in range(3, 5):
			path = "(.//*[normalize-space(text()) and normalize-space(.)=''])[" + str(i) + "]/following::span[2]"
			a = driver.find_element_by_xpath(path)
			# 中信银行信用卡 尾号8311
			if a.text == '招商银行信用卡 尾号2508':
				a.click()
				break
		# 输入支付密码
		driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)=''])[2]/following::button[1]").click()
		driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)=''])[1]/following::li[4]").click()
		driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)=''])[1]/following::li[8]").click()
		driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)=''])[1]/following::li[6]").click()
		driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)=''])[1]/following::li[2]").click()
		driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)=''])[1]/following::li[7]").click()
		driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)=''])[1]/following::li[9]").click()
		driver.find_element_by_link_text("确定").click()
		driver.find_element_by_link_text("继续参与").click()
		driver.get(driver.current_url)
		sleep(2)
		driver.refresh()
	sleep(2)

	total = len(driver.find_elements_by_class_name("activity-wrap"))
	count = len(driver.find_elements_by_link_text("已参与"))

	driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='拼好运'])[1]/preceding::img[3]").click()

	# 结束后发送通知
	notify('小米抽奖活动', '共有'+ str(total) + '个活动, ' + '其中参与了' + str(count) + '个活动.')
	if total == count:
		os.system('say 已抽完奖, 共参与了' + str(total) + '个活动')
	else:
		os.system('say 还有' + str(total-count) + '个活动未完成')
	sleep(60)
	driver.quit()
	return driver

def main():
	cookies = {
			'cUserId': '8gnaYn9uFthE-7X4JEGWfvaRFas',
			'mipaycommon_serviceToken': 'xTpaEftBBEkPi1kDuh8RzSNrt3ZSfcM5nlQzTv0E5a6kKOu4wJKxevWBs7Mz4iRIcm0zwqm8kfpFbHJ6bTU8ww+LaQGub0gID4u1Y2r9WQaiKywiKPQOhO+a8eDzmTC/Gt/RGOuKSB1J27kiTEa5Z7DEsNQjL3cQ+4dquQ35IwVfaRc00rlHKSblOhn9QTqvfNSd2fAKG7xqyC47cr/GAH9hkHjm1YMMZaf0aP6ND4KrPVqy8jyUAySJqD5pbsf1fJbtTy4dZCuO/5EdnzJSjQ==',
			'mipaycommon_ph': '8/gWtewqU/a9fGNYJ+OKjg==',
			
			'serviceToken': '/3Y2JuOdJ7G5H4fmHjq9sjawBqXPyJYWkD2/PX00fnk9IbtXMLMku5ReuiWSoQ6MtdQwC9zmI+KzF7dMfi5LgnM7+Zfk5317jqVpg8x/VFPEIsub3sxL1jMIuXQS8SJG5Px9SrjRiPhnqahX3lUscdtseONaDovK1RQG+yjnqRSiyQyUusBDi5ghlwxkGmq+nihQFQxmD4nU9q6UBB8H+dBz0Yv9QyByxjdhGmd5JC6jNb6TErbDJ4cbf9p8YZgGz37NTDjRGnvTM9kp82B4Ng==',
			'cashpay-wap_slh': 'SwtN8CYPOFatuodkSDZC1z5I9Tg=',
			'cashpay-wap_ph': 'wYSK9zS4XBpve+KP/NlsyQ==',
		}

	try:
		driver = mi(cookies)
	except:
		sleep(60)
		driver.quit()

if __name__ == '__main__':
	main()