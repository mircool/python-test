import time
import execjs
import requests

token = 'a7d612dd821a14118f7adfef11b08c4e'
g = '12574478'
data = '{"cid":"TpFacRecommendService:TpFacRecommendService","methodName":"execute","params":"{\"pageNo\":\"1\",\"cna\":\"/CG6Gg0qawACASeCGC1NUGVc\",\"pageSize\":\"20\",\"from\":\"PC\",\"sort\":\"mix\",\"trafficSource\":\"pc_index_recommend\",\"url\":\"https://sale.1688.com/factory/home.html?spm=a260k.dacugeneral.searchbox.2.663335e44vSGCA\"}"}'

i = str(time.time() * 1000).split('.')[0]

sign_key = token + "&" + i + "&" + g + "&" + data

with open('1688.js', encoding='utf-8') as f:
    js_code = f.read()

ctx = execjs.compile(js_code)

sign = ctx.call('h', sign_key)

url = 'https://h5api.m.1688.com/h5/mtop.taobao.widgetservice.getjsoncomponent/1.0/?'

params = {"jsv": "2.6.1",
          "appKey": g,
          "t": i,
          "sign": sign,
          "v": "1.0", "type": "jsonp", "isSec": "0", "timeout": "20000",
          "api": "mtop.taobao.widgetService.getJsonComponent", "dataType": "jsonp", "jsonpIncPrefix": "mboxfc",
          "callback": "mtopjsonpmboxfc1",
          "data": data
          }

head = {"accept":"*/*","accept-encoding":"gzip, deflate, br","accept-language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","cookie":"cna=/CG6Gg0qawACASeCGC1NUGVc; _m_h5_tk=a7d612dd821a14118f7adfef11b08c4e_1662200125005; _m_h5_tk_enc=8384e1227509a641b269134fde571c7e; lid=ynyjyhc; cookie2=16502bdf27eb9ed15e59be5ed89d60c0; sgcookie=E10084LIx1vPPIpfW0MKh1%2B%2BzUj0xYHaL%2FswmKEUMEqUzAEYs6d%2Fim1QjfJTqVIADtBXXnh2ugGANMma7thOsmtIKC1ZQmuLsdWCYe7xZrB1nN2Ouof8ftLgBRiGuvkF4ENV; t=0ed03861f53521885ea6261aa7b22e34; _tb_token_=733313eef1e75; __cn_logon__=false; alicnweb=touch_tb_at%3D1662195549633; l=eB_9BZCqLXUsXv4JBOfwourza77OSIRAguPzaNbMiOCPOefk5JIOW6kmwHTDC3GVhsgBR3k0hWaBBeYBqQd-nxvOc7DZWVHmn; isg=BP__jumUoCVHCaWjKnzXeynojtOJ5FOGA3p9IJHMm670oB8imbTj1n224nBe-Cv-","dnt":"1","referer":"https://sale.1688.com/","sec-ch-ua":"\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Microsoft Edge\";v=\"104\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\"","sec-fetch-dest":"script","sec-fetch-mode":"no-cors","sec-fetch-site":"same-site","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47"}

res = requests.get(url=url, headers=head, params=params)

print(res.text)
