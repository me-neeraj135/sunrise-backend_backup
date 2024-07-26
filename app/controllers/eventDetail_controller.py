from flask import request, jsonify
from bson import ObjectId
from flasgger import swag_from
from app.models.eventDetail_model import EventDetailModel
from app import mongo

eventDetail_model = EventDetailModel(mongo)


def create_eventDetail():
    data = request.json
    eventDetail_data = {
      "eventId": data['eventId'],
      "about": data['about'],
      "highlight": data['highlight']
    }
    
    eventDetailId = eventDetail_model.create(eventDetail_data)
    return jsonify({"message": "Event detail created successfully", "eventContentId": str(eventDetailId)}), 201


def get_eventDetails():
    eventDetails = eventDetail_model.find({})
    if not eventDetails:
        return jsonify({'message': 'No eventDetails found'}), 404
    
    for eventDetail in eventDetails:
        eventDetail['_id'] = str(eventDetail['_id'])
    
    return jsonify(eventDetails), 200

def get_eventDetail(eventDetailId):
    eventDetail= eventDetail_model.find_one({'_id': ObjectId(eventDetailId)})
    if not eventDetail:
        return jsonify({'error': 'eventDetail not found'}), 404

    eventDetail['_id'] = str(eventDetail['_id'])
    return jsonify(eventDetail), 200


def update_eventDetail(eventDetailId):
    updated_data = request.json
    updating_eventDetail= eventDetail_model.find_one({'_id': ObjectId(eventDetailId)})
    if not updating_eventDetail:
        return jsonify({'error': 'Event detail not found'}), 404

    eventDetail_data = {

      "eventId": updated_data['eventId'],
      "about": updated_data['about'],
      "highlight": updated_data['highlight']

    }
    result = eventDetail_model.update({'_id': ObjectId(eventDetailId)}, eventDetail_data)
    
    
    if result.modified_count == 0:
        return jsonify({'error': 'Event detail update failed'}), 500
    
    return jsonify({'message': 'Event detail updated successfully'}), 200


def delete_eventDetail(eventDetailId):
    result = eventDetail_model.delete({'_id': ObjectId(eventDetailId)})
    if result.deleted_count == 0:
        return jsonify({'error': 'Event detail not found or delete failed'}), 404
    
    return jsonify({'message': 'Event detail deleted successfully'}), 200