import uuid
from datetime import datetime
from tinydb import TinyDB, Query, operations, where

db = TinyDB('databases/bizcord.json')
usersTable = db.table('users')
roomsTable = db.table('rooms')

User = Query()
Room = Query()

def getUser(username):
	return usersTable.get(User.username == username)

def getUserBySessionToken(sessionToken):
	return usersTable.get(User.session_token == sessionToken)

def createUser(username):
	session_token = str(uuid.uuid1())

	newUser = {
		'id': str(uuid.uuid1()),
		'username': username,
		'session_token': session_token,
		'room_ids': []
	}
	usersTable.insert(newUser)

	return newUser

def getRooms():
	return roomsTable.search(Room.fragment({}))

def getRoom(room_id):
	return roomsTable.get(Room.id == room_id)

def createRoom(room_name):
	newUser = {
		'id': str(uuid.uuid1()),
		'name': room_name,
		'members': [],
		'room_ids': []
	}
	usersTable.insert(newUser)

	return newUser

def sendChatMessage(room_id, user_session_token, message):
	foundRoom = getRoom(room_id)
	author = getUserBySessionToken(user_session_token)
	messageObj = createMessageObject(author['id'], author['username'], message)
	roomsTable.update({"messages": foundRoom['messages'] + [messageObj]}, Room.id == room_id)
	return messageObj

def createMessageObject(authorId, authorName, body):
	return {
		'id': str(uuid.uuid1()),
		'authorId': authorId,
		'authorName': authorName,
		'body': body,
		'date': str(datetime.now())
	}

if len(roomsTable.search(Room.id == 'MAIN')) == 0:
	roomsTable.insert({
		'id': 'MAIN',
		'name': 'Main Lobby',
		'members': [],
		'messages': [createMessageObject('ADMIN', 'Admin', 'Welcome to the Main Lobby!')]
	})

	roomsTable.insert({
		'id': 'OTHER',
		'name': 'Other Lobby',
		'members': [],
		'messages': [createMessageObject('ADMIN', 'Admin', 'Welcome to the Other Lobby!')]
	})

	roomsTable.insert({
		'id': 'ANOTHER',
		'name': 'Another Lobby',
		'members': [],
		'messages': [createMessageObject('ADMIN', 'Admin', 'Welcome to Another Lobby!')]
	})