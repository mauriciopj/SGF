from application import app
from datetime import datetime
from flask import render_template, request, flash, session
from application.models.frequenciaDAO import frequenciaDAO, lista
from application.models.usuarioDAO import usuarioDAO
from application.models.socioDAO import socioDAO
from application.controllers.login import verificaSessao

@app.route('/registrar_frequencia', methods=['GET','POST'])
def registrarFrequencia():
    if not verificaSessao():
        return render_template('login/login.html')
    socios = socioDAO.listar(socioDAO)
    if request.method == "POST":
        freq = frequenciaDAO(session.get('userId'))
        freq.salvar(freq)
        for socio in socios:
            obj = lista(socio.idSocio, request.form.get(str(socio.idSocio)))
            obj.idFrequencia = freq.getUltimo().idFrequencia
            obj.salvaFrequencia(obj)
        return listarFrequencia()
    return render_template('frequencia/registra_frequencia.html', socios = socios)

@app.route('/listar_frequencia')
def listarFrequencia():
    if not verificaSessao():
        return render_template('login/login.html')
    frequencias = frequenciaDAO.listar(frequenciaDAO)
    usuarios = usuarioDAO.listar(usuarioDAO)
    return render_template('/frequencia/lista_frequencia.html', frequencias = frequencias, usuarios = usuarios)

@app.route('/editar_frequencia/<int:id>/<string:opcao>', methods=['GET', 'POST'])
def editarFrequencia(id, opcao):
    if not verificaSessao():
        return render_template('login/login.html')
    freq = frequenciaDAO.getId(frequenciaDAO,id)
    socios = socioDAO.listar(socioDAO)
    listas = lista.listar(lista)
    if request.method == "POST":
        freq.dataHoraMod = datetime.now()
        freq.dataHoraMod = freq.dataHoraMod.strftime('%d/%m/%Y %H:%M')
        freq.idUsuarioMod = session.get('userId')
        frequenciaDAO.editar(freq)
        for listaaux in listas:
            if listaaux.idFrequencia == freq.idFrequencia:
                for socio in socios:
                    if socio.idSocio == listaaux.idSocio and listaaux.status != request.form.get(str(socio.idSocio)):
                        listaaux.status = request.form.get(str(socio.idSocio))
                        listaaux.atualizarFrequencia()
                        break
        return listarFrequencia()
    if opcao == 'readonly':
        return render_template('/frequencia/detalhes_frequencia.html', freq = freq, socios = socios, listas = listas)
    return render_template('/frequencia/edicao_frequencia.html', freq = freq, socios = socios, listas = listas)
