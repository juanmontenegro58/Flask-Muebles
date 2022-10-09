from .models import db, Producto

def intert_producto(id, nombre, descripcion, material):
    producto = Producto(id, nombre, descripcion, material)
    db.session.add(producto)
    db.session.commit()

def delete_producto(id):
    producto = Producto.query.filter_by(id=id).first()
    db.session.delete(producto)
    db.session.commit()

def get_productos():
    producto = Producto.query.all()
    return producto

def get_producto(id):
    producto = Producto.query.filter_by(id=id).first()
    return producto