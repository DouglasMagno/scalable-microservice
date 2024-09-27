from app.services import DataService
from app.config import Config
from app.database import MongoDB

class ServerContext:
    def __init__(self):
        self.config = Config()
        self.db_client = MongoDB(self.config)
        self.service = DataService(self.db_client)