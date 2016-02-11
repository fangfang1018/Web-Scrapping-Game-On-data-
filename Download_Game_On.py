__author__ = 'ffpku_000'

import urllib

testfile = urllib.URLopener()
testfile.retrieve("http://www.google.com", "testfile")

###
from lxml import etree
import urllib

web = urllib.urlopen("http://www.ffiec.gov/census/report.aspx?year=2011&state=01&report=demographic&msa=11500")
s = web.read()

html = etree.HTML(s)
# result = etree.tostring(html, pretty_print=True, method="html")

## Get all 'tr'
tr_nodes = html.xpath('//table[@id="Report1_dgReportDemographic"]/tr')
tr_nodes = html.xpath('//table[@border="1"]/tr')

## 'th' is inside first 'tr'
header = [i[0].text for i in tr_nodes[0].xpath("th")]
print header

## Get text from rest all 'tr'
td_content = [[td.text for td in tr.xpath('td')] for tr in tr_nodes[1:]]


###
from lxml import etree
import urllib

web = urllib.urlopen("http://espn.go.com/nba/team/stats/_/name/bos/boston-celtics")
s = web.read()

html = etree.HTML(s)

## Get all 'tr'
tr_nodes = html.xpath('//table[@class="tablehead"]/tr')

# tr_nodes[1].xpath("td")[2].xpath("string()")
# tr_nodes[1].xpath("td")[2].xpath("//text()")

## 'th' is inside first 'tr'
header = [i.xpath("string()") for i in tr_nodes[1].xpath("td")]
print header

## Get text from rest all 'tr'
td_content = [[td.text for td in tr.xpath('td')] for tr in tr_nodes[1:]]

### Scraping GWAS Table from Webpage
from lxml import etree
import urllib

web = urllib.urlopen("file:///C:/Users/ffpku_000/Downloads/Welcome%20to%20GAME-ON.html")
s = web.read()
html = etree.HTML(s)

## Get all 'tr'
tbody = html.xpath('//*[@id="l_edu_dfci_cccb_gameon_domain_Snp"]/tbody/tr')
data = [[td.text for td in tr] for tr in tbody]

###
web = urllib.urlopen("http://gameon.dfci.harvard.edu/gameon")
# web = urllib.urlopen("http://gameon.dfci.harvard.edu/gameon/snps?find=ajax&amp;build=&amp;strand=&amp;NStudy=&amp;effectAllele=&amp;refAllele=")
s = web.read()
html = etree.HTML(s)
# print etree.tostring(html, pretty_print=True)
if "Sign with Google" in etree.tostring(html):
    print "sign in needed"
    web = urllib.urlopen("https://accounts.google.com/ServiceLogin?passive=1209600&continue=https://accounts.google.com/o/oauth2/v2/auth?scope%3Demail%26response_type%3Dcode%26redirect_uri%3Dhttp://gameon.dfci.harvard.edu/gameon/openid_connect_login%26state%3D1e4767e4da0a4%26nonce%3D5a09bf5dd590%26client_id%3D502103739642-65lmisq7sgpflbpcam61rui5h0kl389t.apps.googleusercontent.com%26hl%3Den-US%26from_login%3D1%26as%3D76cb9819e803393a&ltmpl=popup&oauth=1&sarp=1&scc=1")
    s = web.read()
    html = etree.HTML(s)
    if "Sign in with your Google Account" in etree.tostring(html):
        print "Sign in with your Google Account"



    login_form = driver.find_element_by_id('loginForm')


https://accounts.google.com/ServiceLogin?passive=1209600&continue=https://accounts.google.com/o/oauth2/v2/auth?scope%3Demail%26response_type%3Dcode%26redirect_uri%3Dhttp://gameon.dfci.harvard.edu/gameon/openid_connect_login%26state%3D1e4767e4da0a4%26nonce%3D5a09bf5dd590%26client_id%3D502103739642-65lmisq7sgpflbpcam61rui5h0kl389t.apps.googleusercontent.com%26hl%3Den-US%26from_login%3D1%26as%3D76cb9819e803393a&ltmpl=popup&oauth=1&sarp=1&scc=1
https://accounts.google.com/AccountChooser?continue=https%3A%2F%2Faccounts.google.com%2Fo%2Foauth2%2Fv2%2Fauth%3Fscope%3Demail%26response_type%3Dcode%26redirect_uri%3Dhttp%3A%2F%2Fgameon.dfci.harvard.edu%2Fgameon%2Fopenid_connect_login%26state%3D238b51ad4a22d%26nonce%3De03b6af720b8%26client_id%3D502103739642-65lmisq7sgpflbpcam61rui5h0kl389t.apps.googleusercontent.com%26hl%3Den%26from_login%3D1%26as%3D-54300b44e6c9ec3a&btmpl=authsub&hl=en

######
import urllib, urllib2, cookielib

username = 'fangf1018@gmail.com'
password = 'fff11950'

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
login_data = urllib.urlencode({'Email' : username, 'Passwd' : password})
opener.open('https://accounts.google.com/ServiceLogin?passive=1209600&continue=https://accounts.google.com/o/oauth2/v2/auth?scope%3Demail%26response_type%3Dcode%26redirect_uri%3Dhttp://gameon.dfci.harvard.edu/gameon/openid_connect_login%26state%3D1e4767e4da0a4%26nonce%3D5a09bf5dd590%26client_id%3D502103739642-65lmisq7sgpflbpcam61rui5h0kl389t.apps.googleusercontent.com%26hl%3Den-US%26from_login%3D1%26as%3D76cb9819e803393a&ltmpl=popup&oauth=1&sarp=1&scc=1', login_data)
resp = opener.open('http://gameon.dfci.harvard.edu/gameon/snps?find=ajax&amp;build=&amp;strand=&amp;NStudy=&amp;effectAllele=&amp;refAllele=#')
ss = resp.read()
print etree.tostring(etree.HTML(ss), pretty_print=True)



###
from bs4 import BeautifulSoup
import requests

class SessionGoogle:
    def __init__(self, url_login, url_auth, login, pwd):
        self.ses = requests.session()
        login_html = self.ses.get(url_login)
        soup_login = BeautifulSoup(login_html.content, "lxml").find('form').find_all('input')
        dico = {}
        for u in soup_login:
            if u.has_attr('value'):
                dico[u['name']] = u['value']
        # override the inputs with out login and pwd:
        dico['Email'] = login
        dico['Passwd'] = pwd
        self.ses.post(url_auth, data=dico)

    def get(self, URL):
            return self.ses.get(URL).text

    def get(self, URL):
        return self.ses.get(URL).text

url_login = "https://accounts.google.com/ServiceLogin?passive=1209600&continue=https://accounts.google.com/o/oauth2/v2/auth?scope%3Demail%26response_type%3Dcode%26redirect_uri%3Dhttp://gameon.dfci.harvard.edu/gameon/openid_connect_login%26state%3Dd17a90871f34%26nonce%3D1e5c6a1e722b3%26client_id%3D502103739642-65lmisq7sgpflbpcam61rui5h0kl389t.apps.googleusercontent.com%26hl%3Den-US%26from_login%3D1%26as%3D4d374615917fb968&ltmpl=popup&oauth=1&sarp=1&scc=1"
url_auth = "https://accounts.google.com/ServiceLoginAuth"
session = SessionGoogle(url_login, url_auth, "fangf1018@gmail.com", "fff11950")
print session.get("http://plus.google.com")

url_login = "https://accounts.google.com/ServiceLogin"
url_auth = "https://accounts.google.com/ServiceLoginAuth"
session = SessionGoogle(url_login, url_auth, "fangf1018@gmail.com", "fff11950")
print session.get("http://plus.google.com")
print session.get("https://accounts.google.com/ServiceLogin?passive=1209600&continue=https://accounts.google.com/o/oauth2/v2/auth?scope%3Demail%26response_type%3Dcode%26redirect_uri%3Dhttp://gameon.dfci.harvard.edu/gameon/openid_connect_login%26state%3Dd17a90871f34%26nonce%3D1e5c6a1e722b3%26client_id%3D502103739642-65lmisq7sgpflbpcam61rui5h0kl389t.apps.googleusercontent.com%26hl%3Den-US%26from_login%3D1%26as%3D4d374615917fb968&ltmpl=popup&oauth=1&sarp=1&scc=1")





###### ??? Use python to access unread google emails
import urllib2

def get_unread_msgs(user, passwd):
    auth_handler = urllib2.HTTPBasicAuthHandler()
    auth_handler.add_password(
        realm='New mail feed',
        uri='https://mail.google.com',
        user='%s@gmail.com' % user,
        passwd=passwd
    )
    opener = urllib2.build_opener(auth_handler)
    urllib2.install_opener(opener)
    feed = urllib2.urlopen('https://mail.google.com/mail/feed/atom')
    return feed.read()

print get_unread_msgs("fangf1018","fff11950")


##### Use python to access unread google emails
import requests
username = 'fangf1018@gmail.com'
password = 'fff11950'
url = 'https://mail.google.com/mail/feed/atom'
r = requests.get(url, auth=(username, password))
page = r.content
print page
print etree.tostring(etree.HTML(page), pretty_print=True)


import requests
username = 'fangf1018@gmail.com'
password = 'fff11950'
url = 'https://accounts.google.com/ServiceLogin?passive=1209600&continue=https://accounts.google.com/o/oauth2/v2/auth?scope%3Demail%26response_type%3Dcode%26redirect_uri%3Dhttp://gameon.dfci.harvard.edu/gameon/openid_connect_login%26state%3Dd17a90871f34%26nonce%3D1e5c6a1e722b3%26client_id%3D502103739642-65lmisq7sgpflbpcam61rui5h0kl389t.apps.googleusercontent.com%26hl%3Den-US%26from_login%3D1%26as%3D4d374615917fb968&ltmpl=popup&oauth=1&sarp=1&scc=1'
r = requests.get(url, auth=(username, password))
page = r.content
print page
print etree.tostring(etree.HTML(page), pretty_print=True)


#######

s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")
print(r.text)


import requests
r = requests.get('https://api.github.com/user', auth=('fangf1018@gmail.com', 'Ff.11950'))
print r.status_code
print r.headers['content-type']
print r.encoding
print r.text
print r.json()


from requests.auth import HTTPBasicAuth
requests.get('https://api.github.com/user', auth=HTTPBasicAuth('fangf1018@gmail.com', 'Ff.11950'))


r = requests.get('http://en.wikipedia.org/wiki/Monty_Python')
r.text
r.url
r.request.url


import json
r = requests.get('https://api.github.com/repos/kennethreitz/requests/issues/482')
r.status_code
issue = json.loads(r.text)
print(issue[u'title'])
print(issue[u'comments'])
r = requests.get(r.url + u'/comments')
r.status_code
comments = r.json()
print(comments[0].keys())
print(comments[2][u'body'])
print(comments[2][u'user'][u'login'])

body = json.dumps({u"body": u"Sounds great! I'll get right on it!"})
url = u"https://api.github.com/repos/kennethreitz/requests/issues/482/comments"
r = requests.post(url=url, data=body)
r.status_code

from requests.auth import HTTPBasicAuth
auth = HTTPBasicAuth('fake_hahaha@example.com', 'hahaha')
r = requests.post(url=url, data=body, auth=auth)
r.status_code
content = r.json()
print(content[u'body'])



from requests.auth import HTTPBasicAuth
url = 'https://accounts.google.com/ServiceLogin?passive=1209600&continue=https://accounts.google.com/o/oauth2/v2/auth?scope%3Demail%26response_type%3Dcode%26redirect_uri%3Dhttp://gameon.dfci.harvard.edu/gameon/openid_connect_login%26state%3D3eb5122fb8d73%26nonce%3D1c6f3a76f0887%26client_id%3D502103739642-65lmisq7sgpflbpcam61rui5h0kl389t.apps.googleusercontent.com%26hl%3Den-US%26from_login%3D1%26as%3D-5197e24a70d83811&ltmpl=popup&oauth=1&sarp=1&scc=1'
auth = HTTPBasicAuth('fangf1018@gmail.com', 'fff11950')
r = requests.get(url=url, auth=auth)
r.status_code
print r.headers
r.url
print r.text


####################################################

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'http://gameon.dfci.harvard.edu/gameon'
driver = webdriver.Chrome('C:/Program Files/chromedriver.exe')
driver.get(url)
assert 'Welcome to GAME-ON' in driver.title

time.sleep(0.2)
driver.find_element_by_xpath('//*[@id="google_login_form"]/input[3]').click()

time.sleep(0.2)
driver.find_element_by_name("Email").send_keys("fangf1018@gmail.com")
driver.find_element_by_name("signIn").submit()

time.sleep(0.2)
driver.find_element_by_name("Passwd").send_keys("fff11950")
driver.find_element_by_name("signIn").submit()

time.sleep(0.2)
driver.find_element_by_xpath('//*[@id="termsofuse_checkbox"]').click()
driver.find_element_by_name("btnAccept").click()

### Scraping GWAS Table from Webpage
# 2,608,508 entries
from lxml import etree
import re

j = -1
j_ = -1
data = []
data_file = open('C:/Users/ffpku_000/Documents/Research_Genome/Data/Game_On_Data.txt', 'w')
error = []
error_file = open('C:/Users/ffpku_000/Documents/Research_Genome/Data/Game_On_Error_log.txt', 'w')

while j<2608508:

    try_times = 0
    while j == j_ and try_times<100:
        html = etree.HTML(driver.page_source)
        tbody = html.xpath('//*[@id="l_edu_dfci_cccb_gameon_domain_Snp"]/tbody/tr')
        ij = html.xpath('//*[@id="l_edu_dfci_cccb_gameon_domain_Snp_info"]')[0].text
        i = int(re.sub(',', '', re.split(' ', ij)[1]))
        j = int(re.sub(',', '', re.split(' ', ij)[3]))
        new_lines = [[td.text for td in tr] for tr in tbody]
        try_times +=1

    if try_times<100:

        # make sure the data table loaded from html have # of lines as stated
        assert (j-i+1) == len(new_lines)

        # write to file
        for line in new_lines:
            for item in line:
                data_file.write("%r," % item)
            data_file.write('\n')

        # update
        data.append(new_lines)
        j_ = j

    else:

        for line in new_lines:
            for item in range(0, 27):
                data_file.write(" ")
            data_file.write('\n')

        error_file.write(str(j+1)+'\n')


    # click "Next" to load data from next page
    try:
        driver.find_element_by_xpath('//*[@id="l_edu_dfci_cccb_gameon_domain_Snp_next"]').click()
    except UnexpectedAlertPresentException:
        print 'Session seems ended?! '
        break

print len(data)
data_file.close()
error_file.close()

driver.close()






'''

Traceback (most recent call last):
  File "C:\Program Files\Anaconda2\lib\site-packages\IPython\core\interactiveshell.py", line 3066, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-239-0365b3c0d98b>", line 32, in <module>
    html = etree.HTML(driver.page_source)
  File "C:\Program Files\Anaconda2\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 464, in page_source
    return self.execute(Command.GET_PAGE_SOURCE)['value']
  File "C:\Program Files\Anaconda2\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "C:\Program Files\Anaconda2\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 181, in check_response
    raise exception_class(message, screen, stacktrace)
UnexpectedAlertPresentException: Alert Text: None
<super: <class 'WebDriverException'>, <UnexpectedAlertPresentException object>>
In[240]: print len(data)

'''
