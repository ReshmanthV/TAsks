from typing import Dict, List
from pymongo import MongoClient


class MongoConnect:
    def __init__(self, uri):
        try:
            self.uri = uri
            self.client = MongoClient(self.uri)
        except Exception as e:
            print(f"Exception in connection {(str(e))}")
            raise e

    def __call__(self, *args, **kwargs):
        return self.client


class MongoCollectionBaseClass:
    def __init__(self, mongo_client, database, collection):
        self.client = mongo_client
        self.database = database
        self.collection = collection

    def insert_one(self, data: Dict):
        try:
            database_name = self.database
            collection_name = self.collection
            db = self.client[database_name]
            collection = db[collection_name]
            result = collection.insert_one(data)
            return result
        except Exception as e:
            print(f"Error in inserting the data {str(e)}")
            raise e

    def find(self):
        try:
            database_name = self.database
            collection_name = self.collection
            db = self.client[database_name]
            collection = db[collection_name]
            result = collection.find({})
            final_result = []
            for each in result:
                del each["_id"]
                final_result.append(each)
            if len(final_result) == 0:
                return "Product list is empty"
            return final_result
        except Exception as e:
            print(f"Error in inserting the data {str(e)}")
            raise e

    def update_one(self, prod_id: Dict, data: Dict):
        try:
            database_name = self.database
            collection_name = self.collection
            db = self.client[database_name]
            collection = db[collection_name]
            response = collection.update_one(prod_id, {"$set": data})
            return response.modified_count
        except Exception as e:
            print(f"Failed to update one doc {str(e)}")
            raise e

    def delete_one(self, prod_id: Dict):
        try:
            database_name = self.database
            collection_name = self.collection
            db = self.client[database_name]
            collection = db[collection_name]
            result = collection.delete_one(prod_id)
            return result
        except Exception as e:
            print(f"Failed to delete {str(e)}")
            raise e

    def aggregate(self, pipelines: List):
        try:
            database_name = self.database
            collection_name = self.collection
            db = self.client[database_name]
            collection = db[collection_name]
            response = collection.aggregate(pipelines)
            return response
        except Exception as e:
            print(f"Failed to get the aggregate data {str(e)}")
            raise e
