
from  flask import Blueprint, request
from controllers.users import ( 
    sign_up_controller, 
    registration_controller,
    get_users_controller, 
    get_user_controller, 
    delete_user_controller, 
    user_login_controller,
    forget_password_controller,
    reset_password_controller   
)


users_blueprint = Blueprint('users', __name__)
base_url = 'users'

@users_blueprint.route(f'/{base_url}/signup', methods = ['POST'])
def sign_up():
    doc = request.get_json()
    return sign_up_controller(doc)

@users_blueprint.route(f'/{base_url}/registration', methods = ['POST'])
def register():
    doc = request.get_json()
    return registration_controller(doc)

@users_blueprint.route(f'/{base_url}/', methods = ['GET'])
def get_users():
    return get_users_controller()
     
@users_blueprint.route(f'/{base_url}/<id>/', methods = ['GET'])
def get_user(id):
    return get_user_controller(id)     

@users_blueprint.route(f'/{base_url}/<id>/', methods=['DELETE'])
def delete_user(id):
    doc = request.get_json()
    return delete_user_controller(id, doc)

@users_blueprint.route(f'/{base_url}/login/', methods=['POST'])  
def user_login(): 
    doc = request.get_json()
    return user_login_controller(doc)
    
@users_blueprint.route(f'/{base_url}/forget-password/', methods=['POST'])  
def forget_password(): 
    doc = request.get_json()
    return forget_password_controller(doc)

@users_blueprint.route(f'/{base_url}/reset-password/', methods=['PUT'])  
def reset_password(): 
    doc = request.get_json()
    return reset_password_controller(doc)
