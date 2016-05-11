# coding=utf-8
import urllib
import urllib2
import re
import json
import base64
url = 'http://www.lagou.com/jobs/positionAjax.json?'
pn = 3
for pn in range(5):
    post_data = {'first':'true','kd':'python','pn':str(pn)}
    decode_post_data =urllib.urlencode(post_data)
    request = urllib2.Request(url,data=decode_post_data)
    response = urllib2.urlopen(request)
    pageCode = response.read().decode('utf-8')
#print pageCode
    page_json = json.loads(pageCode)
#print type(page_json)
#print page_json.keys()

    page_json = page_json['content']['positionResult']
#print type(page_json)
    page_json = page_json['result']
    pn = pn +1
    i=0
    for i in range(10):
#print page_json[0]
#print type(page_json[0])
#print page_json[0].keys()
        print page_json[i]['companyName'],page_json[i]['city'],page_json[i]['positionType'],page_json[i]['industryField'],page_json[i]['salary']
        i=i+1
#print page_json.keys()
#print page_json
'''
patten = re.compile('"createTime":(.*?)"companyId".*?"positionType":(.*?)"workYear":(.*?) ',re.S)
match = patten.match(pageCode)
print match
items = re.findall(patten,pageCode)
print items
for item in items:
    print item[0],item[1],item[2]

#print type(items),type(items[0])
#pageCode = response.read()
#ss = json.loads(pageCode)
#s = json.dumps(ss,ensure_ascii=False)
#print ss
#print s
#print type(s),type(ss["content"]["result"])
#print ss.keys()
#content = ss["content"]["result"]
#print content
#print content.index(u'companyName')
#print content.index
#print pageCode
'''