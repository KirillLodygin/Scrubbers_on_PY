#! python3
# -*- coding: utf8 -*-

import re, os, urllib.request
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.parse import urlparse

allExtLinks = set()
allIntLinks = set()


def getBsObj(siteUrl):
	try:
		opener = urllib.request.build_opener()
		opener.addheaders = [('User-agent', 'Mozilla/5.0')]
		html = opener.open(siteUrl)
	except HTTPError as e:
		print(e)
		return None
	try:
		bsObj = BeautifulSoup(html, "html.parser")
	except AttributeError as e:
		return None
	return bsObj


# getInternalLinks
def getInternalLinks(bsObj, includeUrl):
	includeUrl = urlparse(includeUrl).scheme + "://" + urlparse(includeUrl).netloc
	internalLinks = []
	# Finds all links that begin with a "/"
	for link in bsObj.findAll("a", href=re.compile("^(/|.*" + includeUrl + ")")):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in internalLinks:
				if link.attrs['href'].startswith("/"):
					internalLinks.append(includeUrl + link.attrs['href'])
				else:
					internalLinks.append(link.attrs['href'])
	return internalLinks


# getExternalLinks
def getExternalLinks(bsObj, excludeUrl):
	externalLinks = []
	# Finds all links that start with "http" or "www" that do
	# not contain the current URL
	for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!" + excludeUrl + ").)*$")):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in externalLinks:
				externalLinks.append(link.attrs['href'])
	return externalLinks

# getAllLinks
def getAllLinks(siteUrl):
	bsObj = getBsObj(siteUrl)
	if bsObj is None:
		print("URL is not found")
	else:
		domain = urlparse(siteUrl).scheme + "://" + urlparse(siteUrl).netloc
		internalLinks = getInternalLinks(bsObj, domain)
		externalLinks = getExternalLinks(bsObj, domain)
		
		for link in externalLinks:
			if link not in allExtLinks:
				allExtLinks.add(link)
		
		for link in internalLinks:
			if link not in allIntLinks:
				allIntLinks.add(link)
				getAllLinks(link)


getAllLinks("https://learn.javascript.ru/")

os.chdir(r'C:\Users\Kirilll\PycharmProjects\Scrubbers_on_PY\getAllLinks\links')

with open('links.txt', 'w') as ouf:
	ouf.write('Internal Links (' + str(len(allIntLinks)) + '): ')
	for link in allIntLinks:
		ouf.write('\n' + link)
	
	ouf.write('\n\nExternal Links (' + str(len(allExtLinks)) + '): ')
	if len(allExtLinks) == 0:
		ouf.write('\nNo External Links On Site')
	else:
		for link in allExtLinks:
			ouf.write('\n' + link)

print('Completed!\n')
print('Internal Links - ' + str(len(allIntLinks)) + '\n')
print('External Links - ' + str(len(allExtLinks)))
