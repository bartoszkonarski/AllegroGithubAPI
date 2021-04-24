from flask import Blueprint, render_template,request
# from flask_wtf import Form
from wtforms import StringField, Form
import requests
views = Blueprint('views', __name__)

class UserNameForm(Form):
    username = StringField('username')
    
@views.route('/',methods=['GET','POST'])
def mainpage():
    form = UserNameForm(request.form)
    if request.method=='POST':
        username = request.form.get('username')
        response = requests.get(f"http://localhost:5000/api/{username}")
        if response.status_code == 404:
            return render_template("results.html",form=form,data=None)
        return render_template("results.html",form=form,data=response.json())
    
    
    return render_template("base.html",form=form)