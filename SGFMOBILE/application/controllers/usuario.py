# -*- coding: utf-8 -*-
import json
import requests
from application import app
from flask import render_template, request, session, flash, jsonify
from application.controllers.login import verificaSessao

@app.route('/novo_usuario', methods=['GET', 'POST'])
def cadastrarUsuario():
    if not verificaSessao():
        return render_template('login/login.html')
    if session['userNome'] != "Admin":
        return render_template('home/index.html')
    if request.method == "POST":
        user = {
            'nome': request.form.get('nome'),
            'telefone': request.form.get('telefone'),
            'email': request.form.get('email'),
            'endereco': request.form.get('endereco'),
            'senha': request.form.get('senha'),
            'senhaConf': request.form.get('senhaConf')
        }
        resp = request.post("http://localhost:5000/usuario/", data=user).text
        if resp == "True":
            flash('O registro foi salvo com sucesso!', 'alert alert-success')
            return listarUsuarios()
        flash('Falha ao salvar o registro', 'alert alert-danger')
    return render_template('usuario/novo_usuario.html')


@app.route('/lista_usuarios/')
def listarUsuarios():
    if not verificaSessao():
        return render_template('login/login.html')
    usersPage = requests.get("http://localhost:5000/usuario/")
    return render_template('usuario/lista_usuarios.html', users = usersPage.json())

@app.route('/deletar_usuario/<int:id>')
def deletarUsuario(id):
    pass

@app.route('/editar_usuario/<string:id>', methods=['GET', 'POST'])
def editarUsuario(id):
    if not verificaSessao():
        return render_template('login/login.html')
    userPage = requests.get("http://localhost:5000/usuario/"+id)
    if request.method == "POST":
        user = {
            'nome': request.form.get('nome'),
            'telefone': request.form.get('telefone'),
            'email': request.form.get('email'),
            'endereco': request.form.get('endereco'),
        }
        resp = requests.put("http://localhost:5000/usuario/"+id, data=user).text
        if resp == "True":
            flash('O registro foi atualizado com sucesso!', 'alert alert-success')
            if session['userNome'] == "Admin":
                return listarUsuarios()
            return meuPerfil()
        flash('Falha ao salvar o registro', 'alert alert-danger')
    return render_template('usuario/edicao_usuario.html', user = userPage.json(), idUsuario = id)

@app.route('/alterar_senha', methods=['GET', 'POST'])
def alterarSenha():
    if not verificaSessao():
        return render_template('login/login.html')
    if request.method == "POST":
        user = usuarioDAO.getId(usuarioDAO,session['userId'])
        if request.form.get('senhaAtual') == user.senha:
            if user.confirmarSenha(request.form.get('novaSenha'),request.form.get('senhaConf')) == True:
                usuarioDAO.editar(user)
                return render_template('usuario/meu_perfil.html', user = user)
        else:
            flash('Senha atual está incorreta', 'alert alert-danger')
    return render_template('usuario/edicao_usuario.html', user = user, histories = "#logoutModal2")

@app.route('/meu_perfil')
def meuPerfil():
    userPage = requests.get("http://localhost:5000/usuario/"+str(session['userId']))
    return render_template('usuario/meu_perfil.html', user = userPage.json(), idUsuario = str(session['userId']))
