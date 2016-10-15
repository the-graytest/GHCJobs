# -*- coding: utf-8 -*-


# Partner ID:	99969
# Key:	dPObtWeMnBw


import urllib, urllib2, sys,csv, os, json


import urllib2, sys

import time

 

def main():
	with open('CompanyList.csv', mode='r') as infile:
		reader = csv.reader(infile)
		mydict = {rows[0]:rows[1] for rows in reader}

	final_dict = dict()
	count = 0
	for key in mydict.keys():
		if count > 50:
			print "Sleepy time!, The API has limits and you just found one ;)"
			time.sleep(10)
			count -= 50

		CompanyName = key.strip()
		query_args = {'action':'employers', 'keyword': CompanyName, 'ps':'1'}	
		data = urllib.urlencode(query_args)

		url = "http://api.glassdoor.com/api/api.htm?t.p=99969&t.k=dPObtWeMnBw&userip=129.161.129.75&useragent=Mozilla&format=json&v=1"
		hdr = {'User-Agent': 'Mozilla/5.0'}
		req = urllib2.Request(url,data,headers=hdr)
		response = urllib2.urlopen(req)
		response_dict = dict(json.loads(response.read()))['response']
		response_dict['boothNum'] = mydict[key]

		final_dict[key]= response_dict 
		count += 1

	print response_dict




if __name__ == '__main__':
	main()