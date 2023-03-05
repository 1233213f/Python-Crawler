import json
import requests


class Translator:
    @staticmethod
    def translate(text, src, dst):
        src = src.replace("-", "_")
        dst = dst.replace("-", "_")
        tp = src.upper() + "2" + dst.upper()
        url = f"http://fanyi.youdao.com/translate?&doctype=json&type={tp}&i={text}"
        resp = requests.get(url)
        return json.loads(resp.content)


def test():
    translator = Translator()
    print(translator.translate("于千万人之中 遇见你所遇见的人 于千万年之中 时间的无涯的荒野里 没有早一步 也没有晚一步 刚好赶上了 张爱玲", "zh-CN", "en"))
    a='于千万人之中 遇见你所遇见的人 于千万年之中 时间的无涯的荒野里 没有早一步 也没有晚一步 刚好赶上了 张爱玲'

if __name__ == "__main__":
    test()