#! python3
# -*- coding: utf8 -*-

import requests, bs4

res = requests.get('http://www.pythonscraping.com/pages/page1.html')
try:
	res.raise_for_status()
except Exception as exc:
	print('Возникла проблема: %s' % exc)

if res is None:
	print("URL is not found")
else:
	bsObj = bs4.BeautifulSoup(res.text, "lxml")
	print(bsObj.h1)