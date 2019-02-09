#-*- coding: utf-8 -*-
from datetime import datetime
from flask.views import MethodView
from flask import request, jsonify, abort
from application.models.frequenciaDAO import frequenciaDAO, lista
from application.models.usuarioDAO import usuarioDAO
from application.models.socioDAO import socioDAO

class FrequenciaView(MethodView):

    def get(self, id=None, page=1):
        if not id:
            frequencias = frequenciaDAO.listar(frequenciaDAO)
            usuarios = usuarioDAO.listar(usuarioDAO)
            res = {}
            for frequencia in frequencias:
                for usuario in usuarios:
                    if usuario.idUsuario == frequencia.idUsuario:
                        usuarioNome = usuario.nome
                    if not frequencia.idUsuarioMod:
                        usuarioNomeMod = None
                        frequencia.dataHoraMod = None
                    elif usuario.idUsuario == frequencia.idUsuarioMod:
                        usuarioNomeMod = usuario.nome
                res[frequencia.idFrequencia] = {
                    'idFrequencia': frequencia.idFrequencia,
                    'dataHora': frequencia.dataHora,
                    'usuario': usuarioNome,
                    'dataHoraMod': frequencia.dataHoraMod,
                    'usuarioMod': usuarioNomeMod,
                }
        else:
            frequencia = frequenciaDAO.getId(frequenciaDAO,id)
            if not frequencia:
                abort(404)
            res = {}
            res[frequencia.idFrequencia] = {
                'dataHora': frequencia.dataHora,
            }
        return jsonify(res)

    def post(self):
        freq = frequenciaDAO(request.form.get('idUsuario'))
        freq.salvar(freq)
        return "True"

    def put(self, id=None):
        freq = frequenciaDAO.getId(frequenciaDAO,id)
        freq.idUsuarioMod = request.form['idUsuarioMod']
        freq.dataHoraMod = datetime.now()
        freq.dataHoraMod = freq.dataHoraMod.strftime('%d/%m/%Y %H:%M')
        frequenciaDAO.editar(freq)
        return "True"

    def delete(self, id):
        # Delete the record for the provided id.
        return

class ListaView(MethodView):

    def get(self, id=None, page=1):
        from application.models.frequenciaDAO import lista
        listas = lista.listar(lista)
        socios = socioDAO.listar(socioDAO)
        res = {}
        for lista in listas:
            if lista.idFrequencia == id:
                for socio in socios:
                    if socio.idSocio == lista.idSocio:
                        socioNome = socio.nome
                        sociocpf = socio.cpf
                        break
                res[lista.idLista] = {
                    'idLista': lista.idLista,
                    'cpf': sociocpf,
                    'idSocio': lista.idSocio,
                    'socio': socioNome,
                    'status': lista.status,
                }
        return jsonify(res)

    def post(self):
        socios = socioDAO.listar(socioDAO)
        for socio in socios:
            obj = lista(socio.idSocio,request.form.get(str(socio.idSocio)))
            obj.idFrequencia = frequenciaDAO.getUltimo(frequenciaDAO).idFrequencia
            obj.salvaFrequencia(obj)
        return "True"

    def put(self, id=None):
        socios = socioDAO.listar(socioDAO)
        listas = lista.listar(lista)
        for obj in listas:
            if obj.idFrequencia == id:
                idSocio = socioDAO.getId(socioDAO,obj.idSocio).idSocio
                if obj.idSocio == idSocio and obj.status != request.form[str(obj.idSocio)]:
                    obj.status = request.form[str(obj.idSocio)]
                    obj.atualizarFrequencia()
        return "True"
