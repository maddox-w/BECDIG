# About

BECDIG is used to analyze the first-hop found in .eml files. IP information scraped from Scamalytics is then outputted for the user listing known address functionalities such as VPN/S, proxy, and TOR association.


Note: 
Scraped data from Scamalytics is currently 90-95% accurate. Sometimes, the software likes to pull proxy and other IP data instead of the proper associations. For these addresses, a manual lookup is required (https://scamalytics.com/ip). Also, eml-analyzer currently has an unknown key error when parsing .eml header data, not all files will be captured and this process is currently 98% accurate.

## Requirements and Installation Procedures:

This listed files on this repo represent the Windows version of BECDIG and are only posted for display purposes. Please ensure to only utilize the .zip contents of either the BECDIG-WINDOWS or BECDIG-LINUX files for the smoothest experience.

1. Extract BECDIG.zip contents.
2. Ensure the listed modules found in becdig.py, becscan.py, and eml_analyzer are installed.
3. Dump all .eml files into the eml_files directory
4. Run becdig.py inside the BECDIG directory
5. Best of luck with your forensic investigation!

## Future Updates
1. Additional .EML data
2. Increased accuracy for scraped scamalytics data

### Harness the POWER of the Windows Command Prompt to move thousands of .EMLs from one location to another!
<p align="center">![alt text](https://user-images.githubusercontent.com/83250335/151015707-161f202f-4569-4730-b75a-385171bbe115.gif)</p>
```
for /r "[EML SOURCE LOCATION]" %x in (*.eml) do move /y "%x" "[EML DESTINATION LOCATION]\BECDIG\eml_files"
```
