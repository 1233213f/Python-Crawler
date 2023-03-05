import requests
import execjs
import json

result = True
headers = {
    'Cookie': 'BAIDUID=2DB1AFA0F846F42901047AED8B33E89D:FG=1; BAIDUID_BFESS=2DB1AFA0F846F42901047AED8B33E89D:FG=1; __yjs_duid=1_0faee1072060aa9da16e45836d86a0401616929924749; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1616929926; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1616929927; __yjsv5_shitong=1.0_7_2b075ac61e99db24c5ec74a3d00655137508_300_1616929925818_219.146.214.92_2235fd8a; ab_sr=1.0.0_YzAwY2E0NTI5MjBiYmNhNjQ2Y2VmNDljMGU4MjgyYmM5ZTYxNjUwYzI2ZTlkZDAyZjMxNDIxODU5Y2RhNzE0YTRkOTVlM2Y1ZmIyOTc5OWQ4YzYzY2NkZjdjYjEyZjA4',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}

with open("sign.js","r") as f:
    s = f.read()

# 为参数动态赋值
def setparameter(input,p_from,p_to):
    global formdata
    # 获取动态生成的sign值
    # 第一个参数默认，第二个参数是我们要翻译的内容
    sign = execjs.compile(s).call("e", input)
    formdata = {
    'from': p_from,
    'to': p_to,
    'query': input,
    'transtype': 'translang',
    'sign': sign,
    'simple_means_flag': 3,
    'token': '2b05b729bcef9ccb94cf5d6ea7154362',
    'domain': 'common'
    }

# 获取数据，提取翻译结果
def translate(input):
    if result == True:
        parameter_from = "zh"
        parameter_to = "en"
        url = "https://fanyi.baidu.com/v2transapi?from=zh&to=en"  # 中文译为英文
    else:
        parameter_from = "en"
        parameter_to = "zh"
        url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"  # 英文译为中文
    setparameter(input,parameter_from,parameter_to)
    html = requests.post(url,data = formdata,headers=headers).text
    html = json.loads(html)
    results = html['liju_result']['tag']  #  提取翻译结果
    print("翻译结果：")
    for get in results:
        print(get)

# 程序入口
def main():
    global result
    userinput = input("请输入需要翻译的内容：")
    # 判断用户输入是否为中文，若为中文执行汉译英，若为英文执行英译汉
    for ch in userinput:
        if '\u4e00' <= ch <= '\u9fff':
            result = True
        else:
            result = False
    translate(userinput)

main()
