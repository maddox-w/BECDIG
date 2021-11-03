import requests
from bs4 import BeautifulSoup
import ast
from alive_progress import alive_bar
import pandas as pd
import json
import os

def grab_scamalytics_data():

	cwd = os.getcwd()
	with open(f'{cwd}\\becdig_dump\\dict_output.txt') as f:
		data = f.read()

	local_dict = json.loads(data)

	rapid_lookup_data = {}

	key_list=list(local_dict.keys())

	# Scrape data
	print("Grabbing Scamalytics data...for free!")
	x = 0
	with alive_bar(len(key_list)) as bar:
		for key in key_list:
			# Grab current email
			email_name = key_list[x]
			# Grab current IP address
			ip_address = local_dict[email_name]
			scrape_info = []
			page = requests.get(f'https://scamalytics.com/ip/{ip_address}')
			soup = BeautifulSoup(page.text, 'html.parser')
			scraped_page = soup.find_all('td')
			for td in scraped_page:
				scrape_info.append(td.text)
			if scrape_info[14] == "Open":
				rapid_lookup_data[ip_address] = email_name, scrape_info[2], scrape_info[5], scrape_info[21], scrape_info[22], scrape_info[23], scrape_info[24], scrape_info[25], scrape_info[26]
			elif scrape_info[14] == "Closed":
				rapid_lookup_data[ip_address] = email_name, scrape_info[2], scrape_info[5], scrape_info[21], scrape_info[22], scrape_info[23], scrape_info[24], scrape_info[25], scrape_info[26]
			else:
				rapid_lookup_data[ip_address] = email_name, scrape_info[2], scrape_info[5], scrape_info[15], scrape_info[16], scrape_info[17], scrape_info[18], scrape_info[19], scrape_info[20]
			bar()
			x = x + 1

	# Write data
	print("Writing data to file... ")
	df = pd.DataFrame.from_dict(rapid_lookup_data, orient='index', columns=['Email', 'ISP', 'Country', 'Anonymizing VPN', 'Tor Exit Node', 'Server', 'Public Proxy', 'Web Proxy', 'Search Engine Robot'])
	file_name = ('becdig_data.xlsx')
	df.to_excel(file_name)
	print('Done!')


