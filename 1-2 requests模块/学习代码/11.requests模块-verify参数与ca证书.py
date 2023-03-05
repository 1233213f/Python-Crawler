import requests
url = "https://sam.huat.edu.cn:8443/selfservice/"
response = requests.get(url,verify=False)
print(response.content)