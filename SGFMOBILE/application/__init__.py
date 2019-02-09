# -*- coding: utf-8 -*-
from flask import Flask
#from flask_sqlalchemy import SQLAlchemy

app = Flask('application')
app.config['SECRET_KEY'] = 'random'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/sgf'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy(app)
app.debug = True
from application.controllers import *
