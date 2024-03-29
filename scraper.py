#!"C:\Users\Henry\AppData\Local\Microsoft\WindowsApps\python.exe"

import requests
from bs4 import BeautifulSoup
import csv

header = ["Category", "Genre", "Language", "Status", "Published", "Updated", \
"Packaged", "Rating", "Chapters", "Words", "Publisher", "Story URL", "Author URL", "Summary", "FullStory"]
row = ["" for i in range(len(header))]

genres = ["action", "adventure", "comedy", "crime and mystery", "death game", "fantasy", "historical", "horror", \
"romance", "satire", "science fiction", "cyberpunk and derivatives", "speculative", "thriller", "isekai", "western"]

tags = {"category": [], "genre": [], "language": "", "status" : "", "published" : "", "updated" : "", \
"Packaged" : "", "rating" : [], "chapters" : "", "words" : "", "publisher" : "www.archiveofourown.org", \
"story url" : "", "author url" : "", "summary" : [], "fullstory" : []}

with open("listofURLS.txt", 'r') as URLS:
  for link in URLS:
      url = link
      re = requests.get(url)
      soup = BeautifulSoup(re.content, "html.parser")
      for tag in tags:
          if tag == "language":
              tags[tag] = soup.find("dd", class_ = tag).text
          elif tag == "rating":
              text = soup.find("dd", class_ = tag + " tags").text
              tags[tag] = text
          elif tag == "fullstory":
              results = soup.find("div", role="article")
              #print(results.prettify())
              elements = results.find_all("p")
              for element in results:
                  tags[tag].append(element.text)
          elif tag == "summary":
              results = soup.find("div", class_="summary module")
              elements = results.find_all("p")
              for element in elements:
                  tags[tag].append(element.text)
          elif tag == "author url":
              results = soup.find("a", rel="author").text
              tags[tag] = "https://archiveofourown.org/users/" + results
          elif tag == "status":
              results = soup.find("dd", class_ = "stats")
              elements = results.find_all("dt", class_ = tag)
              for element in elements:
                  tags[tag] = element.text
          elif tag == "updated":
              results = soup.find("dd", class_ = "stats")
              elements = results.find_all("dd", class_ = "status")
              for element in elements:
                  tags[tag] = element.text 
          elif tag == "category":
              results = soup.find("dd", class_ = "fandom tags")
              elements = results.find_all("li")
              for element in elements:
                  tags[tag].append(element.text)
          elif tag == "genre":
              results = soup.find("dd", class_ = "freeform tags")
              elements = results.find_all("li")
              for element in elements:
                  if element.text.lower() in genres:
                      tags[tag].append(element.text)
          elif tag == "package":
              continue;
          elif tag == "story url":
              tags[tag] = url
          else:
              meta = soup.find("dd", class_ = "stats")
              elements = meta.find_all("dd", class_ = tag)
              for element in elements:
                  tags[tag] = element.text
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
    
      title = soup.find("h2", class_ = "title heading").text
    
      filename = title.strip() + ".csv"
      with open(filename, 'w', newline="") as file:
          csvwriter = csv.writer(file)
          csvwriter.writerow(header)
          csvwriter.writerow(row)
        
