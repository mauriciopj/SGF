# -*- coding: utf-8 -*-
import sys
from flask import flash
from application import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

class frequenciaDAO(db.Model):
    __tablename__ = 'frequencia'
    idFrequencia = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idUsuario = db.Column(db.Integer)
    dataHora = db.Column(db.String(25))
    dataHoraMod = db.Column(db.String(25))
    idUsuarioMod = db.Column(db.Integer)

    def __init__(self, idUsuario):
        self.idUsuario = idUsuario
        self.dataHora = datetime.now()
        self.dataHora = self.dataHora.strftime('%d/%m/%Y %H:%M')
        self.dataHoraMod = None
        self.idUsuarioMod = None

    def __repr__(self):
        return '<frequenciaDAO %d>' % self.idFrequencia

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
        frequencia = self.query.all()
        return frequencia

    def editar(self):
        try:
            db.session.commit()
        except:
            flash('Falha ao editar o registro'+str(sys.exc_info()[0]), 'alert alert-danger')
        else:
            flash('O registro foi atualizado com sucesso!', 'alert alert-success')

    def getId(self, id):
        frequencia = self.query.filter_by(idFrequencia=id).first()
        return frequencia

    def getUltimo(self):
        ultimo = self.query.order_by('idFrequencia desc').first()
        return ultimo

class lista(db.Model):
    __tablename__ = 'lista_frequencia'
    idLista = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idSocio = db.Column(db.Integer)
    status = db.Column(db.String(8))
    idFrequencia = db.Column(db.Integer, db.ForeignKey('frequencia.idFrequencia'))

    def __init__(self, idSocio, status):
        self.idSocio = idSocio
        self.status = status

    def __repr__(self):
        return '<lista %d>' % self.idLista

    def salvaFrequencia(self, socio):
        db.create_all()
        try:
            db.session.add(socio)
            db.session.commit()
        except:
            flash('Falha ao salvar lista de frequencia'+str(sys.exc_info()[0]), 'alert alert-danger')

    def atualizarFrequencia(self):
        db.session.commit()

    def listar(self):
        listas = self.query.all()
        return listas
