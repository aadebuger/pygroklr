#encoding=utf-8
'''
Created on 2017年10月19日

@author: aadebuger
'''
from pygrok import Grok

text="""Jun  8 03:35:36 localhost haproxy[2839]: 116.231.254.57:65076 [08/Jun/2017:03:35:36.228] api.xxx.com~ nodes/nginx1 30/0/1/6/37 200 369 - - ---- 1/1/1/0/0 0/0 "OPTIONS /1.1/classes/AudioInformation?&where=%7B%22status%22%3A%221%22%2C%22createdAt%22%3A%7B%22%24gte%22%3A%7B%22__type%22%3A%22Date%22%2C%22iso%22%3A%222016-10-01T00%3A00%3A00.000Z%22%7D%7D%7D&keys=status&order=-createdAt&limit=0&count=1 HTTP/1.1"
"""
#ok
pattern = """%{IP:client_ip}:%{NUMBER:client_port:int} \[%{NOTSPACE:haproxy_timestamp}\] %{NOTSPACE:frontend_name} %{NOTSPACE:backend_name} %{NUMBER:time_queue:int}/%{NUMBER:time_backend_connect:int}/%{NUMBER:time_duration:int}/%{NUMBER:time_duration1:int}/%{NUMBER:time_duration2:int} %{NUMBER:bytes_read:int} %{NOTSPACE:termination_state} - - ---- %{NUMBER:actconn:int}/%{NUMBER:feconn:int}/%{NUMBER:beconn:int}/%{NUMBER:srvconn:int}/%{NUMBER:retries:int} %{NUMBER:srv_queue:int}/%{NUMBER:backend_queue:int} \"%{DATA:captured_request_headers}\""""
#fail
pattern = """%{IP:client_ip}:%{NUMBER:client_port:int} \[%{NOTSPACE:haproxy_timestamp}\] %{NOTSPACE:frontend_name} %{NOTSPACE:backend_name} %{NUMBER:time_queue:int}/%{NUMBER:time_backend_connect:int}/%{NUMBER:time_duration:int}/%{NUMBER:time_duration1:int}/%{NUMBER:time_duration2:int} %{NUMBER:bytes_read:int} %{NOTSPACE:termination_state} - - ---- %{NUMBER:actconn:int}/%{NUMBER:feconn:int}/%{NUMBER:beconn:int}/%{NUMBER:srvconn:int}/%{NUMBER:retries:int} %{NUMBER:srv_queue:int}/%{NUMBER:backend_queue:int} ?( \"%{GREEDYDATA:full_http_request}\")?( %{NOTSPACE:captured_response_headers})?"""

pattern = """%{DATA:captured_request_headers1}: %{IP:client_ip}:%{NUMBER:client_port:int} \[%{NOTSPACE:haproxy_timestamp}\] %{NOTSPACE:frontend_name} %{NOTSPACE:backend_name}/%{NOTSPACE:server_name} %{NUMBER:time_queue:int}/%{NUMBER:time_backend_connect:int}/%{NUMBER:time_duration:int}/%{NUMBER:time_duration1:int}/%{NUMBER:time_duration2:int} %{NUMBER:bytes_read:int} %{NOTSPACE:termination_state} - - ---- %{NUMBER:actconn:int}/%{NUMBER:feconn:int}/%{NUMBER:beconn:int}/%{NUMBER:srvconn:int}/%{NUMBER:retries:int} %{NUMBER:srv_queue:int}/%{NUMBER:backend_queue:int} \"(<BADREQ>|(%{WORD:http_verb} (%{URIPROTO:http_proto}://)?(?:%{USER:http_user}(?::[^@]*)?@)?(?:%{URIHOST:http_host})?(?:%{URIPATHPARAM:http_request})?( HTTP/%{NUMBER:http_version})?))?\""""



grok = Grok(pattern)
print grok.match(text)


text="""Oct 14 06:28:15 localhost haproxy[7310]: 180.169.122.18 - - [14/Oct/2017:06:28:15 +0000] GET /xxx/quotephp_v2/Api/quote/dyna?obj=SZ002407 HTTP/1.1 200 470 - Jakarta Commons-HttpClient/3.1 - xxx.com"""

text="""Oct 14 06:28:15 localhost haproxy[7310]: 180.169.122.18 - - [14/Oct/2017:06:28:15 +0000] GET /xxxx/quotephp_v2/Api/quote/dyna?obj=SZ002407 HTTP/1.1 200 470 - Jakarta Commons-HttpClient/3.1 - xxx.com"""
pattern="""%{DATA:captured_request_headers1}: %{IPORHOST:clientip} %{USER:ident} %{USER:auth} \[%{HTTPDATE:timestamp}\] (?:%{WORD:verb} %{NOTSPACE:request}(?: HTTP/%{NUMBER:httpversion})?|%{DATA:rawrequest}) %{NUMBER:response} (?:%{NUMBER:bytes}|-) (%{QS:referrer}|-) %{GREEDYDATA:agent} %{GREEDYDATA:forword} %{GREEDYDATA:host}"""
#pattern = """%{DATA:captured_request_headers1}: %{IPORHOST:clientip} %{USER:ident} %{USER:auth} \[%{HTTPDATE:timestamp}\] (?:%{WORD:verb} %{NOTSPACE:request}(?: HTTP/%{NUMBER:httpversion})?|%{DATA:rawrequest}) %{NUMBER:response} (?:%{NUMBER:bytes}|-) %{QS:referrer} %{QS:agent} %{QS:forword} %{QS:host}"""



grok = Grok(pattern)
print grok.match(text)


if __name__ == '__main__':
    pass