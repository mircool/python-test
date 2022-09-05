import js2py
import requests

with open('企名科技.js', 'r', encoding='UTF-8') as file:
    js_code = file.read()

ctx = js2py.EvalJs()
ctx.execute(js_code)

url = 'https://vipapi.qimingpian.cn/DataList/productListVip'
post_data = {"time_interval": "", "tag": "", "tag_type": "", "province": "", "lunci": "", "page": "1", "num": "20",
             "unionid": ""}

res = requests.post(url, post_data)
encrypt_data = res.json()['encrypt_data']

data = ctx.s(encrypt_data)
print(data)
