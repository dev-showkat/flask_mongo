from flask import jsonify, make_response
from twilio.rest import Client
from special_variables import _twilio_sid, _twilio_auth_token, _twilio_phone_number


account_sid = _twilio_sid
auth_token = _twilio_auth_token
client = Client(account_sid, auth_token)


def send_sms(to, body):
    try:
        if not (to and body):
            return make_response(jsonify({"msg": "invalid data", 'required fields': ['to', 'body'] }), 400) 
        message = client.messages.create(to = to, body = body, from_ = _twilio_phone_number)
        return make_response(jsonify({"msg": "sms sent successfully!", 'sms': message.body, 'to': to}), 200)
    except Exception as e:
        return make_response(jsonify({"msg": e.args}), 201)
