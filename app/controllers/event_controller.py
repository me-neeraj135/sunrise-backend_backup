from flask import request, jsonify
from bson import ObjectId
from flasgger import swag_from
from app.models.event_model  import EventModel
from app import mongo

event_model = EventModel(mongo)


def create_event():
    data = request.json
    event_data = {
        "title": data['title'],
        "location": data['location'],
        "img":data['img'],
        "startTime": data['startTime'],
        "endTime":data['endTime'],
        "startDate":data['startDate'],
        "endDate":data['endDate'],
        "year": data['year'],
        "teacherId": data['teacherId']

    }
    
    eventId = event_model.create(event_data)
    return jsonify({"message": "Event created successfully", "eventId": str(eventId)}), 201


def get_events():
    events = event_model.find({})
    if not events:
        return jsonify({'message': 'No events found'}), 404
    
    for event in events:
        event['_id'] = str(event['_id'])
    
    return jsonify(events), 200

def get_event(eventId):
    event= event_model.find_one({'_id': ObjectId(eventId)})
    if not event:
        return jsonify({'error': 'Event not found'}), 404

    event['_id'] = str(event['_id'])
    return jsonify(event), 200


def update_event(eventId):
    updated_data = request.json
    updating_event= event_model.find_one({'_id': ObjectId(eventId)})
    if not updating_event:
        return jsonify({'error': 'Event not found'}), 404

    event_data = {
        "title": updated_data['title'],
        "location": updated_data['location'],
        "img":updated_data['img'],
        "startTime": updated_data['startTime'],
        "endTime":updated_data['endTime'],
        "startDate":updated_data['startDate'],
        "endDate":updated_data['endDate'],
        "year": updated_data['year'],
        "teacherId": updated_data['teacherId']
       

    }
    result = event_model.update({'_id': ObjectId(eventId)}, event_data)
    
    
    if result.modified_count == 0:
        return jsonify({'error': 'Event update failed'}), 500
    
    return jsonify({'message': 'Event updated successfully'}), 200


def delete_event(eventId):
    result = event_model.delete({'_id': ObjectId(eventId)})
    if result.deleted_count == 0:
        return jsonify({'error': 'Event not found or delete failed'}), 404
    
    return jsonify({'message': 'Event deleted successfully'}), 200