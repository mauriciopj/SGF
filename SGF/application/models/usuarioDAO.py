# -*- coding: utf-8 -*-
import sys
from flask import flash, session
from application import db
from flask_sqlalchemy import SQLAlchemy

class usuarioDAO(db.Model):
    __tablename__ = 'usuarios'
    idUsuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(150)) #Validar email para ser único
    endereco = db.Column(db.String(150))
    senha = db.Column(db.String(50))

    def __init__(self, nome, telefone, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def confirmarSenha(self, senha, senhaConf):
        if senha == senhaConf:
            self.senha = senha
            return True
        else:
            return False

    def salvar(self, obj):
        db.create_all()
        try:
            db.session.add(obj)
            db.session.commit()
        except:
            flash('Falha ao salvar o registro'+str(sys.exc_info()[0]), 'alert alert-danger')
        else:
            flash('O registro foi salvo com sucesso!', 'alert alert-success')

    def listar(self):
        users = self.query.all()
        return users

    def deletar(self, id):
        user = self.getId(self,id)
        if user:
            try:
                db.session.delete(user)
                db.session.commit()
            except:
                flash('Falha ao deletar o registro'+str(sys.exc_info()[0]), 'alert alert-danger')
            else:
                flash('O registro foi deletado com sucesso!', 'alert alert-success')

    def editar(self):
        try:
            db.session.commit()
        except:
            flash('Falha ao editar o registro'+str(sys.exc_info()[0]), 'alert alert-danger')
        else:
            flash('O registro foi atualizado com sucesso!', 'alert alert-success')

    def login(self, email = "", senha = ""):
        session['logged'] = False
        user = self.getEmail(self, email)
        if user and senha == user.senha:
            session['logged'] = True
            session['userId'] = user.idUsuario
            session['userNome'] = user.nome
            session['userEmail'] = user.email
        elif user and senha != user.senha:
            flash('Senha incorreta', 'alert alert-danger')
        else:
            flash('Usuário não existe!', 'alert alert-danger')

    def getId(self, id):
        user = self.query.filter_by(idUsuario=id).first()
        return user

    def getEmail(self, email):
        user = self.query.filter_by(email=email).first()
        return user
