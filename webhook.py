from decouple import config
import requests
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')
url = "https://api.telegram.org/bot"
ngrok_url = "https://653b8546.ngrok.io"

data= requests.get(f'{url}{token}/setwebhook?url={ngrok_url}/{token}')
# 웹훅을 설정하기 위해서 ngrok
print(data)