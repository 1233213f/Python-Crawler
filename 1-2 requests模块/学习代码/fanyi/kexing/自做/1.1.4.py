import requests
import json
import sys

# word = input("Please input a word：")
headers = {
    # 百度
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/x-www-form-urlencoded",
    "cookie": "BAIDUID=FC63C630AFF8B9316B089EDF7B8415DE:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BIDUPSID=F04E3A354DE23180A5590BEA7E406E4E; PSTM=1562398118; H_WISE_SIDS=130985_126887_133104_114550_133855_130510_133282_131887_128142_120209_133254_133017_132909_133044_131246_132439_130763_132378_131518_118887_118876_118851_118829_118800_131651_132841_132604_107320_133158_132590_132782_130127_133352_133303_132889_129648_132557_132538_133836_133472_131905_128892_133847_132552_132675_132543_131423_133414_132905_133009_110085_131570_127969_123289_131752_131296_127417_133914; H_PS_PSSID=1465_21086_29237_28518_29099_28831_29220_26350_29071; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; delPer=0; PSINO=3; locale=zh; yjs_js_security_passport=0a5e1f994df0ad23b5e87ca58f7d4ee59561bcc7_1562557459_js; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1562558308,1562558314,1562558467,1562567665; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1562567665; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1562558308,1562558314,1562558467,1562567665; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1562567665",
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
    # 有道
    # "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}
post_data = {
    # 有道
    # "inputtext": "傻子",
    # "type": "AUTO",
    # 百度
    "query": "人生苦短",
    "from": "zh",
    "to": "en",
    "token": "ffe943c7f668b03a5bc968f9cbdd88df",
    "sign": "822331.552714",
}
post_url = "https://fanyi.baidu.com/basetrans"

response = requests.post(post_url, data=post_data, headers=headers)
print(response.content.decode())
dict_ret = json.loads(response.content.decode())
# ret = dict_ret["trans"][0]["dst"]
ret = dict_ret["trans"][0]["result"][0][1]
print("result is：", ret)
