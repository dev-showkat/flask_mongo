from flask import Flask
from flask_cors import CORS
from utils.sms_util import send_sms
from apis.users import users_blueprint
from apis.todos import todos_blueprint
from utils.password_encryption import bcrypt
from utils.email_util import mail, sent_email
from config.db_config import mongo_db, mongo_db_uri
from special_variables import (
    _secret_key, 
    _mail_server, 
    _mail_port, 
    _mail_username,
    _mail_password, 
    _mail_use_tls, 
    _mail_use_ssl
)


app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = _secret_key
app.config["MONGO_URI"] = mongo_db_uri
app.config['MAIL_SERVER']=_mail_server
app.config['MAIL_PORT'] = _mail_port
app.config['MAIL_USERNAME'] = _mail_username
app.config['MAIL_PASSWORD'] = _mail_password
# app.config['MAIL_USE_TLS'] = _mail_use_tls
app.config['MAIL_USE_SSL'] = _mail_use_ssl


mongo_db.init_app(app)
bcrypt.init_app(app)
mail.init_app(app)

# Health Check
@app.route('/')
def health_check():
    return {
        'msg': 'Health Is Good'
    }

@app.route('/email')
def send_email():
    return sent_email('header', ['showkat9600@gmail.com'], 'body of email')

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'URL Not Found: '
    }
    return message

@app.route('/sms')
def send_msg(to = '+916005927438', body = 'Hello from twilio'):
    return send_sms(to, body)

app.register_blueprint(todos_blueprint)
app.register_blueprint(users_blueprint)

if __name__ == '__main__':
    app.run()



    