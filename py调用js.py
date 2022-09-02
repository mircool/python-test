import execjs
import requests

url = 'https://vipapi.qimingpian.cn/DataList/productListVip'
post_data = {"time_interval": "", "tag": "", "tag_type": "", "province": "", "lunci": "", "page": "1", "num": "20",
             "unionid": ""}

res = requests.post(url, data=post_data).json()

encrypt_data = res['encrypt_data']

with open('test.js') as f:
    js_code = f.read().strip()

ctx = execjs.compile(js_code).call('s', encrypt_data)
print(ctx)
