from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

driver = webdriver.Chrome()
Wait_message = "Looking for chats, contacts or messages..."
not_found_message = "No chats, contacts or messages found"


driver.get('https://web.whatsapp.com/')




phone_num='phonenumber.txt'

file = open(phone_num)
text = file.read().split('\n')
file.close()
file = open('log.txt',"a")
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
file.write('----------------------------------------------------------\n')
file.write('                  %s\n' % (dt_string) )
file.write('----------------------------------------------------------\n')

input('Press any key after scanning QR code')

for name in text:
	if name[:1:]=='#':
		continue

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
			web = "https://web.whatsapp.com/send?phone="+name
			driver.get(web)

		while True:
			try:
				a = driver.find_element_by_xpath('//*[@id="side"]/header/div[1]/div/div/span')
				break
			except:
				time.sleep(1)
	except:
		pass

	time.sleep(2)
	
	try:
		msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
		msg_box.send_keys(Keys.CONTROL, 'v')
		button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')
		button.click()
	except:
		print('%s Not FOUND!!!!!' % (name))
		abc = "%s Not FOUND!!!!!\n" % (name)
		file.write(abc)
		ok_button = driver.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div')
		ok_button.click()

	time.sleep(1)

file.write('----------------------------------------------------------\n')
file.write('                     END OF LOG FILE\n')
file.write('----------------------------------------------------------\n\n\n')
file.close()
a = input("PROGRAM KELAR!!!!Press Enter to continue...")