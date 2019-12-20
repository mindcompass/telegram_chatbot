from flask import Flask, render_template,request
from decouple import config
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

#chat_id 단순히 내 텔레그램으로 보는 내용

    
if __name__ == ("__main__"):
    app.run(debug=True)