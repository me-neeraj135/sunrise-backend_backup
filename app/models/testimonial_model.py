from bson import ObjectId

class TestimonialModel:
    collection_name = 'testimonial'

    def __init__(self, mongo):
        self.collection = mongo.db[self.collection_name]

    def create(self, data):
        result = self.collection.insert_one(data)
        return result.inserted_id if result else None

    def find(self, query):
        # Add isActive condition to the query
        query['isActive'] = 1
        return self.collection.find(query)

    def find_one(self, query):
        # Add isActive condition to the query
        query['isActive'] = 1
        return self.collection.find_one(query)

    def update(self, query, data):
        return self.collection.update_one(query, {'$set': data})

    def delete(self, query):
        return self.collection.delete_one(query)
