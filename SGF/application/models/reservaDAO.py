# -*- coding: utf-8 -*-
import sys
from flask import flash
from application import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

class reservaDAO(db.Model):
    __tablename__ = 'reservas'
    idReserva = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idUsuario = db.Column(db.Integer)
    idSocio = db.Column(db.Integer)
    idBarraca = db.Column(db.Integer)
    dataHora = db.Column(db.String(25))

    def __init__(self, idUsuario, idSocio, idBarraca):
        self.idUsuario = idUsuario
        self.idSocio = idSocio
        self.idBarraca = idBarraca
        self.dataHora = datetime.now()
        self.dataHora = self.dataHora.strftime('%Y/%m/%d %H:%M:%S')

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
        reservas = self.query.all()
        return reservas

    def deletar(self, id):
        reserva = self.getId(self,id)
        if reserva:
            try:
                db.session.delete(reserva)
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
        reserva = self.query.filter_by(idReserva=id).first()
        return reserva
