#-*- coding: utf-8 -*-
from flask.views import MethodView
from flask import request, jsonify, abort
from application.models.socioDAO import socioDAO

class SocioView(MethodView):

    def get(self, id=None, page=1):
        if not id:
            socios = socioDAO.listar(socioDAO)
            res = {}
            for socio in socios:
                res[socio.idSocio] = {
                    'idSocio': socio.idSocio,
                    'nome': socio.nome,
                    'cpf': socio.cpf,
                    'telefone': socio.telefone,
                    'endereco': socio.endereco,
                    'complemento': socio.complemento,
                    'sexo': socio.sexo,
                }
            return jsonify(res)
        else:
            socio = socioDAO.getId(socioDAO,id)
            if not socio:
                abort(404)
            res = {}
            res[socio.idSocio] = {
                'idSocio': socio.idSocio,
                'nome': socio.nome,
                'cpf': socio.cpf,
                'telefone': socio.telefone,
                'endereco': socio.endereco,
                'complemento': socio.complemento,
                'sexo': socio.sexo,
            }
            return jsonify(res)
