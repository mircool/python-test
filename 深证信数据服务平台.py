# -*- coding: utf-8 -*-
import requests
import time
import base64

url = 'http://webapi.cninfo.com.cn/api/sysapi/p_sysapi1007'

mcode = base64.b64encode(str(round(time.time())).encode('UTF-8'))

header = {
    "mcode": mcode,
    "Referer": "http://webapi.cninfo.com.cn/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47",
}

data = {
    'tdate': '2022-09-02',
    'market': 'SZE'
}

res = requests.post(url=url, headers=header, data=data)

print(res.json())
