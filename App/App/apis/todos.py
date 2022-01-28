from  flask import Blueprint, request
from controllers.todos import (create_todo_controller, 
                            get_todos_controller, 
                            get_todo_controller, 
                            update_todo_controller, 
                            delete_todo_controller
                        )


todos_blueprint = Blueprint('todos', __name__)


@todos_blueprint.route("/todos/", methods = ['POST'])
def create_todo():
    doc = request.get_json()
    return create_todo_controller(doc)
     

@todos_blueprint.route('/todos/', methods = ['GET'])
def get_todos():
    return get_todos_controller()

@todos_blueprint.route('/todos/<id>/', methods = ['GET'])
def get_todo(id):
    return get_todo_controller(id)

@todos_blueprint.route("/todos/<id>/", methods = ['PUT'])
def update_todo(id):
    doc = request.get_json()
    return update_todo_controller(id, doc)
     

@todos_blueprint.route("/todos/<id>/", methods=['DELETE'])
def delete_todo(id):
    return delete_todo_controller(id)

