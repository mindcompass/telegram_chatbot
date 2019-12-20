from decouple import config
import requests
token = config('TELEGRAM_BOT_TOKEN')
url = "https://api.telegram.org/bot"
paw_url = "https://kyuhyunkang.pythonanywhere.com"

data= requests.get(f'{url}{token}/setwebhook?url={paw_url}/{token}')
# 텔레그램에서 수행했던 결과를 FLASK임시 서버에 연동시는 것
print(data.text)