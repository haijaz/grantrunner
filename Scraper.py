import unicodedata, sys
from bs4 import BeautifulSoup
import mechanize

def scrape(keyword):
	browser = mechanize.Browser()
	browser.open('http://www.grants.gov/search/advanced.do')
	browser.select_form(name='searchForm')
	browser['text'] = keyword
	browser.submit(id = 'submitsearch')
	boss = BeautifulSoup(browser.response().read())
	boss = BeautifulSoup(boss.decode('latin-1','ignore'))
	rows = boss.find("table", border=1, width="100%").find_all("tr")
	for row in rows:
		x=0
		try:
			cells = row.find_all("td")
			fundingNumber = cells[0].text.strip()
			opportunityTitle = cells[1].text.strip()
			Agency = cells[2].text.strip()
			openDate = cells[3].text.strip()
			CloseDate = cells[4].text.strip()
			attachment = cells[5].text.strip()
		except Exception:
			print 'well, here we are'
			sys.exc_clear()
	return rows