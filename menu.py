#-*- coding: utf-8 -*-
import time
import menu_db, setup

day_list = ['월요일', '화요일', '수요일', '목요일', '금요일']
db_day = ['mon', 'tue', 'wed', 'thu', 'fri']
bob_list = ['아침', '점심', '저녁']
db_bob = ['b', 'l', 'd']

url = setup.url
cookies = setup.cookies

def now():
	return time.gmtime(time.time()+32400)

def bob_info(day, time):
	result_string = ""
	result_string += "[ "
	result_string += day_list[day]
	result_string += " "
	result_string += bob_list[time]
	result_string += " ]"
	return result_string
	
def timecheck(time):
	if time < 9 :
		return 0
	elif time < 13 :
		return 1
	elif time < 19 :
		return 2
	return 3
	
def get_menu(day, time):
	if day > 4 :
		return '주말출근...?'
	if time is 3 :
		return get_menu(day+1, 0)
	result_string = ""
	result_string += bob_info(day, time)
	result_string += '\n'
	result_string += menu_db.get_bob(day, time).encode('utf-8')
	return result_string
	
def get_day_all_menu(day):
	if day > 4 :
		return '주말출근...?'
	result_string = ""
	result_string += get_menu(day, 0) + '\n'
	result_string += get_menu(day, 1) + '\n'
	result_string += get_menu(day, 2)
	return result_string
	
def get_next_menu():
	return get_menu(now().tm_wday, timecheck(now().tm_hour))

def get_today_a_menu(time):
	return get_menu(now().tm_wday, time)

def get_today_all_menu():
	return get_day_all_menu(now().tm_wday)

def get_tomorrow_a_menu(time):
	return get_menu(now().tm_wday+1, time)
	
def get_tomorrow_all_menu():
	return get_day_all_menu(now().tm_wday+1)

def get_someday_a_menu(day, time):
	return get_menu(day, time)
	
def get_someday_all_menu(day):
	return get_day_all_menu(day)