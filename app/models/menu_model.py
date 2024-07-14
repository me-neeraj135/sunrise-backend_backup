from bson import ObjectId

class MenuModel:
    collection_name = 'menu'

    def __init__(self, mongo):
        self.collection = mongo.db[self.collection_name]

    def create(self, menu_data):
        result = self.collection.insert_one(menu_data)
        return result.inserted_id

    def find(self, query):
        return list(self.collection.find(query))

    def find_one(self, query):
        return self.collection.find_one(query)

    def update(self, query, menu_data):
        result = self.collection.update_one(query, {'$set': menu_data})
        return result

    def delete(self, query):
        result = self.collection.delete_one(query)
        return result
