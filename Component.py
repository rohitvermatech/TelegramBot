import json
import requests


class com:
    def __init__(self, token):
        self.token = token

    def __chataction(self, uid, chat_action):

        r = requests.post("https://api.telegram.org/bot" + self.token + "/sendChatAction",
                          headers={"Content-Type": "application/json"},
                          data=json.dumps({
                              "chat_id": uid,
                              "action": chat_action
                          }))

    def sendmsg(self, uid, text, reply_markup=None):
        self.__chataction(uid, 'typing')
        if reply_markup is None:
            r = requests.post("https://api.telegram.org/bot" + self.token + "/sendMessage",
                              headers={"Content-Type": "application/json"},
                              data=json.dumps({
                                  "chat_id": uid,
                                  "text": text
                              }))
        else:
            r = requests.post("https://api.telegram.org/bot" + self.token + "/sendMessage",
                              headers={"Content-Type": "application/json"},
                              data=json.dumps({
                                  "chat_id": uid,
                                  "text": text,
                                  "reply_markup": reply_markup
                              }))

    def sendpic(self, uid, picurl, caption):

        r = requests.post("https://api.telegram.org/bot" + self.token + "/sendPhoto",
                          headers={"Content-Type": "application/json"},
                          data=json.dumps({
                              "chat_id": uid,
                              "photo": picurl,
                              "caption": caption
                          }))

    def parse(self, data):
        if 'my_chat_member' in data:
            pass
        elif 'callback_query' in data:
            message = data['callback_query']['data']
            uid = data['callback_query']['message']['chat']['id']
            fname = data['callback_query']['message']['chat']['first_name']
            lname = data['callback_query']['message']['chat']['last_name']
        else:
            message = data['message']['text']
            uid = data['message']['chat']['id']
            fname = data['message']['chat']['first_name']
            lname = data['message']['chat']['last_name']
        return {
            "uid": uid,
            "fname": fname,
            "lname": lname,
            "text": message
        }
