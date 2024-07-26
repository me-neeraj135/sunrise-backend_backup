from flask import request, jsonify
from bson import ObjectId
from flasgger import swag_from
from app.models.class_model import  ClassModel
from app import mongo

class_model = ClassModel(mongo)


def create_class():
    data = request.json
    class_data = {
        "className": data["className"],
        "aboutClass": data["aboutClass"],
        "students": data["students"],
        "classUrl":data['classUrl']
    }
    
    class_id = class_model.create(class_data)
    return jsonify({"message": "Class created successfully", "class_id": str(class_id)}), 201


def get_classes():
    classes = class_model.find({})
    if not classes:
        return jsonify({'message': 'No classes found'}), 404
    
    for student_class in classes:
        student_class['_id'] = str(student_class['_id'])
    
    return jsonify(classes), 200

def get_class(class_id):
    student_class= class_model.find_one({'_id': ObjectId(class_id)})
    if not student_class:
        return jsonify({'error': 'Class not found'}), 404

    student_class['_id'] = str(student_class['_id'])
    return jsonify(student_class), 200


def update_class(class_id):
    updated_data = request.json
    updating_class= class_model.find_one({'_id': ObjectId(class_id)})
    if not updating_class:
        return jsonify({'error': 'Class not found'}), 404

    class_data = {
        "className": updated_data["className"],
        "aboutClass": updated_data["aboutClass"],
        "students": updated_data["students"],
        "classUrl":updated_data['classUrl']

    }
    result = class_model.update({'_id': ObjectId(class_id)}, updated_data)
    
    
    if result.modified_count == 0:
        return jsonify({'error': 'Class update failed'}), 500
    
    return jsonify({'message': 'Class updated successfully'}), 200


def delete_class(class_id):
    result = class_model.delete({'_id': ObjectId(class_id)})
    if result.deleted_count == 0:
        return jsonify({'error': 'Class not found or delete failed'}), 404
    
    return jsonify({'message': 'Class deleted successfully'}), 200