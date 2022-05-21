# About

BECDIG is used to analyze the first-hop found in .eml files. IP information scraped from Scamalytics is then outputted for the user listing known address functionalities such as VPN/S, proxy, and TOR association.

## Requirements and Installation Procedures:

Please ensure to only utilize the .zip contents of either the BECDIG-WINDOWS or BECDIG-LINUX files for the smoothest experience.

1. Extract BECDIG.zip contents.
2. Ensure the listed modules found in becdig.py, becscan.py, and eml_analyzer are installed.
3. Dump all .eml files into the eml_files directory
4. Run becdig.py inside the BECDIG directory

### Harness the POWER of the Windows Command Prompt to move thousands of .EMLs from one location to another!
![alt text](https://user-images.githubusercontent.com/83250335/151015707-161f202f-4569-4730-b75a-385171bbe115.gif)
```
for /r "[EML SOURCE LOCATION]" %x in (*.eml) do move /y "%x" "[EML DESTINATION LOCATION]\BECDIG\eml_files"
```
