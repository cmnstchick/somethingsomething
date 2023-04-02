# from models import 
from flask import Flask, render_template, url_for, redirect, request,\
     send_from_directory
import os.path
import time


app = Flask(__name__)

@app.route('/')
def ScamTextDetect():
    return render_template('scamtextdetector.html')

@app.route('/output', methods=["POST"])
def ScamTextInput():
    user_input = request.form["user_input"]
    print(user_input)
    
    
    return render_template('scamtextdetector.html')


if __name__ == "__main__":
    app.run(debug=True)
