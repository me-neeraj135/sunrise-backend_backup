from bson import ObjectId

class ClassDetailModel:
    collection_name = 'classDetail'

    def __init__(self, mongo):
        self.collection = mongo.db[self.collection_name]

    def create(self, data):
        return self.collection.insert_one(data).inserted_id

    def find(self, query):
        return list(self.collection.find(query))

    def find_one(self, query):
        return self.collection.find_one(query)

    def update(self, query, data):
        return self.collection.update_one(query, {'$set': data})

    def delete(self, query):
        return self.collection.delete_one(query)
