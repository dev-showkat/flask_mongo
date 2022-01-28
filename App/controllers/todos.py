# from config.db_config import mongo_db
import datetime
from models.todos import Todo
from bson.objectid import ObjectId
from flask import jsonify, make_response
from utils.token_util import token_required


@token_required
def create_todo_controller(data, doc):
    try:
        if not (doc.get('title', None) and doc.get('description', None )):
            return make_response(jsonify({'msg':'Invalid data'}), 400) 
        todo = Todo(title = doc.get('title'), description = doc.get('description'), created_at = datetime.datetime.now(), updated_at = datetime.datetime.now(), created_by = data['email'])
        todo.save()    
        return make_response(jsonify({"msg": "todo Created successfully"}), 201)   
    except Exception as e:
        return make_response(jsonify({'msg':e.args}), 400)

def get_todos_controller():
    try:
        todos = [{'title': todo.title, 'description': todo.description} for todo in Todo.objects]
        if not todos:
            return make_response(jsonify({'msg': "todos list is empty"}), 404) 
        return make_response(jsonify({'todos': todos}))
    except Exception as e:
        return make_response(jsonify({'msg':e.args}), 400)
    
def get_todo_controller(id):
    try:
        todo = Todo.objects(id = ObjectId(id)).first()
        if not todo:
            return make_response(jsonify({"msg": f"Todo not found, with id: {id}"}), 404)
        return make_response(jsonify({'todo': todo}), 200)
    except Exception as e:
        return make_response(jsonify({'msg':e.args}), 400)    

@token_required
def update_todo_controller(data, id, doc):
    try:
        todo = Todo.objects(id = ObjectId(id)).first()
        if not todo:
            return make_response(jsonify({"msg": f"Todo not found, with id: {id}"}), 404)
        if not doc:
            return make_response(jsonify({"msg": "Invalid data"}), 404)
        todo.update(title = doc.get('title', todo.title), description = doc.get('description', todo.description), created_at = todo.created_at, updated_at = datetime.datetime.now(), created_by = ObjectId(data['id']))
        return make_response(jsonify({"msg": f"Todo Updated successfully" }), 201)
    except Exception as e:
        return make_response(jsonify({'msg':e.args}), 400)

@token_required
def delete_todo_controller(data, id):
    try:
        todo = Todo.objects(id = ObjectId(id)).first()
        if not todo:
            return make_response(jsonify({"msg": f"Todo not found, with id: {id}"}), 404)
        todo.delete()
        return make_response(jsonify({"msg": f"Todo Deleted successfully, with id: {id}"}), 204)
    except Exception as e:
        return make_response(jsonify({'msg':e.args}), 400)
