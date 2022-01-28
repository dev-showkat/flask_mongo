from config.db_config import mongo_db


class Todo(mongo_db.Document):
    title = mongo_db.StringField(required = True)
    description = mongo_db.StringField(required = True)
    created_at = mongo_db.DateTimeField()
    updated_at = mongo_db.DateTimeField()
    created_by = mongo_db.ReferenceField('User')

   
