# -*- coding: utf-8 -*-
import sys
from flask import flash
from application import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

class socioDAO(db.Model):
    __tablename__ = 'socios'
    idSocio = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    cpf = db.Column(db.String(11))
    telefone = db.Column(db.String(20))
    endereco = db.Column(db.String(150))
    complemento = db.Column(db.String(150))
    dataCadastro = db.Column(db.Date)
    sexo = db.Column(db.String(2))

    def __init__(self, nome, cpf, telefone, endereco, complemento, sexo):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.complemento = complemento
        self.sexo = sexo
        self.dataCadastro = datetime.today()

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
        socios = self.query.all()
        return socios

    def deletar(self, id):
        socio = self.getId(self,id)
        if socio:
            try:
                db.session.delete(socio)
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

    def getId(self, id):
        socio = self.query.filter_by(idSocio=id).first()
        return socio
