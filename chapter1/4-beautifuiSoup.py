#! python3
# -*- coding: utf8 -*-

import requests, bs4


def getTitle(url):
	res = requests.get(url)
	
	try:
		res.raise_for_status()
	except Exception as exc:
		print('There was a problem: %s' % exc)
		return None
	
	try:
		bsObj = bs4.BeautifulSoup(res.text)
		title = bsObj.body.h1
	except Exception as exc:
		return None
	
	return title


title = getTitle('http://www.pythonscraping.com/pages/page1.html')

if title is None:
	print('Title could not be found')
else:
	print(title)
