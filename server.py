from flask import Flask, render_template, send_from_directory, request, make_response
from flask_sock import Sock
from components.user_database import getUser, createUser, getUserBySessionToken, sendChatMessage, getRooms, getRoom
import json

app = Flask(__name__)
sock = Sock(app)

clients = {}

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/static/<path:path>')
def send_static(path):
	return send_from_directory('static', path)

# Session Route (GET)

# Login Route (POST)

# Get All Rooms route (GET)

# Get Room by ID route (GET)

# WebSockets server
@sock.route('/ws')
def socketServer(ws):
	while True:
		data = ws.receive()

if __name__ == "__main__":
	app.run(debug=True)