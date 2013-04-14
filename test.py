# from bs4 import BeautifulSoup
import Scraper

keyword = 'cybersecurity'
results = Scraper.scrape(keyword)
for k in results:
	for each in k:
		print each + '=' + results[each].strip()
	
	