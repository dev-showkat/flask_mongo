import email
import jwt
import datetime
from models.users import User
from bson.objectid import ObjectId
from utils.email_util import sent_email
from flask import jsonify, make_response
from special_variables import _secret_key
from utils.token_util import token_required
from flask_bcrypt import generate_password_hash, check_password_hash


def sign_up_controller(doc):
    try:
        user = User.objects(email = doc.get('email', None)).first()
        if user:
            return make_response(jsonify({'msg':'user already exists'}), 400) 
        if not (doc and doc.get('email', None)):
            return make_response(jsonify({'msg':'email and password are required'}), 400)  
        # token = jwt.encode({'email': doc.get('email'), 'password': doc.get('password'), 'id':'', 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes = 20)}, _secret_key, 'HS256')
        token = jwt.encode({'email': doc.get('email'), 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes = 30)}, _secret_key, 'HS256')
        subject = 'Registration Token'
        return sent_email(subject, [doc.get('email')], token), 200
    except Exception as e:
        return make_response(jsonify({'msg': e.args }), 400)

@token_required
def registration_controller(data, doc):
    try:
        user = User.objects(email = data.get('email', None)).first()
        if user:
            return make_response(jsonify({'msg':'user already exists'}), 400) 
        if not (doc and doc.get('password', None)):
            return make_response(jsonify({'msg':'password is required'}), 400) 
        user = User(email = data.get('email'), password = generate_password_hash(doc.get('password', None)), created_at = datetime.datetime.now(), updated_at = datetime.datetime.now())
        user.save()    
        return make_response(jsonify({"msg": "user created successfully"}), 201)   
    except Exception as e:
        return make_response(jsonify({'msg': e.args }), 400)

def get_users_controller():
    try:
        users = [{'email': user.email} for user in User.objects]
        if not users:
           return make_response(jsonify({'msg': "users list is empty"}), 404) 
        return make_response(jsonify({'users': users}), 200)
    except Exception as e:
        return make_response(jsonify({'msg': e.args }), 400)
    
def get_user_controller(id):
    try:
        user = User.objects(id = ObjectId(id)).first()
        if not user:
            return make_response(jsonify({"msg": f"user not found, with id: {id}"}), 404)
        return make_response(jsonify({'email': user.email}), 200)
    except Exception as e:
        return make_response(jsonify({'msg':e.args }), 400)     

@token_required
def delete_user_controller(data, id, doc):
    try:
        user = User.objects(id = ObjectId(id)).first()
        if not user:
            return make_response(jsonify({"msg": f"user not found, with id: {id}"}), 404)
        if not (doc and doc.get('email', None) and doc.get('password', None)):
            return make_response(jsonify({'msg':'email and password are required'}), 400)
        if not (user.email == doc.get('email') and check_password_hash(user.password[2:-1], doc['password'])):
            return make_response(jsonify({'msg':'wrong email or password'}), 400)
        user.delete()
        return make_response(jsonify({"msg": f"user deleted successfully, with id: {id}"}), 204)
    except Exception as e:
        return make_response(jsonify({'msg':e.args}), 400)

def user_login_controller(doc):
    try:
        user = User.objects(email = doc.get('email', None)).first()
        if not (user and doc.get('password', None)):
            return make_response(jsonify({"msg": f"user not exists or incorrect password", "required fields": ['email', 'password'] }), 404) 
        if user.password[0] != '$':
            password = user.password.split("'")[1]
        else:
            password = user.password
        if not check_password_hash(password, doc['password']):
            return make_response(jsonify({"msg": "password is incorrect"}))
        token = jwt.encode({'email': user.email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)}, _secret_key, 'HS256')
        return make_response(jsonify({"msg": f"LoggedIn successfully", "token": token}), 200)
    except Exception as e:
        return make_response(jsonify({'msg':f'{e.args} or invalid data'}), 400)
    
    
def forget_password_controller(doc):
    try:
        email = doc.get('email', None)
        user = User.objects(email = email).first()
        if not user:
            return make_response(jsonify({'msg':f'user not found, with email {email}' } ), 404)
        token = jwt.encode({'email': user.email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes = 20)}, _secret_key, 'HS256')
        subject = 'Forget Password Token'
        return sent_email(subject, [email], token)
    except Exception as e:
        return make_response(jsonify({'msg': 'invalid data'}), 400)

@token_required
def reset_password_controller(data, doc):
    try:
        new_password = doc.get('new_password', None)
        if not new_password:
            return make_response(jsonify({'msg': 'new password is required'}), 400)    
        user = User.objects(email = data['email']).first()
        if not user:
            return make_response(jsonify({"msg": f"user not found, with email: {data['email']}"}), 404)
        user.update(email = user['email'], password = str(generate_password_hash(new_password)), updated_at = datetime.datetime.now())
        subject = 'Password reset successful'
        body = f'your password has been reset successfully, your new password is: {new_password}'
        return sent_email(subject, [user.email], body)
    except Exception as e:
        return make_response(jsonify({'msg':e.args, 'status': 500})) 
    
    


