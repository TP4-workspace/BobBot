#-*- coding: utf-8 -*-
import requests, json
from bs4 import BeautifulSoup
import sqlite3
import re
from operator import eq

day_list = ['mon', 'tue', 'wed', 'thu', 'fri']
bob_list = ['b', 'l', 'd']

url = "http://appmobile.ourhome.co.kr/front/menu/weeklyMenuSelectList.do?mi=R030010&busiplcd=FA0NS"
cookies = {'user_id' : 'jHuYo3gvgvj7sY1KNasAVQ=='}


def crawl_week_menu():
	res = requests.get(url,cookies=cookies)
	plain_text = res.text
	soup = BeautifulSoup(plain_text, "html.parser")
	
	flickingwrap = soup.find('div', {'id':'flickingWrap'})
	menu = soup.find('div', {'id':'menu2_c'})
	day_menu = menu.findAll('div', {'class' : 'textShadowBox'})
	
	con = sqlite3.connect("week_menu.db")
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS menu;")
	cur.execute("CREATE TABLE IF NOT EXISTS menu(DAY text, BOB text, MENU text)")
	
	
	day_i = 0
	for day in day_menu:
		bob = day.findAll('span', {'class' : 'fontOrange'})
		
		wday = day.find('div', {'class' : 'menuTitle'}).text
		wday_text_format = re.compile(".*\((.)\)")
		wday_text = wday_text_format.sub("\g<1>", wday)
		
		if eq(wday_text.encode('utf-8'), '월') : 
			day_i = 0
		elif eq(wday_text.encode('utf-8'), '화') : 
			day_i = 1
		elif eq(wday_text.encode('utf-8'), '수') : 
			day_i = 2
		elif eq(wday_text.encode('utf-8'), '목') : 
			day_i = 3
		elif eq(wday_text.encode('utf-8'), '금') : 
			day_i = 4
		
		menu_i = 0
		for menu in bob:
			menu_string = ""
			tmp = bob[menu_i].parent.text
			menu_string += '* '
			menu_string += re.sub(r"[\t\n]", "", tmp)
			menu_string = " ".join(menu_string.split()).encode('utf-8')

			if eq(bob[menu_i].parent.parent.find('th', {'scope' : 'row'}).text.encode('utf-8'),'아침') :
				query = "'" + day_list[day_i] + "', 'b', '" + menu_string + "'"
			elif eq(bob[menu_i].parent.parent.find('th', {'scope' : 'row'}).text.encode('utf-8'),'점심') :
				query = "'" + day_list[day_i] + "', 'l', '" + menu_string + "'"
			else :
				query = "'" + day_list[day_i] + "', 'd', '" + menu_string + "'"
			
			cur.execute("INSERT INTO menu VALUES(" + query + ")")
			menu_i += 1
	
	con.commit()
	con.close()
	print "db update!"
	return

def get_bob(day, time):
	con = sqlite3.connect("week_menu.db")
	cur = con.cursor()
	cur.execute("SELECT MENU FROM menu WHERE DAY='" + day_list[day] + "' AND BOB='" + bob_list[time] + "'")
	result_string = ""
	data = cur.fetchall()
	
	if len(data) is 0 :
		result_string += 'Holiday!!\n'
	else : 
		for row in data:
			result_string += row[0]
			result_string += '\n'
	con.close()

	return result_string
	
