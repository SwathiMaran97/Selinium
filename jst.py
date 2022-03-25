# import scrapy

# class MySpider(scrapy.Spider):
#     name = 'icsi'

#     start_urls = ['https://www.icsi.in/Student/Default.aspx?TabID=100']

#     search_action_url = 'https://www.icsi.in/Student/Default.aspx?TabID=100'

#     def parse(self, response):
#         formdata = dict()
#         for input in response.css('form#Form input'):
#             name = input.xpath('./@name').get()
#             value = input.xpath('./@value').get()
#             formdata[name] = str(value) if value else ''
#         formdata['dnn$ctr410$MemberSearch$txtCpNumber'] = '16308'
#         formdata['__EVENTTARGET'] = 'dnn$ctr410$MemberSearch$btnSearch'

#         return scrapy.FormRequest(self.search_action_url, formdata=formdata, callback=self.parse_search)

#     def parse_search(self, response):
#         scrapy.shell.inspect_response(response, self)
#         return
# import requests
# from lxml import html
# import json
# import sys

# session_requests = requests.session()
# login_url = sys.argv[1]
# tokenname = sys.argv[2]
# result = session_requests.get(login_url)
# htmls = html.fromstring(result.text)

# csrf = list(set(htmls.xpath("//input[@name={}]/@value".format(tokenname))))[0]

# print (csrf)
import requests_html
import lxml
from bs4 import BeautifulSoup
import requests
import json
import sys
# s = requests.session()
# login = s.get('https://vconnect.net/login')
# login_html = lxml.html.fromstring(login.text)
# hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')
# form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}
# print(form)
# {'_token': 'cAsN1Gb5Mo6EfdtZYsD29t5fWbiXIHcwWiRx3N2b', 
#  'context': ''}
# form['email'] = "swathi.com"
# form['password'] = "r2r22123"
# response = s.post('https://vconnect.net/login', data=form)
# response.url
# print('jj')

s = requests_html.HTMLSession()
html = s.get('https://vconnect.net/login')
# r.html.render(sleep=5, timeout=8)
doc = lxml.html.fromstring(html.content)

auth = doc.xpath("//*[@id='orangeForm-email']")[0]
a=input(auth)
auth1 = doc.xpath("//*[@id='orangeForm-pass']")[0]
a1=input(auth1)
# s.post('/html/body/header/section/div/div/div/div[2]/div/div/form/div[4]/button')
login_data={a,a1}
r= s.post('https://vconnect.net/login', data=login_data)
r.status_code
print(r.status_code)
# with requests.Session() as session:
#     post = session.post(POST-LOGIN-URL, data=payload)
#     r = session.get(REQUEST-URL)
#     print(r.text)