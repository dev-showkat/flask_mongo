import jwt
from functools import wraps
from flask import jsonify, request
from special_variables import _secret_key



def token_required(f):
    wraps(f)
    def token_decorater(*args, **kwargs):
        if not 'token' in request.headers:
            return jsonify({'message' : 'Token is missing!'}), 401
        token = request.headers['token']            
        try: 
            data = jwt.decode(token, _secret_key, 'HS256')
            return f(data, *args, **kwargs)
        except Exception as e:
            return jsonify({'message' : f'token or {e.args}' }), 401
    return token_decorater