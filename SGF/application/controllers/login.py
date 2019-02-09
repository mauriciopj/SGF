# -*- coding: utf-8 -*-
from application import app
from flask import render_template, request, flash, session
from application.models.usuarioDAO import usuarioDAO

@app.route('/login', methods=['GET','POST'])
def fazerLogin():
    if verificaSessao():
        return render_template('home/index.html')
    elif request.method == "POST":
        email = request.form.get('email')
        senha = request.form.get('senha')
        usuarioDAO.login(usuarioDAO, email, senha)
        if verificaSessao():
            return render_template('home/index.html')
    return render_template('login/login.html')

@app.route('/logout')
def fazerLogout():
    session['logged'] = False
    session.pop('userNome', None)
    session.pop('userEmail', None)
    return render_template('login/login.html')

def verificaSessao():
    return session.get('logged')
