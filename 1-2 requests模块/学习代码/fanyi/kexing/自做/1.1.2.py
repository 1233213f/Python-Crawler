# -*-coding: utf-8 -*
import requests
import execjs
import re


class Baidu(object):

    def __init__(self):
        self.url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
        self.header = {
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'origin': 'https://fanyi.baidu.com',
            'referer': 'https://fanyi.baidu.com/?aldtype=16047',
            'user-agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Mobile Safari/537.36",
            'x-requested-with': 'XMLHttpRequest',
            'cookie': 'PSTM=1617286808; BAIDUID=ADB4B57BAD64E89BA72F04D5F5C49BA2:FG=1; BIDUPSID=44A8F4ACEE884666EDCA81002A0C2A57; __yjs_duid=1_22f80a5922d92e08277474c219336a581617378807065; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; FANYI_WORD_SWITCH=1; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; H_WISE_SIDS=107316_110085_127969_131423_154214_164075_165136_165935_166147_167538_168388_168542_168767_169308_170149_170495_170588_170759_170761_170816_170873_171158_171214_171626_171649_171671_171849_171988_171990_172291_172310_172406_172472_172590_172678_172718_172997_173016_173124_173127_173130_173244; BDUSS=Up5cjlLWU1yak9iZm5jd2d4YUVoOG5ULVFueUdwaXdFdmNXLTFEdk1KQ0Z5SlJnRVFBQUFBJCQAAAAAAAAAAAEAAAAu2UrOwePRqbPgMjAxOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIU7bWCFO21gU; BDUSS_BFESS=Up5cjlLWU1yak9iZm5jd2d4YUVoOG5ULVFueUdwaXdFdmNXLTFEdk1KQ0Z5SlJnRVFBQUFBJCQAAAAAAAAAAAEAAAAu2UrOwePRqbPgMjAxOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIU7bWCFO21gU; BAIDUID_BFESS=ADB4B57BAD64E89BA72F04D5F5C49BA2:FG=1; H_PS_PSSID=33817_33751_33344_31660_33758_33676_22157; delPer=0; PSINO=7; BA_HECTOR=2k24a120alal8g2k3t1g6u61l0r; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1617634436,1617705185,1617808417,1617893430; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1617810243,1617893458; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1617893458; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1617893703; __yjs_st=2_NTQxMjViZGI3ZTc1OTVhYzQxZWEyNjI2MjhjMGZmODI0M2E4MDE2YjQzMmVlOWI0NjQ0ZDJhZGJjNWY4YzUwYWQwNjNjNDUyYjNkNjRmY2RkZmY5ZjM1OTcwOTUwNWJjZjI0MWM5MWY5Mzk4MmIyMTAwMGY0ZDQyYzhhNmU4NDk5NjE0MjgwZGI0MzEyNDgzZTRiYWZhYjg1OGQ0YzBiYWU3NjdmYTc3NjQ1N2JhNDIzODZiNWVkYjliMzk5ZDQ1NWRjMDQ0ODg5ZmNiZWY4NjdlZjUzYjZkZjM5ZjAwMjdiMGUyNzdlMDA5MTY5NzFlMWZlNmQ1ZmYyMDFjMWI0OF83X2U1NjU4MzE0; ab_sr=1.0.0_YWQwN2VjZmMwNzQwM2MyMGMwZmFlNDQ3Y2FiZTY1OWRhMzg5MTkwNGNjOTdhZThmYWU2MWQzYmJjODQwZDFlZTZhNDcxODcyYzBhZDU2OGJhNjY5M2VjYTJhMDJkNjAyZjU0MzUyYjliNzVhZmJkMWFmNDcwZTkyNTZlZjYyOWE='
        }

        self.data = None

    def get_sign_ctx(self):
        ctx = execjs.compile(
            r"""

             function n(r, o) {
                for (var t = 0; t < o.length - 2; t += 3) {
                    var a = o.charAt(t + 2);
                    a = a >= "a" ? a.charCodeAt(0) - 87 : Number(a),
                    a = "+" === o.charAt(t + 1) ? r >>> a : r << a,
                    r = "+" === o.charAt(t) ? r + a & 4294967295 : r ^ a
                    }
                return r
                 }

            function e(r) {
        var o = r.match(/[\uD800-\uDBFF][\uDC00-\uDFFF]/g);
        if (null === o) {
            var t = r.length;
            t > 30 && (r = "" + r.substr(0, 10) + r.substr(Math.floor(t / 2) - 5, 10) + r.substr(-10, 10))
        } else {
            for (var e = r.split(/[\uD800-\uDBFF][\uDC00-\uDFFF]/), C = 0, h = e.length, f = []; h > C; C++)
                "" !== e[C] && f.push.apply(f, a(e[C].split(""))),
                C !== h - 1 && f.push(o[C]);
            var g = f.length;
            g > 30 && (r = f.slice(0, 10).join("") + f.slice(Math.floor(g / 2) - 5, Math.floor(g / 2) + 5).join("") + f.slice(-10).join(""))
        }
        var u = void 0
          , l = "" + String.fromCharCode(103) + String.fromCharCode(116) + String.fromCharCode(107);
        u =' """ + str(self.get_gtk()) + r""" ';
        for (var d = u.split("."), m = Number(d[0]) || 0, s = Number(d[1]) || 0, S = [], c = 0, v = 0; v < r.length; v++) {
            var A = r.charCodeAt(v);
            128 > A ? S[c++] = A : (2048 > A ? S[c++] = A >> 6 | 192 : (55296 === (64512 & A) && v + 1 < r.length && 56320 === (64512 & r.charCodeAt(v + 1)) ? (A = 65536 + ((1023 & A) << 10) + (1023 & r.charCodeAt(++v)),
            S[c++] = A >> 18 | 240,
            S[c++] = A >> 12 & 63 | 128) : S[c++] = A >> 12 | 224,
            S[c++] = A >> 6 & 63 | 128),
            S[c++] = 63 & A | 128)
        }
        for (var p = m, F = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(97) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(54)), D = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(51) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(98)) + ("" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(102)), b = 0; b < S.length; b++)
            p += S[b],
            p = n(p, F);
        return p = n(p, D),
        p ^= s,
        0 > p && (p = (2147483647 & p) + 2147483648),
        p %= 1e6,
        p.toString() + "." + (p ^ m)
    }
            """
        )
        return ctx

    def get_sign(self, text):
        ctx = self.get_sign_ctx()
        sign = ctx.call("e", text)
        print(sign)
        return sign

    def get_token(self):
        s = requests.session()
        url = 'https://fanyi.baidu.com/'
        html = requests.get(url, headers=self.header)
        html = html.text
        # print(html)
        raw_tk_str = str(re.search('token:.*,', html))
        token = raw_tk_str.split('\'')[1]
        print(token)
        return token

    def get_cookie(self):
        import urllib.request
        import http.cookiejar
        cookie = http.cookiejar.CookieJar()
        handler = urllib.request.HTTPCookieProcessor(cookie)
        opener = urllib.request.build_opener(handler)
        response = opener.open('https://fanyi.baidu.com/?aldtype=16047#zh/en/aa%E9%80%9F%E5%BA%A6')
        # print(response)
        for item in cookie:
            print('%s = %s' % (item.name, item.value))

    def get_gtk(self):
        url = 'https://fanyi.baidu.com/'
        html = requests.get(url)
        html = html.text
        raw_gtk_str = str(re.search('window.gtk = .*;', html))
        gtk = raw_gtk_str.split('\'')[1]
        # print('gtk '+gtk)
        return gtk

    def get_data(self, from_lan, to_lan, text):
        data = {}
        data['from'] = from_lan
        data['to'] = to_lan
        data['query'] = text
        data['simple_means_flag'] = 3
        data['transtype'] = 'realtime'
        data['sign'] = self.get_sign(text)
        data['token'] = self.get_token()
        return data

    def translate(self, from_lan, to_lan, text):
        self.data = self.get_data(from_lan, to_lan, text)
        s = requests.session()
        response = requests.post(self.url, headers=self.header, data=self.data)
        print(response.json())
        return response.json()['trans_result']['data'][0]['dst']
'''    langList: {
'zh': '中文'
'jp': '日语'
'jpka': '日语假名'
'th': '泰语'
'fra': '法语'
'en': '英语'
'spa': '西班牙语'
'kor': '韩语'
'tr': '土耳其语'
'vie': '越南语'
'ms': '马来语'
'de': '德语'
'ru': '俄语'
'ir': '伊朗语'
'ara': '阿拉伯语'
'est': '爱沙尼亚语'
'be': '白俄罗斯语'
'bul': '保加利亚语'
'hi': '印地语'
'is': '冰岛语'
'pl': '波兰语'
'fa': '波斯语'
'dan': '丹麦语'
'tl': '菲律宾语'
'nl': '荷兰语'
'ca': '加泰罗尼亚语'
'cs': '捷克语'
'hr': '克罗地亚语'
'lv': '拉脱维亚语'
'lt': '立陶宛语'
'rom': '罗马尼亚语'
'af': '南非语'
'pt_BR': '巴西语'
'pt': '葡萄牙语'
'swe': '瑞典语'
'sr': '塞尔维亚语'
'eo': '世界语'
'sk': '斯洛伐克语'
'slo': '斯洛文尼亚语'
'sw': '斯瓦希里语'
'iw': '希伯来语'
'el': '希腊语'
'hu': '匈牙利语'
'hy': '亚美尼亚语'
'it': '意大利语'
'id': '印尼语'
'sq': '阿尔巴尼亚语'
'am': '阿姆哈拉语'
'as': '阿萨姆语'
'az': '阿塞拜疆语'
'eu': '巴斯克语'
'bn': '孟加拉语'
'bs': '波斯尼亚语'
'gl': '加利西亚语'
'ka': '格鲁吉亚语'
'gu': '古吉拉特语'
'ha': '豪萨语'
'ig': '伊博语'
'iu': '因纽特语'
'ga': '爱尔兰语'
'zu': '祖鲁语'
'kn': '卡纳达语'
'kk': '哈萨克语'
'lb': '卢森堡语'
'mk': '马其顿语'
'mt': '马耳他语'
'mi': '毛利语'
'mr': '马拉提语'
'ne': '尼泊尔语'
'or': '奥利亚语'
'pa': '旁遮普语'
'tn': '塞茨瓦纳语'
'si': '僧加罗语'
'ta': '泰米尔语'
'tt': '塔塔尔语'
'te': '泰卢固语'
'ur': '乌尔都语'
'uz': '乌兹别克语'
'cy': '威尔士语'
'yo': '约鲁巴语'
'yue': '粤语'
'wyw': '文言文'
'cht': '中文繁体' '''

# a1 = "zh"
# a2 = "jp"
# a3 = "jpka"
# a4 = "th"
# a5 = "fra"
# a6 = "en"
# a7 = "spa"
# a8 = "kor"
# a9 = "tr"
# a10 = "vie"
# a11 = "ms"
# a15 = "de"
# a12 = "yue"
# a13 = "wyw"
# a14 = "cht"
if __name__ == '__main__':
    stopword = ":q"
    # print("1 中文 2 日语 3 日语假名 4 泰语 5 法语 6 英语 7 西班牙语 8 韩语 9 土耳其语 10 越南语  11 马来语  12 粤语 13 文言文 14 中文繁体  15 德语")
    m1=eval(input(print("被翻译翻译语言\n")))
    n1=eval(input(print("翻译语言\n")))
    t=input("请输入你要翻译的内容：\n")


    # print(len(t1.split(',')))


    d="zh,jp,jpka,th,fra,en,spa,kor,tr,vie,ms,de,ru,ir,ara,est,be,bul,hi,pl,fa,dan,tl,nl,ca,cs,hr,lv,lt,rom,af,pt_BR,pt,swe,sr,eo,sk,slo,sw,iw,el,hu,hy,it,id,sq,am,yue,wyw,cht"
    print(t)
    m=d.split(',')[m1]
    n=d.split(',')[n1]
    t1 = "于千万之中,遇见你所遇见的人,于千万年之中,时间的无涯的荒野里,没有早一步,也没有晚一步刚好赶上了,——张爱玲"
    o=len(t1.split(','))
    bd = Baidu()
    for i in range(0,7):
        print(bd.translate(m, n, t1.split(',')[1]),'',o)
        print('\n')

    # print(bd.translate(from_lan, to_lan, t))

# 于千万之中
# 遇见你所遇见的人，
# 于千万年之中，时间的无涯的荒野里
# 没有早一步，
# 也没有晚一步，
# 刚好赶上了
# ——张爱玲