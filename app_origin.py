from flask import Flask , render_template, request
from decouple import config
import requests
<<<<<<< HEAD
import random
import json 
=======
>>>>>>> 915dbac1090322285e3164ea263065ab8abad9cb

app = Flask(__name__)
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')
url = 'https://api.telegram.org/bot'

@app.route('/')
def hello():
    return "Hello World"

@app.route('/write')
def write():
    return render_template('write.html')
@app.route('/send')
def send():
    text = request.args.get('text')
    requests.get(f'{url}{token}/sendMessage?chat_id={chat_id}&text={text}')
    return render_template('send.html') 

<<<<<<< HEAD
@app.route(f'/{token}', methods=["POST"]) #post방식일때 무조건 실행. 아무나 못들어오게 토큰입력하고, post방식으로 들어오도록 함
def telegram():
    data=request.get_json()
    id=data['message']['chat']['id']
    message_text = data['message']['text']
    if message_text =="안녕":
        return_text = "안녕하세요"
    elif message_text == "로또":
        numbers = range(1,46)
        return_text = sorted(random.sample(numbers, 6)) # random.sample(변수, 갯수): 변수중에서 갯수만큼 뽑아줌
    else:
        headers = {
            "Host": "kapi.kakao.com",
            "Authorization": f"KakaoAK <키 입력>"
            
        }
        query= message_text
        response=requests.get(f'https://kapi.kakao.com/v1/translation/translate?src_lang=kr&target_lang=en&query={query}',headers=headers)
        response_text=response.json()['translated_text'][0][0]
        return_text = response_text
    requests.get(f'{url}{token}/sendMessage?chat_id={id}&text={return_text}')
    return "ok", 200


  
=======


>>>>>>> 915dbac1090322285e3164ea263065ab8abad9cb

if __name__ == ("__main__"):
    app.run(debug=True)