# -*- coding: utf-8 -*-
from application import app
from flask import render_template, request, session
from application.controllers.login import verificaSessao
from application.models.reservaDAO import reservaDAO
from application.models.barracaDAO import barracaDAO
from application.models.socioDAO import socioDAO
from application.models.usuarioDAO import usuarioDAO

@app.route('/nova_reserva', methods=['GET', 'POST'])
def cadastrarReserva():
    if not verificaSessao():
        return render_template('login/login.html')
    socios = socioDAO.listar(socioDAO)
    barracas = barracaDAO.listar(barracaDAO)
    if request.method == "POST":
        reserva = reservaDAO(   session.get('userId'),
                                request.form.get('idSocio'),
                                request.form.get('idBarraca'))
        reserva.salvar(reserva)
    return render_template('/reserva/nova_reserva.html', socios = socios, barracas = barracas)

@app.route('/listar_reservas')
def listarReservas():
    if not verificaSessao():
        return render_template('login/login.html')
    reservas = reservaDAO.listar(reservaDAO)
    usuarios = usuarioDAO.listar(usuarioDAO)
    socios = socioDAO.listar(socioDAO)
    barracas = barracaDAO.listar(barracaDAO)
    return render_template('/reserva/lista_reservas.html', reservas = reservas, usuarios = usuarios, socios = socios, barracas = barracas)

@app.route('/deletar_reserva/<int:id>')
def deletarReserva(id):
    if not verificaSessao():
        return render_template('login/login.html')
    reservaDAO.deletar(reservaDAO,id)
    return listarReservas()

@app.route('/editar_reserva/<int:id>', methods=['GET', 'POST'])
def editarReserva(id):
    if not verificaSessao():
        return render_template('login/login.html')
    reserva = reservaDAO.getId(reservaDAO,id)
    socios = socioDAO.listar(socioDAO)
    barracas = barracaDAO.listar(barracaDAO)
    if request.method == "POST":
        reserva.idUsuario = session.get('userId')
        reserva.idSocio = request.form.get('idSocio')
        reserva.idBarraca = request.form.get('idBarraca')
        reservaDAO.editar(reserva)
        return listarReservas()
    return render_template('/reserva/edicao_reserva.html', reserva = reserva, socios = socios, barracas = barracas)
