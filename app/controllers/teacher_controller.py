from flask import request, jsonify
from bson import ObjectId
from flasgger import swag_from
from ..models.teacher_model import TeacherModel
from .. import mongo

teacher_model = TeacherModel(mongo)

@swag_from('../../swagger/create_teacher.yml')
def create_teacher():
    data = request.json
    teacher_id = teacher_model.create(data)
    return jsonify({'id': str(teacher_id)}), 201

@swag_from('../../swagger/get_teachers.yml')
def get_teachers():
    teachers = teacher_model.find({})
    return jsonify([{
        '_id': str(teacher['_id']),
        'name': teacher['name'],
        'age': teacher['age'],
        'gender': teacher['gender'],
        'img': teacher['img'],
        'position': teacher['position']
    } for teacher in teachers]), 200

@swag_from('../../swagger/get_teacher.yml')
def get_teacher(teacher_id):
    teacher = teacher_model.find_one({'_id': ObjectId(teacher_id)})
    if teacher:
        return jsonify({
            '_id': str(teacher['_id']),
            'name': teacher['name'],
            'age': teacher['age'],
            'gender': teacher['gender'],
            'img': teacher['img'],
            'position': teacher['position']
        }), 200
    return jsonify({'error': 'Teacher not found'}), 404

@swag_from('../../swagger/update_teacher.yml')
def update_teacher(teacher_id):
    data = request.json
    result = teacher_model.update({'_id': ObjectId(teacher_id)}, data)
    return jsonify({'modified_count': result.modified_count}), 200

@swag_from('../../swagger/delete_teacher.yml')
def delete_teacher(teacher_id):
    result = teacher_model.delete({'_id': ObjectId(teacher_id)})
    return jsonify({'deleted_count': result.deleted_count}), 200
