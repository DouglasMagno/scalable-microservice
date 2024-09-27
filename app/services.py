class DataService:
    def __init__(self, db_client):
        self.db_client = db_client
        self.collection = self.db_client.get_collection('data_collection')

    def create_data(self, item: dict):
        result = self.collection.insert_one(item)
        return {"id": str(result.inserted_id)}

    def get_all_data(self):
        items = []
        cursor = self.collection.find()
        for document in cursor:
            document['_id'] = str(document['_id'])
            items.append(document)
        return items