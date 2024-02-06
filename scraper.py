#!"C:\Users\Henry\AppData\Local\Microsoft\WindowsApps\python.exe"

import requests
from bs4 import BeautifulSoup
import csv


url = "https://archiveofourown.org/works/43870134?view_adult=true"
re = requests.get(url)
soup = BeautifulSoup(re.content, "html.parser")

################################################################


tags = {"rating": [], "warning" : [], "category" : [], "fandom" : [], "relationship" : [], "character" : [], "freeform" : []}
info = {"published" : "", "words" : "", "chapters" : "", "kudos" : "", "bookmarks" : "", "hits": ""}

#scrape tags from metadata
for tag in tags:
	meta = soup.find("dd", class_ = tag + " tags")
	elements = meta.find_all("li")
	for element in elements:
		tags[tag].append(element.text)

#scrape story data such as word count
meta = soup.find("dd", class_ = "stats")
elements = meta.find_all("dd")
n = 0
for data in info:
	info[data] = elements[n].text
	n += 1

filename = 'test.csv'

header = ["Rating", "Archive Warnings", "Categories", "Fandom", "Relationships", "Characters", "Additional Tags", \
		  "Published", "Words", "Chapters", "Kudos", "Bookmarks", "Hits"]

lst = [len(tags[tag]) for tag in tags]
mx = max(lst)

rows = [[] for x in range(mx)]

for i in range(mx):
	for tag in tags:
		try:
			rows[i].append(tags[tag][i])
		except IndexError:
			rows[i].append("Empty")

for data in info:
	rows[0].append(info[data])


with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(header)
    csvwriter.writerows(rows)
