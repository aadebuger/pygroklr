#encoding=utf-8
'''
Created on 2017年10月12日

@author: aadebuger
'''


from pygrok import Grok


text='222.246.37.225 - - [30/Jul/2017:11:12:02 +0800] "GET /template/html/5f/597849dbdbe5f.html HTTP/1.1" 304 0 "http://hot.eastday.com/mini045/index-in.html" "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727)" "-" "dytz2.dyrh168.com"'
pattern = '%{IPORHOST:clientip} %{USER:ident} %{USER:auth} \[%{HTTPDATE:timestamp}\] "(?:%{WORD:verb} %{NOTSPACE:request}(?: HTTP/%{NUMBER:httpversion})?|%{DATA:rawrequest})" %{NUMBER:response} (?:%{NUMBER:bytes}|-) %{QS:referrer} %{QS:agent} %{QS:forword} %{QS:host}'
# {'gender': 'male', 'age': '25', 'name': 'gary', 'weight': '68.5'}
grok = Grok(pattern)
print grok.match(text)

print("cdn")
text='113.201.30.129 MISS 118 [11/Oct/2017:06:10:14 +0800] "GET http://dytz.dyry168.com/favicon.ico HTTP" 200 1172 "-" "Mozilla/5.0 (Linux; U; Android 6.0; zh-cn; ALE-TL00 Build/HuaweiALE-TL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36"'
pattern = '%{IPORHOST:clientip} %{USER:ident} %{USER:auth} \[%{HTTPDATE:timestamp}\] "(?:%{WORD:verb} %{NOTSPACE:request}(?: HTTP)?|%{DATA:rawrequest})" %{NUMBER:response} (?:%{NUMBER:bytes}|-) %{QS:referrer} %{QS:agent}'
# {'gender': 'male', 'age': '25', 'name': 'gary', 'weight': '68.5'}
grok = Grok(pattern)
print grok.match(text)
print("cdn domain")
pattern = '%{IPORHOST:clientip} %{USER:ident} %{USER:auth} \[%{HTTPDATE:timestamp}\] "(?:%{WORD:verb} http://%{URIHOST:domain_host}%{NOTSPACE:request}(?: HTTP)?|%{DATA:rawrequest})" %{NUMBER:response} (?:%{NUMBER:bytes}|-) %{QS:referrer} %{QS:agent}'
# {'gender': 'male', 'age': '25', 'name': 'gary', 'weight': '68.5'}
grok = Grok(pattern)
print grok.match(text)

text="http://dytz.dyry168.com/favicon.ico"
pattern='http://%{URIHOST:urihost}%{NOTSPACE:request}'
grok = Grok(pattern)
print("url")
print grok.match(text)


if __name__ == '__main__':
    pass