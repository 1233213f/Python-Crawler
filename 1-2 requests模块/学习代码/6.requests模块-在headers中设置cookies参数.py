import requests
from selenium import webdriver


url='https://github.com/1233213f'
headers={
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Mobile Safari/537.36',
    'cookies': '_octo=GH1.1.736618271.1617286854; _device_id=f2b6915530f847e715879287db542f95; user_session=bSkcyGC-hbYmt4zsSK6JeLH5J9_aJmEv2UZLraJb__kStXyK; __Host-user_session_same_site=bSkcyGC-hbYmt4zsSK6JeLH5J9_aJmEv2UZLraJb__kStXyK; logged_in=yes; dotcom_user=1233213f; has_recent_activity=1; color_mode=%7B%22color_mode%22%3A%22light%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; tz=Asia%2FShanghai; _gh_sess=jpzngW5ELUMcndnMjRHKQR34%2BPthyn25lovcKvLGEBwy9Q1%2Fpxh%2FQTlveJ2%2BAoMfTFBuj%2BeKcCNrn8LBpgZ1gcPVmm0oWGeyhbq4SqO7ZVjxA1JTyYeCkch4UK8Gbx%2BOTPnYQh%2FpUDQ5x5cjFCfbUv70HrTm6Y8Kx5gux8z7aO3csWAF25FfT3TSgbPj4eOF--pySu5mUsbjBbCGQO--vYD69vahLhMdLuzn8vNT1Q%3D%3D'
}

driver=webdriver.Chrome()
driver.get(url)
# response=requests.get(url,headers=headers)

with open("github.html","wb")as f:
    f.write(response.content)