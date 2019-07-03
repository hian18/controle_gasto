from .db import db

categorias = db.Table('categorias',
                      db.Column('categoria_id', db.Integer, db.ForeignKey(
                          'categoria.id'), primary_key=True),
                      db.Column('despesa_id', db.Integer, db.ForeignKey(
                          'despesas.id'), primary_key=True)
                      )


class Categoria(db.Model):
    __tablename__ = 'categoria'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True)

    def __repr__(self):
        return self.nome


class Despesa(db.Model):
    __tablename__ = 'despesas'
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(80))
    valor = db.Column(db.Float)
    data = db.Column(db.DateTime)
    categorias = db.relationship('Categoria', secondary=categorias,
                                 lazy='subquery', backref=db.backref('despesas', lazy=True))
