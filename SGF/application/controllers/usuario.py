# -*- coding: utf-8 -*-
from application import app
from flask import render_template, request, session, flash, redirect, url_for
from application.controllers.login import verificaSessao
from application.models.usuarioDAO import usuarioDAO

@app.route('/novo_usuario', methods=['GET', 'POST'])
def cadastrarUsuario():
    if not verificaSessao():
        return render_template('login/login.html')
    if session['userNome'] != "Admin":
        return render_template('home/index.html')
    if request.method == "POST":
        user = usuarioDAO(  request.form.get('nome'),
                            request.form.get('telefone'),
                            request.form.get('email'),
                            request.form.get('endereco'))
        if user.confirmarSenha(request.form.get('senha'),request.form.get('senhaConf')) == True:
            user.salvar(user)
            return listarUsuarios()
        else:
            flash('Senhas não correspondem', 'alert alert-danger')
    return render_template('usuario/novo_usuario.html')

@app.route('/lista_usuarios')
def listarUsuarios():
    if not verificaSessao():
        return render_template('login/login.html')
    users = usuarioDAO.listar(usuarioDAO)
    return render_template('usuario/lista_usuarios.html', users = users)

@app.route('/deletar_usuario/<int:id>')
def deletarUsuario(id):
    if not verificaSessao():
        return render_template('login/login.html')
    usuarioDAO.deletar(usuarioDAO,id)
    return listarUsuarios()

@app.route('/editar_usuario/<int:id>', methods=['GET', 'POST'])
def editarUsuario(id):
    if not verificaSessao():
        return render_template('login/login.html')
    user = usuarioDAO.getId(usuarioDAO,id)
    if request.method == "POST":
        user.nome = request.form.get('nome')
        user.telefone = request.form.get('telefone')
        user.email = request.form.get('email')
        user.endereco = request.form.get('endereco')
        usuarioDAO.editar(user)
        return listarUsuarios()
    return render_template('usuario/edicao_usuario.html', user = user)

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
    user = usuarioDAO.getId(usuarioDAO,session['userId'])
    return render_template('usuario/meu_perfil.html', user = user)
