import requests
import re

if __name__ == '__main__':
    url = 'https://movie.douban.com/top250'
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77'
    }
    resq = requests.get(url, headers=head)
    resq.encoding = 'utf-8'
    html = resq.text
    obj = re.compile(
        r'<div class="item">.*?<span class="title">(?P<title>.*?)'
        r'</span>.*?<br>(?P<year>.*?)&nbsp;/&nbsp;.*?'
        r'<span class="rating_num" property="v:average">(?P<rating>.*?)</span>',
        re.S)
    result = obj.finditer(html)
    for item in result:
        dic = item.groupdict()
        dic['year'] = dic['year'].strip()
        print(dic)
