# from flask_pymongo import PyMongo
from flask_mongoengine import MongoEngine

mongo_db_uri = "mongodb://localhost:27017/todo_db"

# mongo = PyMongo()
mongo_db = MongoEngine()