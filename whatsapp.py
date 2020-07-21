from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime


my_phone_number = '+6285779017487'
Wait_message = "Looking for chats, contacts or messages..."
not_found_message = "No chats, contacts or messages found"
phone_num='phonenumber.txt'


def main():
	global my_phone_number,Wait_message,not_found_message,phone_num,file
	driver = webdriver.Chrome()
	driver.get('https://web.whatsapp.com/')
	checkbox = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div/div[3]/label/input')
	checkbox.click()

	file = open(phone_num)
	text = file.read().split('\n')
	file.close()
	file = open('log.txt',"a")
	now = datetime.now()
	dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
	file.write('----------------------------------------------------------\n')
	file.write('                  %s\n' % (dt_string) )
	file.write('----------------------------------------------------------\n')

	input('Press enter after scanning QR code')

	for name in text:
		if name[:1:]=='#':
			continue

		find = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
		namee = '+' + name
		find.send_keys(namee)
		find.send_keys(Keys.RETURN)

		time.sleep(5)
		try:
			not_found = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/span').text
			while(not_found==Wait_message):
				time.sleep(1)
				not_found = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/span').text
		except:
			not_found='masuk else'

		if(not_found==not_found_message):
			find = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
			find.clear()
			find.send_keys(my_phone_number)
			find.send_keys(Keys.RETURN)
			msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
			web = "wa.me/"+name
			msg_box.send_keys(web)
			msg_box.send_keys(Keys.RETURN)
			time.sleep(1)
			href = "//a[@href='http://wa.me/"+name+"']"
			driver.find_element_by_xpath(href).click()
			time.sleep(4)


			try:
				ok_button = driver.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div')
				ok_button.click()
				print('%s Not FOUND!!!!!' % (name))
				abc = "%s Not FOUND!!!!!\n" % (name)
				file.write(abc)
			except:
				msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
				msg_box.send_keys(Keys.CONTROL, 'v')
				button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')
				button.click()

		else:
			msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
			msg_box.send_keys(Keys.CONTROL, 'v')
			button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')
			button.click()			

		
		time.sleep(1)


if __name__ == '__main__':
	global file
	try:
		main()
		file.write('---Program Done---\n')
		file.write('----------------------------------------------------------\n')
		file.write('                     END OF LOG FILE\n')
		file.write('----------------------------------------------------------\n\n\n')
		file.close()
		a = input("PROGRAM KELAR!!!!Press Enter to continue...")
	except:
		file.write('#######################ERROR EXIT#########################\n')
		file.write('----------------------------------------------------------\n')
		file.write('                     END OF LOG FILE\n')
		file.write('----------------------------------------------------------\n\n\n')
		file.close()