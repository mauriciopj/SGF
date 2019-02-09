# -*- coding: utf-8 -*-
import sys
from flask import flash
from application import db
from flask_sqlalchemy import SQLAlchemy

class barracaDAO(db.Model):
    __tablename__ = 'barracas'
    idBarraca = db.Column(db.Integer, primary_key=True, autoincrement=True)
    identificacao = db.Column(db.String(20))
    descricao = db.Column(db.String(150))
    tamanho = db.Column(db.String(20))
    localizacao = db.Column(db.String(20))

    def __init__(self, identificacao, descricao, tamanho, localizacao):
        self.identificacao = identificacao
        self.descricao = descricao
        self.tamanho = tamanho
        self.localizacao = localizacao

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
        barracas = self.query.all()
        return barracas

    def deletar(self, id):
        barraca = self.getId(self,id)
        if barraca:
            try:
                db.session.delete(barraca)
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
        barraca = self.query.filter_by(idBarraca=id).first()
        return barraca
