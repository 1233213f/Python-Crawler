import requests
url='https://baidu.com'
response=requests.get(url)
print(len(response.content.decode()))
print(response.content.decode())
headers={
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Mobile Safari/537.36'
}
response1=requests.get(url,headers=headers)

print(response1.content.decode())
print(len(response1.content.decode()))