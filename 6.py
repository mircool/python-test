import requests
import re
import json
from lxml import etree


# 下载图片
def down(url: str):
    print(url)
    name = url.split('/')[-1]
    res = requests.get(url)
    with open(f'img/{name}', 'wb') as f:
        f.write(res.content)
        f.close()


# 爬取图片url
def spider_img_url(url: str):
    res = requests.get(url)

    obj = re.compile(r'var deskPicArr.*?=(?P<deskPicArr>.*?);', re.S)
    deskPicArr = obj.search(res.text).group('deskPicArr')
    deskPicArr = json.loads(deskPicArr)
    list_pic = deskPicArr['list']
    for item in list_pic:
        down(item['imgsrc'].replace('##SIZE##', item['oriSize']))


# 爬取分类
def spider_category(url: str = 'https://desk.zol.com.cn/pc/'):
    res = requests.get(url)
    res.encoding = 'gbk'
    et = etree.HTML(res.text)
    category = et.xpath('//dl[@class="filter-item first clearfix"]//a/@href')

    for item in category:
        print(base + item)
        # spider_page_num(base+item)


# 爬取下一页
def spider_page_num(url: str = 'https://desk.zol.com.cn/dongman/'):
    res = requests.get(url)
    res.encoding = 'gbk'

    et = etree.HTML(res.text)
    next_page = et.xpath('//a[@class="next"]/@href')
    if next_page:
        return next_page
    return False


if __name__ == '__main__':
    base = 'https://desk.zol.com.cn'
    spider_category()
