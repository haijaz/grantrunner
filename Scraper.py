import re
# from pprint import pprint
# import unicodedata, sys
# from bs4 import BeautifulSoup
import lxml.html as lh
import mechanize

# def clean(browser):
	# boss = BeautifulSoup(browser.response().read())
	# boss = BeautifulSoup(boss.decode('latin-1','ignore'))
	# rows = boss.find("table", border=1, width="100%").find_all("tr")
	# return rows

	
# this still needs to allow for looping (pass results back and forth from mail scraper module - and reintegrate into first.py (save to database)	
def clean(browser, list):
	print 'hi'
	result = lh.document_fromstring(browser.response().read())
	for bad in result.xpath("//tr/th"):
		bad.getparent().remove(bad)
	new = result.xpath("//table[@border=\"1\"]/tr")

	# print type(new)
	lstResults = list
	for each in new:
		newline = dict()
		# newline = dict(fundingNumber = "",
				# opportunityTitle = "",
				# Agency = "",
				# openDate = "",
				# attachment = "",
				# link = "")
		try:
			newline["fundingNumber"]=each[0].text
			# newline.append(each[1].text)
			links = each[1].iterlinks()
			newline["opportunityTitle"] = each[1].text_content()
			# newline.append(each[1].text_content())
			# print links[0]
			for eachlink in links:
				newline["link"]=eachlink[2]
			# newline.append(each[2].text)
			newline["Agency"] = each[2].text
			newline["openDate"] = each[3].text
			newline["closeDate"] = each[4].text
			# newline.append(each[3].text)
			# newline["closeDate"]=each[3].text
			# newline.append(each[4].text)
			newline["attachment"] = ""
			# links = each[5].iterlinks()
			# for attlink in links:
				# newline["attachment"] = attlink[2]
				# newline.append(attlink[2])
				# newline.append(each[5].text_content())
				# pass
		except Exception:
			pass
		lstResults.append(newline.copy())
	return lstResults



			# f = open('results.html', 'w')
	# f.write(lh.tostring(result, pretty_print=True))
	# f.close
	# for a in result.xpath('.//tr/*/a'):
		# # print a.text
		# print 'asdf'
	# boss = BeautifulSoup(browser.response().read())
	# boss = BeautifulSoup(boss.decode('latin-1','ignore'))
	# rows = boss.find("table", border=1, width="100%").find_all("tr")

	
def scrape(keyword):
	print keyword
	browser = mechanize.Browser()
	browser.open('http://www.grants.gov/search/advanced.do')
	browser.select_form(name='searchForm')
	browser['text'] = keyword
	browser.submit(id = 'submitsearch')
	lstResults = []
	lstResults = clean(browser, lstResults)
	try:
		while browser.find_link(text="Next"):
			req = browser.click_link(text="Next")
			browser.open(req)
			lstResults = clean(browser, lstResults)
	except Exception:
		print 'done'
	return lstResults
	# return rows