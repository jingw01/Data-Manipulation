import mechanize
import urllib, urllib2, cookielib, re, HTMLParser, sys, time, csv, operator, os

browser=mechanize.Browser()
cj = cookielib.LWPCookieJar()
browser.set_cookiejar(cj)
browser.set_handle_equiv(True)
browser.set_handle_gzip(True)
browser.set_handle_redirect(True)
browser.set_handle_referer(True)
browser.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
# User-Agent (this is cheating, ok?)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36')]
url0 = 'https://link.issgovernance.com/'
browser.open(url0)

browser.select_form(nr=0)
browser.form['userName']='charles'
browser.form['password']='river'
browser.submit()

url1='https://link.issgovernance.com/scas/index.php?c=index&tabName=advancedSearch'
'''
print(browser.open(url1).read())
form.find_control("foo").readonly = False # allow changing .value of control foo 
form.set_all_readonly(False) # allow changing the .value of all controls
#for f in browser.forms():
#    print f
'''

	
	