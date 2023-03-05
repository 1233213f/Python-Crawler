import requests
url='https://baidu.com'

proxies={
    'http':'http://223.82.106.253:3128'
    # 'https':'https://223.82.106.253:3128'
}
response=requests.get(url,proxies=proxies)

print(response.text)