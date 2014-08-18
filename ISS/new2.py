from selenium import webdriver
from BeautifulSoup import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from pattern import web
from time import sleep
import csv

#to scrape every case of the list of cases of advanced search page
def scrape_perlist(listcase,driver,sleepInt=7):
	for r in range(1,31):
		try:
			row=driver.find_element_by_xpath("//*[@id='dTable_searchResults']/tbody/tr["+str(r)+"]/td[1]/a")
		except:
			pass

		row.click()

		sleep(sleepInt)

		case=scrape_page(browser)
		listcase.append(case)
		
	        back=driver.find_element_by_xpath("//*[@id='backButtons']/span")
		back.click()
		sleep(sleepInt)
	
	return listcase

#scrape data from the page of each case
def scrape_page(driver):
	html=driver.page_source
	soup=BeautifulSoup(html)
	soup2=soup.findAll(id="content")
	title=soup2[0].find('h1').string
	sec=1 if '(SEC)' in title else 0
	varnames=soup2[0].findAll('dt')
	for n in range(len(varnames)):
		if 'Case Status' in varnames[n].string:
			status=varnames[n].findNext('dd').text
		if 'Class Period' in varnames[n].string:
			period=varnames[n].findNext('dd').text
		if 'Settlement Fund' in varnames[n].string:
			settlement=varnames[n].findNext('dd').text
		if 'Class Definition' in varnames[n].string:
			definition=varnames[n].findNext('dd').string
			ipo=1 if 'IPO' or 'Initial Public Offering' in definition else 0
			lp=1 if 'LP' or 'partnership' in definition else 0
			trust=1 if 'Trust' in definition else 0
			adr=1 if 'American Depository' or 'ADR' or 'ADS' in definition else 0
			ma=1 if 'merger' or 'acquisition' or 'M&A' or 'spinoff' in definition else 0
			common=1 if 'common' in definition else 0
		if 'Security ID' in varnames[n].string:
			securityid=varnames[n].findNext('dd').text
		if 'Final Settlement Date' in varnames[n].string:
			finaldate=varnames[n].findNext('dd').text
		if 'Court' in varnames[n].string:
			if 'Appellate' not in varnames[n].string:
				court=varnames[n].findNext('dd').text
		if 'Institutional' in varnames[n].string:
			institutional=varnames[n].findNext('dd').string
			leadInst=1 if len(institutional)>4 else 0
				
		
		if 'Defendants' in varnames[n].string:
			if 'Settling Defendants' not in varnames[n].string:
				defendants=varnames[n].findNext('dd').text
			else:
				settlingdef=varnames[n].findNext('dd').text
		'''
		if 'Case Summary' in varnames[n].string:
			summary=varnames[n].findNext('dd').string
			if 'IPO' or 'Initial Public Offering' in summary:
				ipo=1 
			if 'LP' or 'partnership' in summary:
				lp=1
			if 'Trust' in summary:
				trust=1
			if 'American Depository' or 'ADR' or 'ADS' in summary:
				adr=1
			if 'merger' or 'acquisition' or 'M&A' or 'spinoff' in summary:
				ma=1
			if 'common stock' in summary:
				common=1
		'''
	
	result=casesprofile(title,status,period,settlement,definition,securityid,finaldate,court,institutional,defendants,settlingdef,sec,ipo,lp,trust,ma,common,adr,leadInst)

	return result


#Create Class
class casesprofile:
	def __init__(self,title,status,period,settlement,definition,securityid,finaldate,court,institutional,defendants,settlingdef,sec,ipo,lp,trust,ma,common,adr,leadInst):
		self.title=title
		self.status=status
		self.period=period
		self.settlement=settlement
		self.definition=definition
		self.securityid=securityid
		self.finaldate=finaldate		
		self.court=court
		self.institutional=institutional
		self.defendants=defendants
		self.settlingdef=settlingdef
		self.sec=sec
		self.ipo=ipo
		self.lp=lp
		self.trust=trust
		self.ma=ma
		self.common=common
		self.adr=adr
		self.leadInst=leadInst


browser = webdriver.Firefox()

browser.get('https://link.issgovernance.com/')

elem = browser.find_element_by_name('userName')  # Find the search box
elem.send_keys('charles')

elem2= browser.find_element_by_name('password')  # Find the search box
elem2.send_keys('river')
option=browser.find_element_by_id('login')
option.click()
browser.implicitly_wait(60) # seconds

browser.get('https://link.issgovernance.com/scas/index.php?c=index&tabName=advancedSearch')
browser.implicitly_wait(60) # seconds

start=browser.find_element_by_id('settlementDateStart')
start.send_keys('01/01/2013')
end=browser.find_element_by_id('settlementDateEnd')
end.send_keys('12/31/2013')
submit=browser.find_element_by_id('btnSearch')
submit.click()

cases_null=[]
cases=scrape_perlist(cases_null,browser)

'''
for n in range(1,9)
	nextpage=browser.find_element_by_xpath("//*[@id='dTable_searchResults_paginate']/span/a[2]")
	nextpage.click()
	newcases=scrape_perlist(cases2,browser)
	cases2.append(newcases)
'''

Titles=['Title','Status','Class Period','Settlement Fund','Case Definition','Security Id','FinalSettlementdate','Court','Lead Institutional','Defendants','Settling Defendants','SEC Case','IPO Case','Limited Partnership','Trust','M&A','Common Stock','ADR/ADS','leadInst']


with open('Output.csv', 'wb') as f:
	writer = csv.writer(f)
	writer.writerows([Titles])

	for i in range(len(cases)):
		Data1 = [cases[i].title,cases[i].status,cases[i].period,cases[i].settlement,cases[i].definition,cases[i].securityid,cases[i].finaldate,cases[i].court,cases[i].institutional,cases[i].defendants,cases[i].settlingdef,cases[i].sec,cases[i].ipo,cases[i].lp,cases[i].trust,cases[i].ma,cases[i].common,cases[i].adr,cases[i].leadInst]
		writer.writerows([Data1])
