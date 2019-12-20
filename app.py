from flask import Flask, render_template, request
from decouple import config
from bs4 import BeautifulSoup
import random
import requests

app = Flask(__name__)

token =config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')
url = "https://api.telegram.org/bot"
 #보이지 않는 파일을 만들면 다른 파일에 있는 변수를 사용할 수 있는건가?

@app.route('/')
def hello():

    return "Hello World"

@app.route('/write')
def write() :
    return render_template('write.html')

@app.route('/send')
def send() :
    text = request.args.get('text') 
    requests.get(f'{url}{token}/sendMessage?chat_id={chat_id}&text={text}')
    return render_template('send.html')

# @app.route(f'/{token}', methods=["POST"])
#     #token으로 복잡하게 사용하기 위해서 넣음
# def telegram():
#     data=request.get_json()
#     chat_id = data['message']['chat']['id']
#     text = data['message']['text']
#     # chat_id = request.get_json.[][][]
#     #if text =="로또" :
#       #보낸 사람에게 보내는 방법 getupdats <- 정보가 쌓이는 곳
#     # url1=f'https://kapi.kakao.com/v1/translation/translate?src_lang=kr&target_lang=en&query={text}'
    
#     # Authorization : "7e6ebaf4ae41d1259b2ab492fc603254"
#     # if text == "안녕":
#     #     return_text = "안녕하세요."
#     # elif text == "로또":
#     #     numbers = range(1,46)
#     #     return_text = sorted(random.sample(numbers, 6))
#     # elif text =="코스피":
#     #         req = requests.get("https://finance.naver.com/sise/sise_index.nhn?code=KOSPI").text
#     #         soup =BeautifulSoup(req, 'html.parser')
#     #         kospi = soup.select_one("#now_value").text
#     #         return_text = kospi 
    

#     # else :
#     #     return_text ="지금 지원하는 채팅은 안녕입니다."
    
#     requests.get(f'{url}{token}/sendMessage?chat_id={chat_id}&text={return_text}')
#     return "ok ", 200
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
    elif text =="코스피":
         req = requests.get("https://finance.naver.com/sise/sise_index.nhn?code=KOSPI").text
            soup =BeautifulSoup(req, 'html.parser')
            kospi = soup.select_one("#now_value").text
            return_text = kospi 

    else:
        headers = {
            "Host": "kapi.kakao.com",
            "Authorization": f"KakaoAK 7e6ebaf4ae41d1259b2ab492fc603254"
            
        }
        query= message_text
        response=requests.get(f'https://kapi.kakao.com/v1/translation/translate?src_lang=kr&target_lang=en&query={query}',headers=headers)
        response_text=response.json()['translated_text'][0][0]
        return_text = response_text
    requests.get(f'{url}{token}/sendMessage?chat_id={id}&text={return_text}')
    return "ok", 200


#chat_id 단순히 내 텔레그램으로 보는 내용

    
if __name__ == ("__main__"):
    app.run(debug=True)