from pymongo import MongoClient
from pymongo.errors import InvalidOperation, OperationFailure
from app.config import Config

class MongoDB:
    is_connected = False
    _client = None
    _config = None
    _CONNECTION_TIMEOUT_MS = 3000
    _MAX_POOL_SIZE = 10

    def __init__(self, config: Config) -> None:
        self._config = config
        self._client = self._connect()

    def get_connection(self, database: str = None):
        if not self.is_connected:
            self._client = self._connect()

        if database is None:
            database = self._config.mongo.database

        return self._client.get_database(database)

    def get_collection(self, name: str, database: str = None):
        return self.get_connection(database).get_collection(name)

    def create_index(self, collection_name, index, **kwargs) -> str:
        return self.get_collection(collection_name).create_index(index, **kwargs)

    def drop_index(self, collection_name, index_name, **kwargs) -> bool:
        try:
            self.get_collection(collection_name).drop_index(index_name, **kwargs)
        except OperationFailure:
            return False

        return True

    def is_mongo_up(self) -> bool:
        try:
            connection = self.get_connection()
            stats = connection.command('dbstats')
            return stats['ok'] == 1
        except InvalidOperation:
            return False

    def disconnect(self) -> None:
        self._client.close()
        self.is_connected = False

    def _connect(self) -> MongoClient:
        connection = MongoClient(
            self._config.mongo.url,
            maxPoolSize=self._MAX_POOL_SIZE,
            connectTimeoutMS=self._CONNECTION_TIMEOUT_MS,
            uuidRepresentation='standard',
        )

        self.is_connected = True

        return connection