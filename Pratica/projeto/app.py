import sqlite3 
from flask import Flask

from flask import Blueprint
from flask_login import LoginManager
from path import bp_user
from models import *




app = Flask(__name__)
'''
ligacao = "sqlite:///zerra.sqlite"
app.config['SECRET_KEY'] = 'stp220613a'
app.config['SQLALCHEMY_DATABASE_URI'] = ligacao
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False
'''
app.register_blueprint(bp_user, url_prefix='/')

#db.init_app(app)
#conectar a base de dados:
conn = sqlite3.connect('PlanosUser.db')
#ativar a relação entre as tabelas
conn.execute('PRAGMA foreign_keys = ON')

login_manager = LoginManager()
login_manager.login_viewc = 'path.login'
login_manager.init_app(app)

@login_manager.user_loader
def loader_user(id):
    query = 'SELECT FROM Utilizador WHERE ID == %d'%(id)
    user = conn.execute(query)
    conn.close()
    return user






if __name__== "__main__":
    app.run(debug = True)
