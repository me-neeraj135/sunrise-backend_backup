from flask import request, jsonify
from bson import ObjectId
from flasgger import swag_from
from app.models.user_model import UserModel
from app import mongo

user_model = UserModel(mongo)

def create_user():
    data = request.json
    user_data = {
        "firstName": data["firstName"],
        "lastName": data["lastName"],
        "mobile": data["mobile"],
        "email": data["email"],
        "password": data["password"],
        "userType": data["userType"],
        "IsActive": 1
    }
    user_id = user_model.create(user_data)
    return jsonify({"message": "User created successfully", "user_id": str(user_id)}), 201

def get_users():
    users = user_model.find({})
    if not users:
        return jsonify({'message': 'No users found'}), 404
    
    for user in users:
        user['_id'] = str(user['_id'])
    
    return jsonify(users), 200

def get_user(user_id):
    user = user_model.find_one({'_id': ObjectId(user_id)})
    if not user:
        return jsonify({'error': 'User not found'}), 404

    user['_id'] = str(user['_id'])
    return jsonify(user), 200

def update_user(user_id):
    data = request.json
    user = user_model.find_one({'_id': ObjectId(user_id)})
    if not user:
        return jsonify({'error': 'User not found'}), 404

    user_data = {
        "firstName": data["firstName"],
        "lastName": data["lastName"],
        "mobile": data["mobile"],
        "email": data["email"],
        "password": data["password"],
        "userType": data["userType"],
        "IsActive": data.get("IsActive", 1)
    }
    result = user_model.update({'_id': ObjectId(user_id)}, user_data)
    
    if result.modified_count == 0:
        return jsonify({'error': 'User update failed'}), 500
    
    return jsonify({'message': 'User updated successfully'}), 200

def delete_user(user_id):
    result = user_model.delete({'_id': ObjectId(user_id)})
    if result.deleted_count == 0:
        return jsonify({'error': 'User not found or delete failed'}), 404
    
    return jsonify({'message': 'User deleted successfully'}), 200
