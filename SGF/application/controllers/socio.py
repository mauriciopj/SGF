# -*- coding: utf-8 -*-
from application import app
from flask import render_template, request
from application.controllers.login import verificaSessao
from application.models.socioDAO import socioDAO

@app.route('/novo_socio', methods=['GET', 'POST'])
def cadastrarSocio():
    if not verificaSessao():
        return render_template('login/login.html')
    if request.method == "POST":
        socio = socioDAO(   request.form.get('nome'),
                            request.form.get('cpf'),
                            request.form.get('telefone'),
                            request.form.get('endereco'),
                            request.form.get('complemento'),
                            request.form.get('sexo'))
        socio.salvar(socio)
    return render_template('socio/novo_socio.html')

@app.route('/lista_socios')
def listarSocios():
    if not verificaSessao():
        return render_template('login/login.html')
    socios = socioDAO.listar(socioDAO)
    return render_template('socio/lista_socios.html', socios = socios)

@app.route('/deletar_socio/<int:id>')
def deletarSocio(id):
    if not verificaSessao():
        return render_template('login/login.html')
    socioDAO.deletar(socioDAO,id)
    return listarSocios()

@app.route('/editar_socio/<int:id>', methods=['GET', 'POST'])
def editarSocio(id):
    if not verificaSessao():
        return render_template('login/login.html')
    socio = socioDAO.getId(socioDAO,id)
    if request.method == "POST":
        socio.nome = request.form.get('nome')
        socio.cpf = request.form.get('cpf')
        socio.telefone = request.form.get('telefone')
        socio.endereco = request.form.get('endereco')
        socio.complemento = request.form.get('complemento')
        socio.sexo = request.form.get('sexo')
        socioDAO.editar(socio)
        return listarSocios()
    return render_template('/socio/edicao_socio.html', socio = socio)
