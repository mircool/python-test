# coding:utf-8
import requests

# import subprocess
# from functools import partial
#
# subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs

import js2py

url = 'https://vipapi.qimingpian.cn/DataList/productListVip'
post_data = {"time_interval": "",
             "tag": "",
             "tag_type": "",
             "province": "",
             "lunci": "",
             "page": "1",
             "num": "20",
             "unionid": ""}

res = requests.post(url, data=post_data).json()

encrypt_data = res['encrypt_data']

with open('test.js', encoding='utf-8', errors='replace') as f:
    js_code = f.read()

# js_code = open('test.js').read()
# js_code = open('test.js', 'rb').read().decode('gb18030', 'replace')

# ctx = execjs.compile(js_code).call('s', encrypt_data)
# print(ctx)

context = js2py.EvalJs()
context.execute(js_code)
result = context.s(encrypt_data)
print(result)
