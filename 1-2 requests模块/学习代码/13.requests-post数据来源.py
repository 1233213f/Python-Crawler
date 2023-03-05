import requests
import json
# https://fanyi.baidu.com/multitransapi

class King(object):

    def __init__(self, word):
        self.url = "https://fanyi.baidu.com/v2transapi?from=zh&to=en"
        url1 = 'https://fanyi.baidu.com/'
        res_1 = session.get(url1).content.decode()
        # 正则提取
        token = re.findall('name="token" value="(.*?)" />', res_1)[0]  # "."匹配所有，“*”指多个，
        print(token)
        self.word = word
        self.headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Mobile Safari/537.36'}
        self.post_data = {
            "from": "zh",
            "to": "en",
            "query": self.word,
            "transtype": "realtime",
            "simple_means_flag": "3",
            "sign": 690025.943192,
            "token": ,
            "domain": "common"
        }
    def get_data(self):
        response = requests.post(self.url, headers=self.headers, data=self.post_data)
        # 默认返回bytes类型，除非确定外部调用使用str才进行解码操作
        return response.content

    def parse_data(self, data):

        # 将json数据转换成python字典
        dict_data = json.loads(data)

        # 从字典中抽取翻译结果
        try:
            print(dict_data['content']['out'])
        except:
            print(dict_data['content']['out'][0])

    def run(self):
        # url
        # headers
        # post——data
        # 发送请求
        data = self.get_data()
        # 解析
        self.parse_data(data)

if __name__ == '__main__':
    # king = King("人生苦短，及时行乐")
    word=input("词句子：\n")
    king = King(word)
    king.run()
    # python标准库有很多有用的方法，每天看一个标准库的使用