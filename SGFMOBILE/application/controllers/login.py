# -*- coding: utf-8 -*-
import json, requests
from application import app
from flask import render_template, request, flash, session, jsonify

global isset

@app.route('/login', methods=['GET','POST'])
def fazerLogin():
    if verificaSessao():
        return render_template('home/index.html')
    elif request.method == "POST":
        email = request.form.get('email')
        senha = request.form.get('senha')
        usersPage = requests.get("http://localhost:5000/usuario/")
        users = usersPage.json()
        session['logged'] = False
        isset = False
        for key in users:
            if users[key]['email'] == email and users[key]['senha'] == senha:
                session['logged'] = True
                session['userId'] = int(users[key]['idUsuario'])
                session['userNome'] = users[key]['nome']
                session['userEmail'] = users[key]['email']
                isset = True
                break
            elif users[key]['email'] == email and senha != users[key]['senha']:
                flash('Senha incorreta', 'alert alert-danger')
                isset = True
        if isset != True:
            flash('Usuário não existe!', 'alert alert-danger')
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
