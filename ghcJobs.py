# -*- coding: utf-8 -*-


# Partner ID:	PID
# Key:	KEY


import urllib, urllib2, sys,csv, os, json
from BeautifulSoup import BeautifulSoup

import urllib2, sys

import time

 

def main():
	with open('CompanyList.csv', mode='r') as infile:
		reader = csv.reader(infile)
		mydict = {rows[0]:rows[1] for rows in reader}

	final = []
	fields = []
	count = 0
	for key in mydict.keys():
		if count > 10:
			time.sleep(5)
			count -= 10
			

		CompanyName = key.strip()
		query_args = {'action':'employers', 'keyword': CompanyName, 'ps':'1'}	
		data = urllib.urlencode(query_args)

		url = "http://api.glassdoor.com/api/api.htm?t.p=PID&t.k=KEY&userip=USER_IP&useragent=Mozilla&format=json&v=1"
		hdr = {'User-Agent': 'Mozilla/5.0'}
		req = urllib2.Request(url,data,headers=hdr)
		try: 
			response = urllib2.urlopen(req)
			response_dict = dict(json.loads(response.read()))['response']
		except:
			print key, sys.exc_info()[0] 
			pass

		print response_dict
		if len(response_dict["employers"]) >0:
			clean_response = response_dict["employers"][0]	

		try:
			clean_response.pop('featuredReview')
		except:
			pass
		try:
			clean_response.pop('squareLogo')
		except:
			pass
		try:
			clean_response.pop('exactMatch')
		except:
			pass
		try:
			clean_response.pop('ceo')
		except:
			pass
		try:
			clean_response.pop('sectorId')
		except:
			pass		
		try:
			clean_response.pop('id')
		except:
			pass		
		try:
			clean_response.pop('industryId')
		except:
			pass
		try:
			clean_response.pop('parentEmployer')
		except:
			pass


		clean_response['boothNum'] = mydict[key]


		final.append(clean_response) 


		
		
		count += 1


	new_final = list()

	for item in final:
		if item not in new_final:
			new_final.append(item)

	final = new_final

	print final
	fields = final[0].keys()
	fieldsRow = {key: key for key in fields}
	with open('FinalCompanyList.csv', 'wb') as csv_file:
		writer = csv.DictWriter(csv_file, fields)
		writer.writerow(fieldsRow)
		for row in final:
			writer.writerow(row)




if __name__ == '__main__':
	main()