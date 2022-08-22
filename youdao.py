import requests
from hashlib import md5
import time
import random


def encrypt_md5(s):
    # 创建md5对象
    new_md5 = md5()
    # 这里必须用encode()函数对字符串进行编码，不然会报 TypeError: Unicode-objects must be encoded before hashing
    new_md5.update(s.encode(encoding='utf-8'))
    # 加密
    return new_md5.hexdigest()


def main():
    url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"
    }
    input_text = input('请输入要翻译的内容')
    t = time.time()
    lts = int(round(t * 1000))
    salt = str(lts) + str(random.randint(0, 9))
    bv = encrypt_md5(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63')
    sign = encrypt_md5("fanyideskweb" + input_text + salt + "Ygy_4c=r#e#4EX^NUGUc5")

    data = {
        "i": input_text,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": int(salt),
        "sign": sign,
        "lts": lts,
        "bv": bv,
        "doctype": "json",
        "version": 2.1,
        "keyfrom": "fanyi.web",
        "action": "FY_BY_CLICKBUTTION",
    }
    res = requests.post(url=url, data=data, headers=head)
    print(res.json())
    # print(data)


if __name__ == '__main__':
    main()
