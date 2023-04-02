# from models import 
from flask import Flask, render_template, url_for, redirect, request,\
     send_from_directory
import os.path
import time
from flask_mail import Mail

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
//update it with your gmail
app.config['MAIL_USERNAME'] = 'your_mail@gmail.com'
//update it with your password
app.config['MAIL_PASSWORD'] = 'your_email_password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
@app.route('/')
def ScamTextDetect():
    return render_template('scamtextdetector.html')

@app.route('/output', methods=["POST"])
def send_mail():
    user_input = request.form["user_input"]
    print(user_input)
    msg = Message('testing 123', sender =   'communist06chiken07@gmail.com', recipients = [user_input])
    msg.body = "hey, sending out email from flask!!!"
    mail.send(msg)
    
    return render_template('scamtextdetector.html')


if __name__ == "__main__":
    app.run(debug=True)
