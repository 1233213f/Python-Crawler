import requests
url='https://baidu.com'
request=requests.get(url)
print(request.text)