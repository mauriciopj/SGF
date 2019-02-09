# -*- coding: utf-8 -*-
import json
import requests
from application import app
from datetime import datetime
from flask import render_template, request, session, flash, jsonify
from application.controllers.login import verificaSessao

@app.route('/registrar_frequencia', methods=['GET','POST'])
def registrarFrequencia():
    if not verificaSessao():
        return render_template('login/login.html')
    sociosPage = requests.get("http://localhost:5000/socio/")
    socios = sociosPage.json()
    if request.method == "POST":
        freq = {'idUsuario': 2}
        lista = {}
        for key in socios:
            lista[socios[key]['idSocio']] = {
                request.form.get(str(socios[key]['idSocio'])): socios[key]['idSocio'],
            }

        #return jsonify(lista)
        resp1 = requests.post("http://localhost:5000/frequencia/", data=freq).text
        resp2 = requests.post("http://localhost:5000/lista/", data=lista).text
        if resp1 =="True" or resp2 == "True":
            flash('O registro foi salvo com sucesso!', 'alert alert-success')
            return listarFrequencia()
        flash('Falha ao salvar o registro', 'alert alert-danger')
    return render_template('/frequencia/registra_frequencia.html', socios = socios)

@app.route('/listar_frequencias', methods=['GET'])
def listarFrequencia():
    if not verificaSessao():
        return render_template('login/login.html')
    page = requests.get("http://localhost:5000/frequencia/")
    return render_template('/frequencia/lista_frequencia.html', frequencias = page.json())

@app.route('/editar_frequencia/<string:id>/<string:opcao>', methods=['GET','POST'])
def editarFrequencia(id,opcao):
    if not verificaSessao():
        return render_template('login/login.html')
    frequenciaPage = requests.get("http://localhost:5000/frequencia/"+id)
    listaPage = requests.get("http://localhost:5000/lista/"+id)
    if opcao == "readonly":
        return render_template('/frequencia/detalhes_frequencia.html', frequencia = frequenciaPage.json(), listas = listaPage.json())
    if request.method == "POST":
        freq = {'idUsuarioMod': 2}
        lista = {}
        socios = requests.get("http://localhost:5000/socio/").json()
        for key in socios:
            lista[socios[key]['idSocio']] = {
                request.form.get(str(socios[key]['idSocio'])): socios[key]['idSocio'],
            }
        resp1 = requests.put("http://localhost:5000/frequencia/"+id, data=freq).text
        resp2 = requests.put("http://localhost:5000/lista/"+id, data=lista).text
        if resp1 =="True" or resp2 == "True":
            flash('O registro foi atualizado com sucesso!', 'alert alert-success')
            return listarFrequencia()
        flash('Falha ao salvar o registro', 'alert alert-danger')
    return render_template('/frequencia/edicao_frequencia.html', frequencia = frequenciaPage.json(), listas = listaPage.json(), idFrequencia=id)
