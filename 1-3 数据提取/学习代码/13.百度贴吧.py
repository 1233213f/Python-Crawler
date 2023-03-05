import requests
from lxml import etree

class Tieba(object):

    def __init__(self,name):
        self.url= "http://tieba.baidu.com/f?ie=utf-8&kw={}".format(name)
        self.headers={
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Mobile Safari/537.36"
        }
    def get_data(self,url):
        response=requests.get(url,headers=self.headers)
        with open("temp.html","wb")as f:
            f.write(response.content)
        return response.content

    def parse_data(self,data):
        data=data.decode().replace("<!--","").replace("-->","")
        html=etree.HTML(data)
        el_list=html.xpath('//*[@id="thread_list"]/li/div/div[2]/div[1]/div[1]/a')
        print(len(el_list))

    def run(self):
        data=self.get_data(self.url)
        self.parse_data(data)

if __name__== '__main__':
    tieba=Tieba("贵州大学")
    tieba.run()
