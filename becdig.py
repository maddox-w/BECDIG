# Required for substring search
import re 
# Required for grabbing eml file names
import os
# Required for running the eml analyzer subprocess
from subprocess import run
# Required for retrieving scamalytics data
import becscan
# Required for writing retrieved IPs to xlsx
import xlsxwriter

def grab_email_ips():
	#Grab from eml_files directory
	print("Grabbing eml files...")
	eml_files = []
	path = 'eml_files'

	# This method of adding files to a list prevents a .DS_STORE unicode read error on Unix systems
	for root, dirs, files in os.walk(path):
		for file in files:
			if file.endswith('.eml'):
				eml_files.append(file)

	#Run eml onsole command, output results in directory parsed_eml

	print("Parsing eml files...")
	#Grab current working directory
	cwd = os.getcwd()
	x = 0
	for file in eml_files:
		#run(["ls"])
		saved_file_name = eml_files[x].replace(" ", "")
		run([f"emlAnalyzer --header -i {cwd}/eml_files/'{eml_files[x]}' > {cwd}/parsed_eml/{saved_file_name}_headers.txt"], shell=True)
		x = x + 1
	print("Done!")

	#Read parsed files into a list

	parsed_eml_files = []
	path = 'parsed_eml'

	# This method of adding files to a list prevents a .DS_STORE unicode read error on Unix systems
	for root, dirs, files in os.walk(path):
		for file in files:
			if file.endswith('.txt'):
				parsed_eml_files.append(file)

	print("Analyzing parsed data...")
	#Read parsed header data files into a string, search for value between "Authentication-Results-Original" and ")" - This location is the first hop.
	ip_list = []
	x = 0
	for files in eml_files:
	
		current_file = f"{cwd}/parsed_eml/{parsed_eml_files[x]}"
	
		with open(f'{current_file}', 'r') as file:
			data = file.read()
			data = re.sub(r"[\n\t\s]*", "", data)

		start = 'Authentication-Results-Original'
		end = 'X-Mimecast-Spam-Score'
		first_hop_field = data[data.find(start)+len(start):data.rfind(end)]

		#Grab first hop ip, located between designated and as permitted sender

		start = 'designates'
		end = 'aspermittedsender'
		first_hop_ip = first_hop_field[first_hop_field.find(start)+len(start):first_hop_field.rfind(end)]

		print(f"File: {parsed_eml_files[x]}, IP:{first_hop_ip}")
		ip_list.append(first_hop_ip)
		x = x + 1
	print("Done!")

	# Write IP list to .xls file
	workbook = xlsxwriter.Workbook(f"{cwd}/ip_list/ips.xlsx")
	worksheet = workbook.add_worksheet()

	row = 0
	column = 0

	for item in ip_list:
		worksheet.write(row, column, item)
		row += 1

	workbook.close()


if __name__ == '__main__':
    grab_email_ips()
    becscan.grab_scamalytics_data()
