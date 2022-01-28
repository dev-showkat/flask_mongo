from config.db_config import mongo_db
from models.todos import Todo

class User(mongo_db.Document):
    email = mongo_db.EmailField(required = True, unique = True)
    password = mongo_db.StringField(required = True)
    created_at = mongo_db.DateTimeField()
    updated_at = mongo_db.DateTimeField()
    todos = mongo_db.ListField(mongo_db.ReferenceField('User', reverse_delete_rule=mongo_db.PULL))


User.register_delete_rule(Todo, 'created_by', mongo_db.CASCADE)