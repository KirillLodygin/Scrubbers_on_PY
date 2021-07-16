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


def getAllNames(url):
	res = getSiteHTML(url)
	if res is None:
		return None
	
	try:
		bsObj = bs4.BeautifulSoup(res.text, "html.parser")
		namelist = bsObj.findAll("span", {"class": "green"})
	except Exception as exc:
		return None
	
	return namelist


nameList = getAllNames("http://www.pythonscraping.com/pages/warandpeace.html")
if nameList is None:
	print("Failed to get the list of names")
else:
	for name in nameList:
		print(name.get_text() + '\n')
