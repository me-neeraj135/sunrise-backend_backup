from bson import ObjectId

class SubmenuModel:
    collection_name = 'sub-menu'

    def __init__(self, mongo):
        self.collection = mongo.db[self.collection_name]

    def create(self, submenu_data):
        result = self.collection.insert_one(submenu_data)
        return result.inserted_id

    def find(self, query):
        return list(self.collection.find(query))

    def find_one(self, query):
        return self.collection.find_one(query)

    def update(self, query, submenu_data):
        result = self.collection.update_one(query, {'$set': submenu_data})
        return result

    def delete(self, query):
        result = self.collection.delete_one(query)
        return result
