import lxml.html
import itertools
import requests
import traceback


import threading
import random


# url = 'https://httpbin.org/ip'
url = 'https://ipinfo.io/json'
# DEBUG FROM CMD: curl --proxy https://27.254.52.99:8080 https://httpbin.org/ip
lim = 5
isMultithreaded = True
prevIndex = 0


def get_proxies():
	url = 'https://free-proxy-list.net/'
	response = requests.get(url)
	parser = lxml.html.fromstring(response.text)
	proxies = set()
	for proxy_id in parser.xpath('//tbody/tr')[:100]:
		if proxy_id.xpath('.//td[7][contains(text(),"yes")]'):
			proxy = ":".join([proxy_id.xpath('.//td[1]/text()')[0], proxy_id.xpath('.//td[2]/text()')[0]])
			proxies.add(proxy)
	return list(proxies)	# return list of https proxies


proxies = get_proxies()
print("{} proxies found!\nPROXY LIST: {}".format(len(proxies), proxies))
proxy_pool = itertools.cycle(proxies)


def send_requests(proxy_id):
	global proxies
	global proxy_pool
	global prevIndex
	# proxy = next(proxy_pool)
	# print(threading.current_thread().name + ": " + "Request #%d"%proxy_id, "going from " + proxy)
	
	try:
		proxyindex = random.randint(0, len(proxies) - 1)
		# proxyvalue = proxies[proxyindex]
		proxyvalue = next(proxy_pool)
		newproxy = {"https": "https://" + proxyvalue}
		# print("AAAAA: ", proxyindex, proxyvalue, newproxy, sep="\n")
		if prevIndex != proxy_id:
			print(threading.current_thread().name + ": " + "Request #%d"%proxy_id, "going from " + proxyvalue)
			prevIndex = proxy_id
		response = requests.get(url, proxies=newproxy, timeout=5)	# 5 sec timeout	
		print("\nStatus Code: ", response.status_code)
		print("Client Address: {}\n".format(response.json()['ip']))
		return 200		# success
	except Exception as e:
		# print("BBBBB: Skipping. Connnection error: ", e)
		print("Skipping current proxy...")
		return 404		# failure


# MULTITHREADING	- Problem: Terminal Freezes during execution
def send_requests_odd():
	''' Thread 1 '''
	proxy_id = 1	
	while proxy_id < lim:
		#Get a proxy from the pool
		proxy_id += 2 if send_requests(proxy_id) == 200 else 0
def send_requests_even():
	''' Thread 2 '''
	proxy_id = 2	
	while proxy_id < lim:
		#Get a proxy from the pool
		proxy_id += 2 if send_requests(proxy_id) == 200 else 0


if isMultithreaded:
	t1 = threading.Thread(target=send_requests_odd, name="Thread1", args=())
	t2 = threading.Thread(target=send_requests_even, name="Thread2", args=())
	t1.start()
	t2.start()
	t1.join()
	t2.join()
else:
	index = 0
	while index < lim:
		index += send_requests(index + 1) == 200

# FINISHED
print("\nDone")


'''
http_proxy = "http://" + proxies[proxyindex]
print("\nCURRENT PROXY: ", http_proxy)
sessionproxies = {'http': http_proxy}
session = requests.Session()
session.proxies.update(sessionproxies)
# Here the proxies will also be automatically used
# because we have attached those to the session object, 
# so no need to pass separately in each call
# print("DDDDD")
'''