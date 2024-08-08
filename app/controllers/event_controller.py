from flask import request, jsonify
from bson import ObjectId
from flasgger import swag_from
from app.models.event_model  import EventModel
from app.models.eventDetail_model import EventDetailModel
 
from app import mongo

event_model = EventModel(mongo)


def create_event():
    data = request.json
    print('evt-data--',data)
    event_data = {
        "title": data['eventTitle'],
        "organizerName":data['organizerName'],
        "location": data['eventAddress'],
        "img":data['eventImage'],
        "startTime": data['startTime'],
        "endTime":data['endTime'],
        "startDate":data['startDate'],
        "endDate":data['endDate'],
        "year": data['eventYear'],
      "about": data['aboutEvent'],
      "highlight": data['eventHighLight'],
      "label": data['eventLabel'],
      "isActive":data['isActive']
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
        "title": updated_data['eventTitle'],
        "organizerName":updated_data['organizerName'],
        "location": updated_data['eventAddress'],
        "img":updated_data['eventImage'],
        "startTime": updated_data['startTime'],
        "endTime":updated_data['endTime'],
        "startDate":updated_data['startDate'],
        "endDate":updated_data['endDate'],
        "year": updated_data['eventYear'],
      "about": updated_data['aboutEvent'],
      "highlight": updated_data['eventHightLight'],
      "label": updated_data['eventLabel'],
      "isActive":updated_data['isActive']
       

    }
    result = event_model.update({'_id': ObjectId(eventId)}, event_data)
    
    
    if result.modified_count == 0:
        return jsonify({'error': 'Event update failed'}), 500
    
    return jsonify({'message': 'Event updated successfully',"updatedEvent":result}), 200


def delete_event(eventId):
    result = event_model.delete({'_id': ObjectId(eventId)})
    if result.deleted_count == 0:
        return jsonify({'error': 'Event not found or delete failed'}), 404
    
    return jsonify({'message': 'Event deleted successfully','deletedEvent':result}), 200