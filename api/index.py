import json
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from api.chatgpt import ChatGPT

line_bot_api = LineBotApi('GMnjt9VhQpe7tyyhI8GUHTzQNTG6BRpi5Ok/5h5x5JFlooXGlivVos2r4KjeEAnkWrvOyu/fsAY4ZXDdaPje7nHpzh+kOE4ezD7Bfjnv4UtsHKZxl3shoW2ifOb2ig3IkCZZZHb/I9lcV7M/ee7hqAdB04t89/1O/w1cDnyilFU=')
webhook_handler = WebhookHandler('7ff47a6cdaa8034d1f9ab26702b499d9')

app = Flask(__name__)
chatgpt = ChatGPT()

# domain root
@app.route('/')
def home():
    return 'LINE Bot API Server is running.'

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        webhook_handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# https://developers.line.biz/en/reference/messaging-api/#message-event
@webhook_handler.add(MessageEvent)
def handle_message(event):    
    print('[handle_message]', event)
    if event.message.type != "text":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="目前不支援文字以外的訊息喔"))
        return
    else:
        reply_msg = chatgpt.get_response(event.message.text)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_msg))
        return

if __name__ == "__main__":
    app.run()