import requests, time, hashlib  # 导入所需模块，hashlib为md5加密所需模块


def youdao(susu):
    # data上传需要修改的数据
    salt = int(time.time() * 10000)
    ts = salt // 10
    value = 'fanyideskweb' + word + str(salt) + '@6f#X3=cCuncYssPsuRUE'  # 此数据通过网页json文件查找并进行修改
    # 通过加密获取所需要的加密格式
    md5 = hashlib.md5()
    md5.update(bytes(value, encoding='utf-8'))
    sign = md5.hexdigest()
    # 从网页上开发者工具里复制请求头下的所有值，大多数都是必须值，并将gzip压缩文件注释掉
    headers = {
        'Accept': 'application/json, text/javascript, /; q=0.01',
        # 'Accept-Encoding': 'gzip, deflate', #注释掉
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '236',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; OUTFOX_SEARCH_USER_ID=-839780230@111.192.38.245; JSESSIONID=abcw8bo9Cp-3WauQT8YTw; OUTFOX_SEARCH_USER_ID_NCOO=1021282290.091752; ___rl__test__cookies=1561013181101',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    # 从网页上开发者工具里复制所需要上传的数据所有值，注：i salt sign ts 随机变化的
    data = {
        'i': word,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'ts': ts,
        'bv': 'c4e95e621267f4d4577f554f2869b772',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME',
    }
    # 翻译接口地址
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    # 请求数据并返回
    response = requests.post(url=url, headers=headers, data=data).text
    # 进行拼接
    data_all = '单词:' + word + "\t" + '翻译:' + response + "\n"
    # 将所有翻译单词保存到文件里
    with open('youdao.txt', 'a', encoding='utf-8') as f:
        f.write(data_all)
    return response


# 主函数
if __name__ == '__main__':
    while True:
        word = input('请输入需要翻译的单词:')
        susu = youdao(word)
        print(susu)