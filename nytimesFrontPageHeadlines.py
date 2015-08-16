#Made by Wilbert Abreu, https://twitter.com/wilbert_abreu
from bs4 import BeautifulSoup
import urllib2
from mailthon import postman, email
import datetime
import os

GMAILUSERNAME = os.environ['GMAILUSERNAME']
GMAILPASSWORD = os.environ['GMAILPASSWORD']
EMAILADDRESSES = os.environ['EMAILADDRESSES']
SENDEREMAIL = os.environ['SENDEREMAIL']

today = datetime.date.today()
print today
def sendMail(message):
	p = postman(host='smtp.gmail.com', auth=(GMAILUSERNAME, GMAILPASSWORD))
	r = p.send(email(
			content='<p><strong>New York Time Front Page</strong></p><p>%s</p>' % (message),
			subject='NY Times Front Page: %s' % (today),
			sender=SENDEREMAIL,
			receivers=[EMAILADDRESSES],
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

		body = ""
		number=1
		for article in articles: 
			body += "%r) " % (number) + str(article) + "<br><br>" 
			number += 1
		return body
		
    except:
        getBuzzfeedQuizInfo()

body = getBuzzfeedQuizInfo()

sendMail(body)
#Made by Wilbert Abreu, https://twitter.com/wilbert_abreu
