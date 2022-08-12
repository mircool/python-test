import requests
import re
import json
from lxml import etree
from concurrent.futures import ThreadPoolExecutor


# 下载图片
def down(url: str):
    print(f'开始下载图片{url}')
    name = url.split('/')[-1]
    res = requests.get(url)
    with open(f'img/{name}', 'wb') as f:
        f.write(res.content)
        f.close()
    print(f'{url}图片下载完成')


# 爬取图片url
def spider_img_url(url: str = 'https://desk.zol.com.cn/bizhi/8229_102247_2.html'):
    print(f'正在爬取{url}')
    res = requests.get(url)

    obj = re.compile(r'var deskPicArr.*?=(?P<deskPicArr>.*?);', re.S)
    deskPicArr = obj.search(res.text).group('deskPicArr')
    deskPicArr = json.loads(deskPicArr)
    img_src = []

    list_pic = deskPicArr['list']
    for item in list_pic:
        # print(item['oriSize'],item['resAll'])
        resAll = item['resAll']
        oriSize = [item['oriSize']]
        all = resAll + oriSize
        base_img_src = item['imgsrc']

        for i in all:
            img_url = base_img_src.replace('##SIZE##', i)
            img_src.extend([img_url])

    return img_src  # 返回所有图片的地址


# 爬取分类 返回所有分类链接
def spider_category(url: str = 'https://desk.zol.com.cn/pc/'):
    print(f'正在爬取分类：{url}')
    res = requests.get(url)
    res.encoding = 'gbk'
    et = etree.HTML(res.text)
    category = et.xpath('//dl[@class="filter-item first clearfix"]//a/@href')

    cate = []
    for item in category:
        cate.append(base_url + item)

    return cate


# 爬取所有页码  返回所有的分页
def spider_page_num(url: str = 'https://desk.zol.com.cn/dongman/'):
    print(f'正在爬取分页：{url}')
    whole_url = url + '10000.html'
    res = requests.get(whole_url)
    res.encoding = 'gbk'

    et = etree.HTML(res.text)

    if et.xpath('//span[@class="active"]/text()'):  # 先判断是否存在翻页
        max_page_num = et.xpath('//span[@class="active"]/text()')[0]
    else:
        max_page_num = 1

    list_url = []
    for i in range(1, int(max_page_num) + 1):
        list_url.append(url + str(i) + '.html')

    return list_url


# 爬取页面获取图片详情页面
def spider_list_url(url: str = 'https://desk.zol.com.cn/dongman/2.html'):
    print(f'正在爬取图片详情页面：{url}')
    res = requests.get(url)
    res.encoding = 'gbk'
    et = etree.HTML(res.text)
    urls = et.xpath('//a[@class="pic"]/@href')
    del urls[0:2]
    page_url = []

    for item in urls:
        page_url.append(base_url + item)
    return page_url


if __name__ == '__main__':

    base_url = 'https://desk.zol.com.cn'
    list_url = []  # 所有分页变量
    page_url = []  # 所有页面的url
    img_url = []  # 所有图片的地址
    cate = spider_category()  # 获取分类
    with ThreadPoolExecutor(max_workers=20) as pool:
        for item in cate:
            list_url.extend(spider_page_num(item))
            # pool.submit(spider_page_num, item)

        for item in list_url:
            page_url.extend(spider_list_url(item))
            # pool.submit(spider_list_url, item)

        for item in page_url:
            img_url.extend(spider_img_url(item))
            # pool.submit(spider_img_url, item)

        for item in img_url:
            # down(item)
            pool.submit(down, item)

    print('图片下载完毕~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
