import os

class MongoConfig:
    def __init__(self):
        self.url = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017')
        self.database = os.environ.get('DATABASE_NAME', 'your_database_name')

class Config:
    def __init__(self):
        self.mongo = MongoConfig()