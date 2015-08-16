from twilio.rest import TwilioRestClient
from googlefinance import getQuotes
import json
from bs4 import BeautifulSoup
import urllib2
from mailthon import postman, email
import datetime
#account = "AC0923ef72f2fd871c25f715c5344a40f4"
#token = "facd245d1e569206ea89092aa6e7a7fb"
#client = TwilioRestClient(account, token)
#
#def text(message):
#	client.messages.create(to="+16466719043", from_="+17323938487",
#                                 body=message)
today = datetime.date.today()
print today
def sendMail(message):
	p = postman(host='smtp.gmail.com', auth=('abreu.wilbert@gmail.com', 'vxerdqxjizrigvfh'))
	r = p.send(email(
			content='<p><strong>New York Time Front Page</strong></p><p>%s</p>' % (message),
			subject='NY Times Front Page: %s' % (today),
			sender='Wilbert <abreu.wilbert@gmail.com>',
			receivers=['wabreu511@gmail.com'],
		))
	if r.ok:
		print 'Sent!'

hdr = {'User-Agent':'Mozilla/5.0'}

def getBuzzfeedQuizInfo():
    site = 'http://www.nytimes.com/'
    req = urllib2.Request(site,headers=hdr)
    soup = BeautifulSoup(urllib2.urlopen(req).read())
    try:
		articles = soup.select(".story-heading a")[:10]
#		
#		body = articles[2]
		body = ""
		number=1
		for article in articles: 
			body += "%r) " % (number) + str(article) + "<br><br>" 
			number += 1
		return body
		
    except:
        getBuzzfeedQuizInfo()

body = getBuzzfeedQuizInfo()
#print body 
sendMail(body)
#print message
