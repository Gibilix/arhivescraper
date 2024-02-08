#!"C:\Users\Henry\AppData\Local\Microsoft\WindowsApps\python.exe"
import scraper

with open("listofURLS.txt", 'r') as file:
  for line in file.readlines():
    scraper.url = line
