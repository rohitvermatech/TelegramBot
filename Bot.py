import json
from Component import com

TG_Token = "your telegram token"


COM = com(TG_Token)


def echo(data):
    tdata = COM.parse(data)
    uid = tdata["uid"]
    text = tdata["text"]

    COM.sendmsg(uid, text)
