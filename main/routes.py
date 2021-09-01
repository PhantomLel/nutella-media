from flask.helpers import flash
from werkzeug.wrappers.response import Response
from main import app, db, bcrypt
from flask import render_template, redirect, session, abort, url_for, request, flash
import os, secrets, json
from main.models import User, Note
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
def home():
  return render_template('registerpage.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
  register_info = request.get_json()
  if register_info:
    print(register_info)
    hashed_password = bcrypt.generate_password_hash(register_info['values']['password']).decode('utf-8')
    
    user = User(f_name=register_info['values']['first_name'],
    l_name=register_info['values']['last_name'], 
    email=register_info['values']['password'],
    password=hashed_password)

    db.session.add(user)
    db.session.commit()

  return render_template('registerpage.html')

    

  