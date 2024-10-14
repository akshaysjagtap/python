"""
	pip install requests
	pip install html5lib
	pip install bs4
	
	command: python3 web.py curl
"""

from bs4 import BeautifulSoup
import requests
import sys

URL = "https://security-tracker.debian.org/tracker/source-package/" + sys.argv[1]
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.findAll('table')
td = table[1].find_all('td')
a = td[0].find_all('a')
print("CVE ID: "+a[0].getText())

URL2 = "https://nvd.nist.gov/vuln/detail/" + a[0].getText()
print("nvd.nist url: "+URL2)
response = requests.get(URL2)
soup = BeautifulSoup(response.text, 'html.parser')
p = soup.findAll('p', attrs={'data-testid': 'vuln-description'})
if(len(p) > 0):
	print("CVE Description: "+p[0].getText())
