import json
from flask import Flask, request

app = Flask(__name__)

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

def get_users():
    with open("users.json") as f:
        users = json.load(f)
        return [User(**user) for user in users]

def get_user(id):
    users = get_users()
    for user in users:
        if user.id == id:
            return user
    return None

def add_user(user):
    users = get_users()
    users.append(user)
    with open("user.json", "w") as f:
        json.dump([user.__dict__ for user in users], f)

def update_user(user):
    users = get_users()
    for i, u in enumerate(users):
        if u.id == user.id:
            users[i] = user
    with open("users.json", "w") as f:
        json.dump([user.__dict__ for user in users], f)

def delete_user(id):
    users = get_users()
    users = [user for user in users if user.id != id]
    with open("users.json", "w") as f:
        json.dump([user.__dict__ for user in users], f)