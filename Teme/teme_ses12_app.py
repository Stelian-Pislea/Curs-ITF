import json
from flask import Flask, request, jsonify
from Teme.teme_ses12 import User

app = Flask(__name__)

repo = User("users.json")

@app.route("users", methods=["GET"])
def get_users():
    users = get_user()
    return {"users": [user.__dict__ for user in users]}

@app.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    user = get_user(id)
    if user:
        return user.__dict__
    else:
        return 'Error, user not found', 404

@app.route("/user", methods=["POST"])
def add_user():
    user = User(**request.json)
    add_user(user)
    return "OK", 201

@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    user = get_user(id)
    if user:
        update_user(User(id, **request.json))
    else:
        return 'Error, user not found', 404

@app.route("/users.json/<int:id>", methods=["DELETE"])
def delete_user(id):
    users = get_users()
    users = [user for user in users if user.id != id]
    with open("users.json", "w") as f:
        json.dump([user.__dict__ for user in users], f)
    return jsonify({"OK"}), 200

if __name__ == '__main__':
    app.run(debug=True)