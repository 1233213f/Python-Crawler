import requests
url='https://baidu.com'
response=requests.get(url)

print(response.encoding)
response.encoding='utf-8'

print(response.text)

#print(response.encoding)\
print(response.content.decode())