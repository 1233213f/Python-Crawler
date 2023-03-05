import requests
import re
import execjs


class BaiduTranslateSpider(object):
    def __init__(self):
        self.get_url = 'https://fanyi.baidu.com/?aldtype=16047'
        self.headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "max-age=0",
            "cookie": "BIDUPSID=92C42CD77D01795CFB404F53DF300F75; PSTM=1592474022; BAIDUID=92C42CD77D01795C8B6F16BDC65002D6:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; yjs_js_security_passport=d12ac5248ad0780a72f91cabe5fd5cfeabc12d36_1593336733_js; delPer=0; PSINO=2; H_PS_PSSID=1431_31672_32141_21087_32139_32045_31708_22158; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1592730594,1592792033,1592962763,1593339867; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1593339867; __yjsv5_shitong=1.0_7_a9e99babc7833c7b19703de982cac135d904_300_1593339843507_175.17.189.189_d0ac9635",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36",
        }


    # 获取sign
    def get_sign(self, word):
        with open('node.js', 'r') as f:
            js_data = f.read()
        execjs_obj = execjs.compile(js_data)
        sign = execjs_obj.eval('e("{}")'.format(word))

        return sign

    # 获取翻译结果
    def get_result(self, word):
        try:
            result = [word]
            fro = 'en'
            to = 'zh'
            token = self.get_token()
            sign = self.get_sign(word)
            # 把formdata定义成字典
            formdata = {
                'from': fro,
                'to': to,
                'query': word,
                'transtype': 'realtime',
                'simple_means_flag': '3',
                'sign': sign,
                'token': token,
            }
            response = requests.post(
                url='https://fanyi.baidu.com/v2transapi',
                data=formdata,
                headers=self.headers,
                timeout=10,
            )
            html_json = response.json()
            for li in html_json['dict_result']['simple_means']['exchange'].values():
                result += li
            return {word: set(result)}
        except Exception as e:
            return {word: set(result)}


if __name__ == '__main__':
    spider = BaiduTranslateSpider()
    word = 'why'
    result = spider.get_result(word)
    print(result)