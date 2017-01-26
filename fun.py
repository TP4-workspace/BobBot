#-*- coding: utf-8 -*-
import requests, json
from bs4 import BeautifulSoup


cat_url = "http://thecatapi.com/api/images/get?format=xml"

def nyannyan():
	#get URL of cat image
	res = requests.get(cat_url)
	plain_text = res.text
	soup = BeautifulSoup(plain_text)
	result = soup.find('url').text.encode('utf-8')
	
	# return the URL
	return result