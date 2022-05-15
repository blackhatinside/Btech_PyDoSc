import lxml.html
import itertools
import requests
import traceback


import threading
import random


# url = 'https://httpbin.org/ip'
url = 'https://ipinfo.io/json'
# curl --proxy https://27.254.52.99:8080 https://httpbin.org/ip
lim = 100


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


#If you are copy pasting proxy ips, put in the list below
#proxies = ['121.129.127.209:80', '124.41.215.238:45169', '185.93.3.123:8080', '194.182.64.67:3128', '106.0.38.174:8080', '163.172.175.210:3128', '13.92.196.150:8080']


proxies = get_proxies()
print("{} proxies found!\nPROXY LIST: {}".format(len(proxies), proxies))
proxy_pool = itertools.cycle(proxies)


def send_requests(proxy_id):
	global proxies
	global proxy_pool
	# proxy = next(proxy_pool)
	# print(threading.current_thread().name + ": " + "Request #%d"%proxy_id, "going from " + proxy)
	
	try:
		proxyindex = random.randint(0, len(proxies) - 1)
		# proxyvalue = proxies[proxyindex]
		proxyvalue = next(proxy_pool)
		newproxy = {"https": "https://" + proxyvalue}
		# print("AAAAA: ", proxyindex, proxyvalue, newproxy, sep="\n")
		print(threading.current_thread().name + ": " + "Request #%d"%proxy_id, "going from " + proxyvalue)
		response = requests.get(url, proxies=newproxy, timeout=5)	# 5 sec timeout	
		print("\nStatus Code: ", response.status_code)
		print("Client Address: {}\n".format(response.json()['ip']))
	except Exception as e:
		# print("BBBBB: Skipping. Connnection error: ", e)
		print("Skipping current proxy...")


# MULTITHREADING	- Problem: Terminal Freezes during execution
# def send_requests_odd():
# 	''' Thread 1 '''
# 	for proxy_id in range(1, lim, 2):
# 	#Get a proxy from the pool
# 		send_requests(proxy_id)
# def send_requests_even():
# 	''' Thread 2 '''
# 	for proxy_id in range(2, lim, 2):
# 	#Get a proxy from the pool
# 		send_requests(proxy_id)
# t1 = threading.Thread(target=send_requests_odd, name="Thread1", args=())
# t2 = threading.Thread(target=send_requests_even, name="Thread2", args=())
# t1.start()
# t2.start()
# t1.join()
# t2.join()


for i in range(lim):
	send_requests(i + 1)

# FINISHED
print("\nDone")
#Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work. 
#We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url 


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