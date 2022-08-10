import json
import re
import requests
from lxml import etree
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

base_url = 'https://desk.zol.com.cn'


def down(url):
    res = requests.get(url)

    obj = re.compile('var deskPicArr.*?=(?P<deskPicArr>.*?);', re.S)

    deskPicArr = obj.search(res.text).group('deskPicArr')
    pic_list = json.loads(deskPicArr)['list']

    for item in pic_list:
        pic_url = item['imgsrc'].replace('##SIZE##', item['oriSize'])
        print(pic_url)
        res_pic = requests.get(pic_url)
        name = pic_url.split('/')[-1]

        with open(f'img/{name}', mode='wb') as f:
            f.write(res_pic.content)
            f.close()


if __name__ == '__main__':
    with ThreadPoolExecutor(20) as t:
        for i in range(5):
            res = requests.get(f'{base_url}/yingshi/{i + 1}.html')
            res.encoding = 'gbk'

            et = etree.HTML(res.text)
            page_url = et.xpath(r'//a[@class="pic"]/@href')
            del page_url[0:2]

            for page in page_url:
                show_url = base_url + page
                # down(show_url)

                t.submit(down, show_url)
