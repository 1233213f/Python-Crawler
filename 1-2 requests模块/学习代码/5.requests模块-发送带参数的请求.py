import requests
# url='https://www.baidu.com/s?wd=pyhton'
# headers={
#     'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Mobile Safari/537.36'
# }
# response=requests.get(url,headers=headers)
# with open('baidu.html','wb')as f:
#     f.write(response.content)
url='https://www.baidu.com/s?'
headers={
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Mobile Safari/537.36'
}
data={
    'wd':'pyhton'
}
response=requests.get(url,headers=headers,params=data)
print(response.url)
with open('baidu1.html','wb')as f:
    f.write(response.content)
