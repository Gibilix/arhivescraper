#!"C:\Users\Henry\AppData\Local\Microsoft\WindowsApps\python.exe"
import scraper

header = ["Category", "Genre", "Language", "Status", "Published", "Updated", \
"Packaged", "Rating", "Chapters", "Words", "Publisher", "Story URL", "Author URL", "Summary", "FullStory"]
row = ["" for i in range(len(header))]
tags = scraper.tags
genres = scraper.genres

with open("listofURLS.txt", 'r') as URLS:
  for link in URLS.readlines():
    scraper.url = link
    scraper.scrape
    title = scraper.title
    for i in range(len(header)):
    	for tag in tags:
    		if header[i].lower() == tag:
    			if type(tags[tag]) is list:
    				row[i] = " ".join(tags[tag])
    			else:
    				row[i] = tags[tag]
    
    #cleaning up the row elements
    for r in range(len(row)):
    	row[r] = row[r].strip()
    
    row[3] = row[3].replace(":", "")
    row[8] = row[8].split("/")[-1]
    #print(row)
    
    filename = ",".join(tags["category"]) + " - " + tags["author url"].split("/", 4)[4] + " - " + title.strip() + ".csv"
    with open(filename, 'w', newline="") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(header)
        csvwriter.writerow(row)
#first and only row for csv
#creating the row

