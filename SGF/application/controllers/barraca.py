# -*- coding: utf-8 -*-
from application import app
from flask import render_template, request
from application.controllers.login import verificaSessao
from application.models.barracaDAO import barracaDAO

@app.route('/nova_barraca', methods=['GET', 'POST'])
def cadastrarBarraca():
    if not verificaSessao():
        return render_template('login/login.html')
    if request.method == "POST":
        barraca = barracaDAO(   request.form.get('identificacao'),
                                request.form.get('descricao'),
                                request.form.get('tamanho'),
                                request.form.get('localizacao'))
        barraca.salvar(barraca)
    return render_template('barraca/nova_barraca.html')

@app.route('/lista_barracas')
def listarBarracas():
    if not verificaSessao():
        return render_template('login/login.html')
    barracas = barracaDAO.listar(barracaDAO)
    return render_template('barraca/lista_barracas.html', barracas = barracas)

@app.route('/deletar_barraca/<int:id>')
def deletarBarraca(id):
    if not verificaSessao():
        return render_template('login/login.html')
    barracaDAO.deletar(barracaDAO,id)
    return listarBarracas()

@app.route('/editar_barraca/<int:id>', methods=['GET', 'POST'])
def editarBarraca(id):
    if not verificaSessao():
        return render_template('login/login.html')
    barraca = barracaDAO.getId(barracaDAO,id)
    if request.method == "POST":
        barraca.identificacao = request.form.get('identificacao')
        barraca.descricao = request.form.get('descricao')
        barraca.tamanho = request.form.get('tamanho')
        barraca.localizacao = request.form.get('localizacao')
        barracaDAO.editar(barraca)
        return listarBarracas()
    return render_template('/barraca/edicao_barraca.html', barraca = barraca)
