from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
Wait_message = "Looking for chats, contacts or messages..."
not_found_message = "No chats, contacts or messages found"


driver.get('https://web.whatsapp.com/')


input('Enter after scanning QR code')

phone_num='phonenumber.txt'

file = open(phone_num)
text = file.read().split('\n')




for name in text:
	find = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
	namee = '+' + name
	find.send_keys(namee)
	find.send_keys(Keys.RETURN)

	time.sleep(3)
	try:
		not_found = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/span').text
		while(not_found==Wait_message):
			time.sleep(1)
			not_found = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/span').text

		if(not_found==not_found_message):
			web = "https://api.whatsapp.com/send?phone="+name
			driver.get(web)

			time.sleep(1)
			tombol = driver.find_element_by_xpath('//*[@id="action-button"]')
			tombol.click()
			time.sleep(1)
			tombol = driver.find_element_by_xpath('//*[@id="fallback_block"]/div/div/a')
			tombol.click()
			time.sleep(7)
	except:
		pass
	
	msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
	msg_box.send_keys(Keys.CONTROL, 'v')

	time.sleep(1)

	button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')
	button.click()
	
