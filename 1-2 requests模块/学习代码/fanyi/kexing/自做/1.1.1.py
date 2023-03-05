# -*- coding:utf-8 -*-
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
        return response.json()['trans_result']['data'][0]['dst']

if __name__ == '__main__':


    t=input("请输入你要翻译的内容：\n")

    bd = Baidu()

    print(bd.translate(m, n, t))