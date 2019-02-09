from flask.views import MethodView
from flask import request, jsonify, abort
from application.models.usuarioDAO import usuarioDAO

class UsuarioView(MethodView):

    def get(self, id=None, page=1):
        if not id:
            users = usuarioDAO.listar(usuarioDAO)
            res = {}
            for user in users:
                res[user.idUsuario] = {
                    'idUsuario': user.idUsuario,
                    'nome': user.nome,
                    'telefone': user.telefone,
                    'email': user.email,
                    'endereco': user.endereco,
                    'senha': user.senha,
                }
        else:
            user = usuarioDAO.getId(usuarioDAO,id)
            res = {}
            if not user:
                return abort(404)
            res[user.idUsuario] = {
                'idUsuario': user.idUsuario,
                'nome': user.nome,
                'telefone': user.telefone,
                'email': user.email,
                'endereco': user.endereco,
                'senha': user.senha,
            }
        return jsonify(res)

    def post(self, id=None):
        user = usuarioDAO(
            request.form['nome'],
            request.form['telefone'],
            request.form['email'],
            request.form['endereco'],
        )
        if user.confirmarSenha(request.form['senha'],request.form['senhaConf']) == False:
            return "False"
        user.salvar(user)
        return "True"

    def put(self, id=None):
        user = usuarioDAO.getId(usuarioDAO,id)
        user.nome = request.form['nome']
        user.telefone = request.form['telefone']
        user.email = request.form['email']
        user.endereco = request.form['endereco']
        usuarioDAO.editar(user)
        return "True"
