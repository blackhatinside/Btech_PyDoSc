import re
import requests
from bs4 import BeautifulSoup

a_file = open("cities_utf8.txt", "r", encoding="utf8")
indiancities = [line.strip().lower() for line in a_file]
a_file.close()

GmailRegex = re.compile(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b')
PhoneRegex = r'(\+91|91|0)? ?([7-9]\d{9})'

with open("my_osint_links.txt", encoding="utf8") as fp:
	page_links = fp.readlines() 
	for index, page in enumerate(page_links, 1):
		print("Page no. {}:\n".format(index), page if page[:5] == "https" else "Page no. :NOT HTTPS\n")
		if index != 11:
			continue
		try:
			page_data = requests.get(page)
			page_data = page_data.text
			# print(page_data)	# DEBUG
		except Exception as e:
			print("Failed to read page. Skipping...", e)
			# soup = BeautifulSoup(page_data, 'html.parser')
			# print(soup.prettify())
		outputPhone = re.findall(PhoneRegex, page_data)
		outputPhone = [x[-1] for x in outputPhone]	#ignore country code
		print()	#line break
		print("\tTop 5 Phone Numbers Found:", *outputPhone[:5], sep="\n\t\t")
		outputMails = re.findall(GmailRegex, page_data)
		print("\tTop 5 Email Addresses Found:", outputMails[:5], sep="\n\t\t")
		outputCities = [city for city in indiancities if city in page_data.lower()]
		print("\tTop 5 Indian Cities Found:", outputCities[:5], sep="\n\t\t")

'''
	# eg = "My mail ID is cyberadithya05@gmail.com and my numbers are +91 9234567890, 9234567801 09876543210 and 919182736455."
	# matchGmail = re.findall(GmailRegex, eg)
	# matchPhone = re.findall(PhoneRegex, eg)
	# matchPhone = [x[-1] for x in matchPhone]
	# print("GMail IDs found:", matchGmail)
	# print("Phone Nums found:", matchPhone)
'''