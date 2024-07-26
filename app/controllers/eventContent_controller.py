from flask import request, jsonify
from bson import ObjectId
from flasgger import swag_from
from app.models.eventContent_model import EventContentModel
from app import mongo

eventContent_model = EventContentModel(mongo)


def create_eventContent():
    data = request.json
    eventContent_data = {
        
        "eventId": data['eventId'],
        "label": data['label']
    
    }
    
    eventContentId = eventContent_model.create(eventContent_data)
    return jsonify({"message": "Event content created successfully", "eventContentId": str(eventContentId)}), 201


def get_eventContents():
    eventContents = eventContent_model.find({})
    if not eventContents:
        return jsonify({'message': 'No eventContents found'}), 404
    
    for eventContent in eventContents:
        eventContent['_id'] = str(eventContent['_id'])
    
    return jsonify(eventContents), 200

def get_eventContent(eventContentId):
    eventContent= eventContent_model.find_one({'_id': ObjectId(eventContentId)})
    if not eventContent:
        return jsonify({'error': 'eventContent not found'}), 404

    eventContent['_id'] = str(eventContent['_id'])
    return jsonify(eventContent), 200


def update_eventContent(eventContentId):
    updated_data = request.json
    updating_eventContent= eventContent_model.find_one({'_id': ObjectId(eventContentId)})
    if not updating_eventContent:
        return jsonify({'error': 'Event content not found'}), 404

    eventContent_data = {
        
        "eventId": updated_data['eventId'],
        "label": updated_data['label']

    }
    result = eventContent_model.update({'_id': ObjectId(eventContentId)}, eventContent_data)
    
    
    if result.modified_count == 0:
        return jsonify({'error': 'Event content update failed'}), 500
    
    return jsonify({'message': 'Event content updated successfully'}), 200


def delete_eventContent(eventContentId):
    result = eventContent_model.delete({'_id': ObjectId(eventContentId)})
    if result.deleted_count == 0:
        return jsonify({'error': 'Event content not found or delete failed'}), 404
    
    return jsonify({'message': 'Event content deleted successfully'}), 200