#!/usr/bin/env python3

import urllib.request

def isValidUser(link):
	status_code = urllib.request.urlopen(link).getcode()
	return status_code == 200

def url_to_username(link):
	prefix = "https://www.instagram.com/"
	return link[len(prefix):-1]

try:
	import sys
	import requests
	import re

	from random import randrange

	a_file = open("cities_utf8.txt", "r", encoding="utf8")
	indiancities = [line.strip().lower() for line in a_file]
	a_file.close()

	GmailRegex = re.compile(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b')
	PhoneRegex = r'(\+91|91|0)? ?([7-9]\d{9})'

	try:
		from googlesearch import search
		from bs4 import BeautifulSoup
	except ImportError as err:
		print("Module Error: ", err)

	queries = []

	isInstagram = True

	''' to search using command line args - single search query
	try:
		params = sys.argv[1:]
		for query in params:
			query = '"{}"'.format(query)
			queries.append(query)	
	except Exception as err:
		print("Error 1a: ", err)

	queries = [" ".join(queries)]
	print("\nSearching for...\n", *queries)
	print() #line break
	# '''

	# ''' to search using customized dorks - multiple search queries
	with open("dork_list.txt", "r") as dork_list:
	    queries = [dork.strip() for dork in dork_list]
	# '''

	# print(queries)	# DEBUG

	with open(f"resource_links.txt", "w+", encoding="utf-8") as resource_links:
		page_links = []
		try:
			print("Matching Links:\n")
			for query in queries[:3]:	# change list slicing to pull more dorks
				for link in search(query, tld="co.in", num=5, stop=5, pause=randrange(5, 25)):
					print(link)
					isValidFile = re.findall("\.env$|\.xlsx$|\.xls$|\.docx$|\.doc$", link)
					# print(isValidFile)	# DEBUG
					if isInstagram:
						if isValidUser(link):
							page_links.append(link)
							resource_links.write(url_to_username(link) + "\n")
					else:
						if isValidFile:
							page_links.append(link)
							resource_links.write(link + "\n")

		except Exception as err:
			print("Error 2: ", err)

	if page_links:
		print("\n\tTop Five Links found:\n", *page_links[:5], sep = "\n\t\t")
	else:
		print("\n\tNo Links found, Moving on...\n")

except Exception as err:
	print("Program Crashed Sucessfully: ", err)

'''

	@params - googlesearch.search()
    query : query string that we want to search for.
    tld : tld stands for top level domain which means we want to search our result on google.com or google.in or some other domain.
    lang : lang stands for language.
    num : Number of results we want.
    start : First result to retrieve.
    stop : Last result to retrieve. Use None to keep searching forever.
    pause: Lapse to wait between HTTP requests. Lapse too short may cause Google to block your IP. Keeping significant lapse will make your program slow but its safe and better option.
    Return : Generator (iterator) that yields found URLs. If the stop parameter is None the iterator will loop forever.

'''
