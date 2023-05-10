from io import BytesIO
from flask import Blueprint, render_template, request, redirect, flash, send_file
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

#REgistar o Blueprint(permite encapsular as funcionalidades, em vez de usar tudo na app.py)
bp_user = Blueprint('bp_user', __name__, template_folder="templates") 
#conectar a base de dados:
conn = sqlite3.connect('PlanosUser.db')
#ativar a relação entre as tabelas
conn.execute('PRAGMA foreign_keys = ON')

@bp_user.route('/')
def index():
    return  render_template('index.html', user = current_user)

#função para fazer o registos dos users(sign)
@bp_user.route('/sigin', methods=['GET' , 'POST' ])
def sigin():

    if request.method == 'GET':
        return render_template("sigin.html")

    if request.method == 'POST':
        nome      = request.form.get('name')
        #last_name = request.form.get('last_name') 
        #user_name = request.form.get('user_name')
        email     = request.form.get('email')
        password  = request.form.get('password')
        telefone  = request.form.get('fone')
        '''
        query = 'SELECT * FROM Utilizador WHERE email == %s'%(email)
        cursor = conn.execute(query)

        if cursor:
            flash("Email alread exist.",category = "error")
            return render_template("sigin.html")
        '''
        query = 'INSERT INTO Utilizador (Nome, Email, Passe, Telefone)VALUES(?,?,?,?)'
        conn.execute(query,(nome, email, generate_password_hash(password, method = 'sha256'), telefone))
        conn.commit()
        conn.close()

    flash("Account Created", category="Success")
    return redirect("login")

#função para fazer o login no sistema: 
@bp_user.route('/login' , methods=['GET' , 'POST' ])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    if request.method == 'POST':
        email = request.form.get('email')
        password  = request.form.get('password')

        query = 'SELECT Nome, Passe FROM Utilizador WHERE email == %s'%(email)
        user = conn.execute(query)


        if user:
            if check_password_hash(user[1], password):
                query = 'SELECT FROM Utilizador WHERE email == %s'%(email)
                users = conn.execute(query)
                login_user(users, remember = True)
                #if user.user_name == 'Admin':
                   # return redirect("Admin")
                return redirect("costumer")
            else:
                 flash("Incorrect Password, try again", category = "error")
        else:
             flash("User email does not exist", category="error")
    
    return  render_template('login.html')

@bp_user.route('/costumer', methods=['GET' , 'POST' ])
@login_required
def costumer():
    return render_template("costumer.html", user = current_user)