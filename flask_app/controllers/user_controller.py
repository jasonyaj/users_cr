from flask import Flask, render_template, request, redirect, session
from flask_app import app
from flask_app.models.user_model import User
from flask_app.models.users_model import Todo

@app.route('/users/<int:id>')
def display_user_info(id):
    data = {
        'user_id' : id
    }
    current_user = User.get_one_user( data )
    return render_template( 'user.html', current_user = current_user )

@app.route('/users/<int:id>/edit')
def display_user_update_info(id):
    data = {
        'user_id' : id
    }
    current_user = User.get_one_user( data )
    return render_template( 'edit.html', current_user=current_user )

@app.route('/users/update/<int:id>', methods=['POST'])
def update_user(id):
    print(request.form)
    update_user = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        "user_id" : id
    }
    Todo.update_one( update_user )
    return redirect( f'/users/{id}' )