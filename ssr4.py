import pandas as pd
import urllib3
from bs4 import BeautifulSoup
import requests

global url_list, title_list, theme_list, score_list, content_list
urllib3.disable_warnings()  # 去除因为网页没有ssl证书出现的警告
url, title, theme, score, content = [], [], [], [], []
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/87.0.4280.141 Safari/537.36'}
the_url = 'https://ssr4.scrape.center/page/1'
html = requests.get(the_url, headers=headers, verify=False, timeout=15)
soup = BeautifulSoup(html.content, 'lxml')
url_list = soup.find_all(class_='name')
for x in url_list:
    url.append('https://ssr1.scrape.center' + x['href'])
for a in url:
    html = requests.get(a, headers=headers, verify=False, timeout=15)
    soup = BeautifulSoup(html.content, 'lxml')
    title_list = soup.find_all(class_='m-b-sm')
    theme_list = soup.find_all(class_='categories')
    score_list = soup.find_all(class_='score m-t-md m-b-n-sm')
    content_list = soup.find_all("div", class_='drama')
    for y, z, i, x in zip(title_list, theme_list, score_list, content_list):
        title.append(y.text)
        theme.append(z.text.replace('','').replace('',''))
        score.append(i.text.strip())
        content.append(x.text.replace('剧情简介', '').replace('','').replace('','').strip())
        bt = {
            '链接': url,
            '标题': title,
            '主题': theme,
            '评分': score,
            '剧情简介': content
        }
        work = pd.DataFrame(bt)
        work.to_csv('work.csv')
