import  os
from dotenv import load_dotenv


BASE_DIR = os.path.join(os.path.dirname(__file__))   # refers to application_top
dotenv_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path)

_secret_key = os.environ.get('SECRET_KEY')
_mail_server = os.environ.get('MAIL_SERVER')
_mail_port = os.environ.get('MAIL_PORT')
_mail_username = os.environ.get('MAIL_USERNAME')
_mail_password = os.environ.get('MAIL_PASSWORD')
_mail_use_tls = os.environ.get('MAIL_USE_TLS')
_mail_use_ssl = os.environ.get('MAIL_USE_SSL')
_twilio_sid = os.environ.get('TWILIO_SID')
_twilio_auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
_twilio_phone_number = os.environ.get('TWILIO_PHONE_NUMBER')