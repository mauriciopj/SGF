# -*- coding: utf-8 -*-
from application import app
from flask import render_template
from application.controllers.login import verificaSessao

@app.route('/')
def home():
    if not verificaSessao():
        return render_template('login/login.html')
    return render_template('home/index.html')
