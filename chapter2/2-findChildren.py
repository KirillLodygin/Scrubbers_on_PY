#! python3
# -*- coding: utf8 -*-

import requests, bs4


def getSiteHTML(url):
	res = requests.get(url)
	
	try:
		res.raise_for_status()
		return res
	except Exception as exc:
		print('There was a problem: %s' % exc)
		return None
	

def getParent(url):
	res = getSiteHTML(url)
	if res is None:
		return None
	
	try:
		bsObj = bs4.BeautifulSoup(res.text, "html.parser")
		tab = bsObj.find("table",{"id":"giftList"})
	except Exception as exc:
		return None
	
	return tab


table = getParent("http://www.pythonscraping.com/pages/page3.html")
if table is None:
	print("Failed to get information")
else:
	for child in table.children:
		print(child)