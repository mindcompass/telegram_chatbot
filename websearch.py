import requests
import json

url = "https://dapi.kakao.com/v2/search/web"
queryString ={"query":"류현진"}
header ={'authorization': '7e6ebaf4ae41d1259b2ab492fc603254'}
r = requests.get(url, headers=header, params=queryString)
print(json.loads(r.text))