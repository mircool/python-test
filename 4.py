import json
import re
import requests


res = requests.get('https://desk.zol.com.cn/bizhi/8726_107512_2.html')

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
