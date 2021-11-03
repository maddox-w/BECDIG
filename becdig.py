# Required for substring search
import re 
# Required for grabbing eml file names
import os
# Required for running the eml analyzer subprocess
import subprocess
# Required for retrieving scamalytics data
import becscan
# Required for writing retrieved IPs to xlsx
import xlsxwriter
# Required for validating .eml first hop
import ipaddress
# Required for tracking eml parsing
from alive_progress import alive_bar

#Tracks .eml files unable to be loaded with eml-analyzer
unloaded_files = []

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
	print("Done!")
	print("Parsing eml files...")
	#Grab current working directory
	cwd = os.getcwd()
	x = 0
	with alive_bar(len(eml_files)) as bar:
		for file in eml_files:
			#run(["ls"])
			saved_file_name = eml_files[x].replace(" ", "")
			#print(f"python3 cli_script.py --header -i \"{cwd}\\eml_files\\{eml_files[x]}\" > \"{cwd}\\parsed_eml\\{saved_file_name}_headers.txt\"")
			#run([f"python3 cli_script.py --header -i \"{cwd}\\eml_files\\{eml_files[x]}\" > \"{cwd}\\parsed_eml\\{saved_file_name}_headers.txt\""], shell=True)
			try:
				subprocess.run(f'python eml_analyzer.py --header -i \"{cwd}\\{path}\\{eml_files[x]}\" > \"{cwd}\\parsed_eml\\{saved_file_name}_headers.txt\"',stderr=subprocess.DEVNULL, shell=True)
			#os.system(f"python eml_analyzer.py --header -i \"{cwd}\\{path}\\{eml_files[x]}\" > \"{cwd}\\parsed_eml\\{saved_file_name}_headers.txt\"")
			except:
				unloaded_files.append(saved_file_name)
			bar()
			x = x + 1
		print("Done!")
		print("Writing unsuccessful .eml loads...")
		error_file = open("errors.txt", "w")
		for error in unloaded_files:
			error_file.write(error + "\n")
			error_file.close()
		print("Done!")
	#Read parsed files into a list

	parsed_eml_files = []
	path = 'parsed_eml'

	# This method of adding files to a list prevents a .DS_STORE unicode read error on Unix systems
	for root, dirs, files in os.walk(path):
		for file in files:
			if file.endswith('.txt'):
				parsed_eml_files.append(file)

	print("Reading parsed data, please wait...")
	#Read parsed header data files into a string, search for value between "Authentication-Results-Original" and ")" - This location is the first hop.
	ip_list = []
	x = 0
	for files in eml_files:
	
		current_file = (f"{cwd}\\parsed_eml\\{parsed_eml_files[x]}")
	
		with open(f'{current_file}', 'r') as file:
			data = file.read()
			data = re.sub(r"[\n\t\s]*", "", data)

		start = 'Authentication-Results-Original'
		end = 'X-Mimecast-Spam-Score'
		first_hop_field = data[data.find(start)+len(start):data.rfind(end)]
		#print(f"{x}: {first_hop_field}")
		#Grab first hop ip, located between designated and as permitted sender

		start = 'designates'
		end = 'aspermittedsender'
		first_hop_ip = first_hop_field[first_hop_field.find(start)+len(start):first_hop_field.rfind(end)]
		
		#Test if IP was found...
		try:
			network = ipaddress.IPv4Network(first_hop_ip)
			ip_list.append(first_hop_ip)
			#print(first_hop_ip)
		except ValueError:
			#invalid IP
			pass
		#print(f"File: {parsed_eml_files[x]}, IP:{first_hop_ip}")
		x = x + 1
	print(f"Done! {x} addresses found.")

	# Write IP list to .xls file
	workbook = xlsxwriter.Workbook(f"{cwd}\\ip_list\\ips.xlsx")
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
