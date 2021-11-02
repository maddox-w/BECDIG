# About

BECDIG is used to analyze the first-hop found in .eml files. IP information scraped from Scamalytics is then outputted for the user listing known address functionalities such as VPN/S, proxy, and TOR association.

Note: Scraped data from Scamalytics is currently 90-95% accurate. Sometimes, the software likes to pull proxy and other IP data instead of the proper associations. For these addresses, a manual lookup is required. (https://scamalytics.com/ip)

# Requirements and Installation Procedures:

This listed files on this repo represent the Windows version of BECDIG and are only posted for display purposes. Please ensure to only utilize the .zip contents of either the BECDIG-WINDOWS or BECDIG-LINUX files for the smoothest experience.

1. Extract BECDIG.zip contents.
2. Install eml analyzer on your system (pip install eml-analyzer) [UNIX/LINUX ONLY!]
3. Ensure the listed modules found in becdig.py, becscan.py, and eml_analyzer are installed.
4. Dump all .eml files into the eml_files directory
5. Run becdig.py inside the BECDIG directory
6. Best of luck with your forensic investigation!

# Future Updates
1. Additional .EML data
2. Increased accuracy for scraped scamalytics data

#Harness the POWER of the Windows Command Prompt to move thousands of .EMLs from one location to another!
for /r "[EML LOCATION]" %x in (*.eml) do move /y "%x" "[X]\BECDIG\eml_files"
