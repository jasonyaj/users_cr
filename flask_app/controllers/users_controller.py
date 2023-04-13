from flask import Flask, render_template, request, redirect, session
from flask_app import app
from flask_app.models.users_model import Todo

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def get_users():
    list_of_users = Todo.get_all()
    return render_template('users.html', list_of_users = list_of_users)

@app.route('/users/new')
def new():
    return render_template('new.html')

@app.route('/process', methods=['POST'])
def add_user():
    print( request.form)
    new_user = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email']
    }
    Todo.create_one( new_user )
    return redirect('/users')