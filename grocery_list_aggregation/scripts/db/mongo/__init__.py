from scripts.config import Service
from scripts.constants import DatabaseConstants
from scripts.utils.mongo_util import MongoCollectionBaseClass, MongoConnect


database = DatabaseConstants.database_name
collection_name = DatabaseConstants.collection_name


mongo_uri = Service.uri
mongo_client = MongoConnect(uri=mongo_uri)()


class CommonCollection(MongoCollectionBaseClass):
    def __init__(self):
        super().__init__(mongo_client, database=database, collection=collection_name)
