from flask import request, jsonify
from bson import ObjectId
from flasgger import swag_from
from app.models.teacher_model import TeacherModel
from app.models.teacher_detail_model import TeacherDetailModel
from app import mongo

teacher_model = TeacherModel(mongo)
teacher_detail_model = TeacherDetailModel(mongo)

def create_teacher():
    data = request.json
    print('tch--',data)
    # Save to teacher collection
    teacher_data = {
        "age": data["age"],
        "gender": data["gender"],
        "img": data["teacherImage"],
        "name": data["name"],
        "position": data["position"],
        "isActive": 1
    }
    teacher_id = teacher_model.create(teacher_data)

    # Save to teacher-detail collection
    teacher_detail_data = {
        "teacherId": teacher_id,
        "about": data["about"],
        "experience": data["experience"],
        "subject": data["subject"],
        "duty": data["duty"]
    }
    teacher_detail_model.create(teacher_detail_data)

    return jsonify({"message": "Teacher and details saved successfully"}), 201

def get_teachers():
    teachers = teacher_model.find({})  # Fetch all teachers
    if not teachers:
        return jsonify({'message': 'No teachers found'}), 404
    
    teachers_data = []
    for teacher in teachers:
        # Fetch teacher details using teacher_id
        teacher_details = teacher_detail_model.find_one({'teacherId': teacher['_id']})
        
        # Construct teacher data with details
        teacher_data = {
            '_id': str(teacher['_id']),
            'name': teacher['name'],
            'age': teacher['age'],
            'gender': teacher['gender'],
            'img': teacher['img'],
            'position': teacher['position'],
            'isActive': teacher['isActive']
        }
        
        if teacher_details:
            teacher_data.update({
                'about': teacher_details['about'],
                'experience': teacher_details['experience'],
                'subject': teacher_details['subject'],
                'duty': teacher_details['duty']
            })
        
        teachers_data.append(teacher_data)

    return jsonify(teachers_data), 200

def get_teacher(teacher_id):
        # Fetch teacher details
    teacher = teacher_model.find_one({'_id': ObjectId(teacher_id)})
    if not teacher:
        return jsonify({'error': 'Teacher not found'}), 404

    # Fetch teacher details using teacher_id
    teacher_details = teacher_detail_model.find_one({'teacherId': ObjectId(teacher_id)})
    if not teacher_details:
        return jsonify({'error': 'Teacher details not found'}), 404

    # Construct response data
    response_data = {
        '_id': str(teacher['_id']),
        'name': teacher['name'],
        'age': teacher['age'],
        'gender': teacher['gender'],
        'img': teacher['img'],
        'position': teacher['position'],
        'isActive': teacher['isActive'],
        'about': teacher_details['about'],
        'experience': teacher_details['experience'],
        'subject': teacher_details['subject'],
        'duty': teacher_details['duty']
    }

    return jsonify(response_data), 200

def update_teacher(teacher_id):
    data = request.json
    # Fetch teacher details
    teacher = teacher_model.find_one({'_id': ObjectId(teacher_id)})
    if not teacher:
        return jsonify({'error': 'Teacher not found'}), 404
    teacher_data = {
        'name': data['name'],
        'age': data['age'],
        'gender': data['gender'],
        'img': data['teacherImage'],
        'position': data['position']
    }
    teacher_detail_data = {
        'about': data['about'],
        'experience': data['experience'],
        'subject': data['subject'],
        'duty': data['duty']
    }
    result = teacher_model.update({'_id': ObjectId(teacher_id)}, teacher_data)
    teacher_detail_model.update({'teacherId': ObjectId(teacher['_id'])}, teacher_detail_data)
    return jsonify({'modified_count': result.modified_count}), 200

def delete_teacher(teacher_id):
    # Fetch teacher details
    teacher = teacher_model.find_one({'_id': ObjectId(teacher_id)})
    if not teacher:
        return jsonify({'error': 'Teacher not found'}), 404
    result = teacher_model.delete({'_id': ObjectId(teacher_id)})
    teacher_detail_model.delete({'teacherId': ObjectId(teacher['_id'])})
    return jsonify({'deleted_count': result.deleted_count}), 200
