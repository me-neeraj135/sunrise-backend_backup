from flask import request, jsonify
from bson import ObjectId
from flasgger import swag_from
from app.models.classDetail_model import ClassDetailModel
from app import mongo

classDetail_model = ClassDetailModel(mongo)


def create_classDetail():
    data = request.json
    print('')

    classDetail_data = {
        "className": data["className"],
        "aboutClass": data["aboutClass"],
        "subjects": data['subjects'],
        
    }
    
    classDetail_id = classDetail_model.create(classDetail_data)
    
    return jsonify({"message": "Class-detail created successfully", "class_id": str(classDetail_id)}), 201


def get_classesDetail():
    classesDetail = classDetail_model.find({})
    if not classesDetail:
        return jsonify({'message': 'No classes-detail found'}), 404
    
    for classDetail in classesDetail:
        classDetail['_id'] = str(classDetail['_id'])
    
    return jsonify(classesDetail), 200

def get_classDetail(classDetail_id):
   
    classDetail= classDetail_model.find_one({'_id': ObjectId(classDetail_id)})
    
    if not classDetail:
        return jsonify({'error': 'Class-detail not found'}), 404

    classDetail['_id'] = str(classDetail['_id'])
    return jsonify(classDetail), 200


def update_classDetail(classDetail_id):
    data= request.json
    updating_classDetail= classDetail_model.find_one({'_id': ObjectId(classDetail_id)})
    if not updating_classDetail:
        return jsonify({'error': 'Class-detail not found'}), 404

    classDetail_data = {
        "className": data["className"],
        "aboutClass": data["aboutClass"],
        "subjects": data["subjects"],
        

    }
    result = classDetail_model.update({'_id': ObjectId(classDetail_id)}, classDetail_data)
    
    
    if result.modified_count == 0:
        return jsonify({'error': 'Class-detail update failed'}), 500
    
    return jsonify({'message': 'Class-detail updated successfully'}), 200


def delete_classDetail(classDetail_id):
    result = classDetail_model.delete({'_id': ObjectId(classDetail_id)})
    if result.deleted_count == 0:
        return jsonify({'error': 'Class-detail not found or delete failed'}), 404
    
    return jsonify({'message': 'Class-detail deleted successfully'}), 200