# coding:utf-8
import requests
import js2py

url = 'https://vipapi.qimingpian.cn/DataList/productListVip'
head = {"Accept": "application/json, text/plain, */*", "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6", "Connection": "keep-alive",
        "Content-Length": "69", "Content-Type": "application/x-www-form-urlencoded", "DNT": "1",
        "Host": "vipapi.qimingpian.cn", "Origin": "https://qimingpian.cn",
        "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Microsoft Edge\";v=\"104\"",
        "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\"", "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47"}

post_data = {"time_interval": "",
             "tag": "",
             "tag_type": "",
             "province": "",
             "lunci": "",
             "page": "1",
             "num": "20",
             "unionid": ""
             }

res = requests.post(url=url, headers=head, data=post_data).json()

encrypt_data = res['encrypt_data']

with open('test.js', encoding='utf-8', errors='replace') as f:
    js_code = f.read()

context = js2py.EvalJs()
context.execute(js_code)
result = context.s(encrypt_data)
print(result)
