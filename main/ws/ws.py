"""Websocket routes"""

from flask_sock import Server

from .. import sock
from ..utils.encrypt import caesor_cipher


@sock.route("/caesor-cipher")
def ws_encrypt(ws: Server):
    ws.send("You are now connected.")
    ws.send("Please send number of steps to encrypt")
    while True:
        steps: str = ws.receive()
        if steps.isdigit():
            ws.send("Enter the text to be encrypted")
            text: str = ws.receive()
            ws.send(f"Encrypted text = {caesor_cipher(text, int(steps))}")
        ws.send("Please send number of steps to encrypt")
