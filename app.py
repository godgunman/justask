from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('GMnjt9VhQpe7tyyhI8GUHTzQNTG6BRpi5Ok/5h5x5JFlooXGlivVos2r4KjeEAnkWrvOyu/fsAY4ZXDdaPje7nHpzh+kOE4ezD7Bfjnv4UtsHKZxl3shoW2ifOb2ig3IkCZZZHb/I9lcV7M/ee7hqAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('7ff47a6cdaa8034d1f9ab26702b499d9')


@app.route("/", methods=['GET'])
def index():
    return "<p>This is a LINE Bot API Server!</p>"
    

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()