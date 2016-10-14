# -*- coding: utf-8 -*-


# Partner ID:	99969
# Key:	dPObtWeMnBw


import urllib, urllib2, sys,csv, os


import urllib2, sys
from BeautifulSoup import BeautifulSoup

 

def main():
	with open('CompanyList.csv', mode='r') as infile:
		reader = csv.reader(infile)
		mydict = {rows[0]:rows[1] for rows in reader}

	# print mydict
	query_args = { 'name': mydict.keys()[0]}	
	data = urllib.urlencode(query_args)
	print data

	url = "http://api.glassdoor.com/api/api.htm?t.p=99969&t.k=dPObtWeMnBw&userip=8.28.178.133&useragent=Mozilla&format=json&v=1&action=employers&"
	hdr = {'User-Agent': 'Mozilla/5.0'}
	req = urllib2.Request(url,data,headers=hdr)
	response = urllib2.urlopen(req)
	soup = BeautifulSoup(response)

	print soup



if __name__ == '__main__':
	main()