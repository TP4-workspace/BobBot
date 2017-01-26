#-*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from kakao_api import Message

app = Flask(__name__)

@app.route('/')
def index():
	return 'hello'

@app.route('/api/keyboard')
def keyboard():
	home_keyboard = Message.homeKeyboard()
	return jsonify(home_keyboard)

@app.route("/api/message", methods=["POST"])
def yellowMessage():
    message = Message.process(request.json)
    return jsonify(message), 200

@app.route("/api/friend", methods=["POST"])
def yellowFriendAdd():
    return 'success'


@app.route("/api/friend/<key>", methods=["DELETE"])
def yellowFriendBlock(key):
    return 'success'

@app.route("/api/chat_room/<key>", methods=["DELETE"])
def yellowExit(key):
	return 'success'

if __name__ == '__main__':
	app.run( host="0.0.0.0", port=80)
