from sqlalchemy.orm import backref
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Producto(db.Model):
    __tablename__ = 'producto'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    descripcion = db.Column(db.String(200), nullable=True)
    link = db.Column(db.String(900), nullable=False)
    id_categoria = db.Column(db.Integer, db.ForeignKey('categoria.id'))

    def __init__(self, id, nombre, descripcion, material,link):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.material = material
        self.link = link

class Categoria(db.Model):
    __tablename__ = 'categoria'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(150), nullable=False)
    producto = db.relationship('Producto', backref='producto', lazy=True)

    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion

class Formulario(db.Model):
    __tablename__ = 'formulario'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(150), nullable=False)
    telefono = db.Column(db.Integer, nullable=False)
    asunto = db.Column(db.String(100), nullable=False)
    mensaje = db.Column(db.String(100), nullable=False)

    def __init__(self, id, nombre, correo,telefono,asunto,mensaje):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.asunto = asunto
        self.mensaje = mensaje





