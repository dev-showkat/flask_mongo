from flask_mail import Mail, Message
from flask import jsonify, make_response


mail = Mail() 

def sent_email(subject, recipients, body):
	if not (subject and recipients and body):
		return make_response(jsonify({"msg": "invalid data", 'required fields': ['subject', 'recipients', 'body'] }), 400)  	
	try:
		html = '<p style = "color: red">Hello, Your token: </p>'+ body
		msg = Message(subject, recipients, html = html, sender='shyxum96@gmail.com' )
		mail.send(msg)
		return make_response(jsonify({"msg": "email sent successfully!"}), 200)  
	except Exception as e:
		return make_response(jsonify({"msg": e.args}), 201)
			
        

