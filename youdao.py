import requests
from hashlib import md5
import time
import random


# md5加密
def encrypt_md5(s):
    # 创建md5对象
    new_md5 = md5()
    # 这里必须用encode()函数对字符串进行编码，不然会报 TypeError: Unicode-objects must be encoded before hashing
    new_md5.update(s.encode(encoding='utf-8'))
    # 加密
    return new_md5.hexdigest()


def get_cookie():
    res = requests.get('https://fanyi.youdao.com/')
    return res.cookies


def main():
    url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    session = requests.Session()

    head = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "DNT": "1",
        "Host": "fanyi.youdao.com",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47",
        "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Microsoft Edge\";v=\"104\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }

    res_home = session.get('https://fanyi.youdao.com/', headers=head)
    # cookies = res_home.cookies.get_dict()
    # session.headers.update('Cookie',)
    # session.cookies.set('OUTFOX_SEARCH_USER_ID', cookies['OUTFOX_SEARCH_USER_ID'])
    # print(cookies['OUTFOX_SEARCH_USER_ID'])
    # return False

    input_text = input('请输入要翻译的内容')
    t = time.time()
    lts = int(round(t * 1000))
    salt = str(lts) + str(random.randint(0, 9))
    bv = encrypt_md5(
        "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47")
    sign = encrypt_md5("fanyideskweb" + input_text + salt + "Ygy_4c=r#e#4EX^NUGUc5")

    data = {
        "i": input_text,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": sign,
        "lts": lts,
        "bv": bv,
        "doctype": "json",
        "version": 2.1,
        "keyfrom": "fanyi.web",
        "action": "FY_BY_CLICKBUTTION",
    }
    res = session.post(url=url, data=data, headers=head)
    print(res.json())
    # print(res.cookies)


if __name__ == '__main__':
    main()
