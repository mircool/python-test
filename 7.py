import requests
import re
import json


def main(url: str = 'https://www.bilibili.com/video/BV1KZ4y1e7cG'):
    res = requests.get(url)
    obj = re.compile('window.__INITIAL_STATE__=(?P<json>.*?);\(function', re.S)
    res_json = obj.search(res.text).group('json')
    res_dict = json.loads(res_json)
    aid = res_dict['aid']
    bvid = res_dict['bvid']
    mid = res_dict['videoData']['owner']['mid']
    cid = res_dict['videoData']['cid']




if __name__ == '__main__':
    main()
