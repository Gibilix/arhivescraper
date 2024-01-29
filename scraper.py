#!"C:\Users\Henry\AppData\Local\Microsoft\WindowsApps\python.exe"

import requests
from bs4 import BeautifulSoup

url = "https://archiveofourown.org/works/38136640/chapters/95270971"

re = requests.get(url)
soup = BeautifulSoup(re.content, "html.parser")
results = soup.find("div", role="article")
#print(results.prettify())
elements = results.find_all("p")
for element in results:
	print(element.text)
