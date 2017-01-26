#-*- coding: utf-8 -*-
import requests
import setup, menu
import urllib3
import json
from apscheduler.schedulers.blocking import BlockingScheduler

urllib3.disable_warnings()

headers = {
	"Accept": "application/vnd.tosslab.jandi-v2+json",
	"Content-Type": "application/json"
	}


def send_menu():
	data = {
		"body" : menu.get_next_menu()
		}

	r = requests.post(setup.jandi_url, data=json.dumps(data), headers=headers)

	print(r.text)

print setup.lunch_push_time['hour']
	
	
sched_lun = BlockingScheduler()
sched_lun.add_job(send_menu, 'cron', day_of_week='mon-fri', hour=setup.lunch_push_time['hour'], minute=setup.lunch_push_time['min'])
sched_lun.add_job(send_menu, 'cron', day_of_week='mon-fri', hour=setup.dinner_push_time['hour'], minute=setup.dinner_push_time['min'])

sched_lun.start()
