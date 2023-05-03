from api.chatgpt import ChatGPT

chatgpt = ChatGPT()

reply_msg = chatgpt.get_models()
print(reply_msg)


reply_msg = chatgpt.get_response("請問滷肉飯和肉燥飯哪裡不同?請用中文回答")
print(reply_msg)

reply_msg = chatgpt.get_response("請問炸醬麵和麻醬麵哪裡不同?請用中文回答")
print(reply_msg)

reply_msg = chatgpt.get_response("哪個熱量高呢?請用中文回答")
print(reply_msg)