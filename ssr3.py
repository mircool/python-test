import requests

session = requests.session()

res = session.get('https://admin:admin@ssr3.scrape.center/')

print(res.text)
