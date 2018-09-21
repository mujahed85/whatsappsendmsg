from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
import pandas as pd

# Replace below path with the absolute path
# to chromedriver in your computer

# friends_lists = []
i=1
# while i<=10:
	# sn='"'+"CA"+str(i)+'"'
	# friends_lists.append(sn)
	# i+=1
# for n in friends_lists:
	# print n

friends_lists = []
csv_file="./MohsinGroups22Sep.csv"
df = pd.read_csv(csv_file)
for name in df.First:
	friends_lists.append(str(name))

# driver = webdriver.Chrome('../chromedriver')
driver = webdriver.Chrome('./chromedriver.exe')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

group_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.RLfQR")))
search = driver.find_elements_by_xpath('//*[@id="side"]/div[2]/div/label/input')[0]
print search
for friend in friends_lists:
	search.clear()
	search.send_keys(friend)
	wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button._3Burg")))
	time.sleep(3)
	persons = driver.find_elements_by_class_name('_2wP_Y')
	print(len(persons))
	for person in persons:
		try:
			if person.text not in ['CHATS','MESSAGES']:
				person_title = person.find_element_by_class_name('_1wjpf')
				print(person_title.get_attribute("title"))
				person_contact = person.find_element_by_class_name('_2EXPL')
				person_contact.click()
				message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
				strMsg="""
				Welcome to CloudAge
				"""
				message.send_keys(strMe)

				sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
				sendbutton.click()
		except:
			print("*")
			continue

driver.close()
