#-*- coding: utf-8 -*-
import fun, menu, menu_db, setup
import telepot
import time

telegram_bot_token = setup.telegram_bot_token

# input string
next_string = ['/next', '/n']
bre_string = ['/dkcla', '/breakfast', '/b']
lun_string = ['/wjatla', '/lunch', '/l']
din_string = ['/wjsur', '/dinner', '/d']
today_string = ['/today', '/dhsmf']
tomorrow_string = ['/tomorrow', '/sodlf']
day_string = ['/1', '/2', '/3', '/4', '/5']
day_bob_string = ['/1b', '/1l', '/1d', '/2b', '/2l', '/2d', '/3b', '/3l', '/3d', '/4b', '/4l', '/4d', '/5b', '/5l', '/5d']
tomorrow_breakfast = ['/nb']
tomorrow_lunch = ['/nl']
tomorrow_dinner = ['/nd']
# once a week
update_string = ['/update', '/u']

# nya ong
cat_string = ['/cat', '/nyan']


err = """[Accepted Message List]
/next | /n : 다음 식사 메뉴
/breakfast | /b | /dkcla : 오늘 아침 메뉴
/lunch | /l | /wjatla : 오늘 점심 메뉴
/dinner | /d | /wjsur : 오늘 저녁 메뉴
/today | /dhsmf : 오늘 전체 메뉴
/tomorrow | /sodlf : 내일 전체 메뉴
/n[b|l|d] : 내일 특정 메뉴 ex) /nb : 내일 아침
/1 | /2 | /3 | /4 | /5 : 월화수목금 각 전체 메뉴
/[1-5][b|l|d] : 특정 요일의 특정 메뉴 ex) /4l : 목요일 점심"""


#bot service start
bot = telepot.Bot(telegram_bot_token)

	
def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	if content_type == 'text':
		# next bob menu
		if msg['text'] in next_string:
			result = menu.get_next_menu()
			bot.sendMessage(chat_id, result)
		
		# today breakfast menu
		elif msg['text'] in bre_string :
			result = menu.get_today_a_menu(0)
			bot.sendMessage(chat_id, result)
			
		# today lunch menu
		elif msg['text'] in lun_string :
			result = menu.get_today_a_menu(1)
			bot.sendMessage(chat_id, result)
		
		# today dinner menu
		elif msg['text'] in din_string :
			result = menu.get_today_a_menu(2)
			bot.sendMessage(chat_id, result)
			
		# today all menu
		elif msg['text'] in today_string :
			result = menu.get_today_all_menu()
			bot.sendMessage(chat_id, result)
		
		# tomorrow breakfast menu
		elif msg['text'] in tomorrow_breakfast :
			result = menu.get_tomorrow_a_menu(0)
			bot.sendMessage(chat_id, result)
			
		# tomorrow lunch menu
		elif msg['text'] in tomorrow_lunch :
			result = menu.get_tomorrow_a_menu(1)
			bot.sendMessage(chat_id, result)
		
		# tomorrow dinner menu
		elif msg['text'] in tomorrow_dinner :
			result = menu.get_tomorrow_a_menu(2)
			bot.sendMessage(chat_id, result)
			
		# tomorrow all menu
		elif msg['text'] in tomorrow_string :
			result = menu.get_tomorrow_all_menu()
			bot.sendMessage(chat_id, result)
			
		# someday all menu
		elif msg['text'] in day_string :
			result = menu.get_someday_all_menu(int(msg['text'][1])-1)
			bot.sendMessage(chat_id, result)
			
		# someday a menu
		elif msg['text'] in day_bob_string :
			time = -1
			if msg['text'][2].encode('utf8') is 'b' :
				time = 0
			elif msg['text'][2].encode('utf8') is 'l' :
				time = 1
			else :
				time = 2
			result = menu.get_someday_a_menu(int(msg['text'][1])-1, time)
			bot.sendMessage(chat_id, result)
			
		# nyaaaaaa-- ong---
		elif msg['text'] in cat_string :
			result = fun.nyannyan()
			bot.sendPhoto(chat_id, fun)
			
		# update db
		elif msg['text'] in update_string :
			result = menu_db.crawl_week_menu()
			bot.sendMessage(chat_id, "done")
			
		# fucker..
		else:
			bot.sendMessage(chat_id, err)


bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
