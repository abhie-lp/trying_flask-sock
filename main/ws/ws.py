"""Websocket routes"""

from json import dumps, loads, JSONDecodeError
from flask_sock import Server

from .. import sock
from ..utils.encrypt import caesar_cipher


@sock.route("/caesar-cipher")
def ws_encrypt(ws: Server):
    ws.send("You are now connected with the server.")
    ws.send("Send steps and text as json.")
    while True:
        data = ws.receive()
        try:
            json: dict = loads(data)
        except JSONDecodeError:
            ws.send("JSON not formatted")
        else:
            if "steps" in json and "text" in json:
                if isinstance(json["steps"], int) or json["steps"].isdigit():
                    result = {"encrypt": caesar_cipher(json["text"],
                                                       int(json["steps"]))}
                    ws.send(dumps(result))
                else:
                    ws.send("Steps is not a valid integer.")
            else:
                if "steps" not in json:
                    ws.send("steps not present JSON.")
                if "text" not in json:
                    ws.send("text not present in JSON.")
