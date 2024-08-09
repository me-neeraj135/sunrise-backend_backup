from flask import request, jsonify, current_app
from bson import ObjectId
from flasgger import swag_from
from app.models.user_model import UserModel
from app.models.testimonial_model import TestimonialModel
from app import mongo

testimonial_model = TestimonialModel(mongo)
user_model = UserModel(mongo)



def get_user_by_id(user_id):
    return user_model.find_one({"_id": user_id})



def create_testimonial():
    data = request.json
 
    
    testimonial_data= {
        # "user_id": user_id,
        "about": data['about'],
        "category":data ['category'],
        "date": data['date'],
        "img":data['img'],
        "title":data['title'],
        "userName":data['userName'],
        "isActive":data ['isActive'],
        
    }


 
    
    testimonial_id = testimonial_model.create(testimonial_data)
    return jsonify({"message": "testimonial created successfully", "testimonial_id": str(testimonial_id)}), 201

def get_testimonials():


    cursor = testimonial_model.find({})  # Querying MongoDB returns a cursor

    if not cursor:
        return jsonify({'message': 'No testimonials found'}), 404
    
    data = list(cursor)  # Convert cursor to a list
    
    # Convert ObjectId to string
    for document in data:
        document["_id"] = str(document["_id"])

    return jsonify(data)  # This will now work


def get_testimonial(testimonial_id):
    testimonial = testimonial_model.find_one({'_id': ObjectId(testimonial_id)})
    if not testimonial:
        return jsonify({'error': 'testimonial not found'}), 404

    testimonial['_id'] = str(testimonial['_id'])
    return jsonify(testimonial), 200

def update_testimonial(testimonial_id):
    data = request.json
    testimonial = testimonial_model.find_one({'_id': ObjectId(testimonial_id)})
    if not testimonial:
        return jsonify({'error': 'testimonial not found'}), 404

    testimonial_data = {
        
        "about": data['about'],
        "category":data ['category'],
        "date": data['date'],
        "img":data['img'],
        "title":data['title'],
        "userName":data['userName'],
        "isActive":data ['isActive'],
    }
    result = testimonial_model.update({'_id': ObjectId(testimonial_id)}, testimonial_data)
    
    if result.modified_count == 0:
        return jsonify({'error': 'testimonial update failed'}), 500
    
    return jsonify({'message': 'testimonial updated successfully'}), 200

def delete_testimonial(testimonial_id):
    result = testimonial_model.delete({'_id': ObjectId(testimonial_id)})
    if result.deleted_count == 0:
        return jsonify({'error': 'testimonial not found or delete failed'}), 404
    
    return jsonify({'message': 'testimonial deleted successfully'}), 200
