import requests
import json


headers = {
            "Host": "kapi.kakao.com",
            "Authorization": "KakaoAK 7e6ebaf4ae41d1259b2ab492fc603254"
        }
query= "규현아 안녕 나는 멋진 남편이다"
        
response=requests.get(f'https://kapi.kakao.com/v1/translation/translate?src_lang=kr&target_lang=en&query={query}',headers=headers)        

response_text=response.json()['translated_text'][0][0]

print(response_text)