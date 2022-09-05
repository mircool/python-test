import requests
import js2py

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

header = {
    "Accept": "*/*", "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Acs-Token": "1662274986285_1662362186261_PZ9RGDfoZT611QxcCOPF8OFKwuWbo2SxPixIRvRUghgbpBmit7Q8RU37MFpD3ROjRVnTIpUFvddu8d1NJ3mhUML6gqU8khO1c0MsFNnb2FSmg9pyPL8CJiZVxa0nuxIqB/9+IxoebB/9Cl3TaKfsCTE86UKcjKpJ7d25bMzgsjRV+3l73gHCIGrApRNJ8tIvQg5+1NceKO3xf5KhexBi17369vTRMkdjDqi2jTjuEd1rj2MQiN2nQt036UWOGB59Jcun5fx/iYuvD6VSQthvZ2oEIzZS9qlEDzO1jFA+0wkuIqa2/atR5dUPBIYi2rSimuKB6Td/GtfEcH1UebHObw==",
    "Connection": "keep-alive", "Content-Length": "135",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "BIDUPSID=3A2E4275BFF19D05AC652BAA013B87B0; PSTM=1653033098; BDUSS=HZkbmFnMDZqaEMwVFdTaWJPS0lGakVlNlBtWUVvSn5KTWhHQ0wxbjlyQ2EwYmRpSVFBQUFBJCQAAAAAAAAAAAEAAABNDIoCeW55anl6AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJpEkGKaRJBiO; BDUSS_BFESS=HZkbmFnMDZqaEMwVFdTaWJPS0lGakVlNlBtWUVvSn5KTWhHQ0wxbjlyQ2EwYmRpSVFBQUFBJCQAAAAAAAAAAAEAAABNDIoCeW55anl6AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJpEkGKaRJBiO; BAIDUID=3B0676F3C3C6A39C0BC47AA17C823D9C:SL=0:NR=10:FG=1; ZFY=:Bx94m:BwNUO7S6STrM:BjeXgUB9XU0:AwC9mR213:Agw5BY:C; BAIDU_WISE_UID=wapp_1654312882717_836; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; BAIDUID_BFESS=3B0676F3C3C6A39C0BC47AA17C823D9C:SL=0:NR=10:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1659772639,1662361123; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1662361123",
    "DNT": "1", "Host": "fanyi.baidu.com", "Origin": "https://fanyi.baidu.com",
    "Referer": "https://fanyi.baidu.com/",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"105\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"105\"",
    "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\"", "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27",
    "X-Requested-With": "XMLHttpRequest"
}

with open('百度翻译.js', encoding='utf-8') as f:
    js_code = f.read()

context = js2py.EvalJs()
context.execute(js_code)

input_data = input('请输入英文关键词')

sign = context.b(input_data)

data = {
    "from": "en",
    "to": "zh",
    "query": input_data,
    "transtype": "realtime",
    "simple_means_flag": "3",
    "sign": sign,
    "token": "ca15820cd95af050bc6b9a76968e7b9c",
    "domain": "common"
}

res = requests.post(url=url, headers=header, data=data)

print(res.json())
