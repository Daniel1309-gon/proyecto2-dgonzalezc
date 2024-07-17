from db import db
from aplicacion import app

class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo = db.Column(db.String(20), nullable=False)
    nombre = db.Column(db.String(45), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    id_ingrediente1 = db.Column(db.Integer, db.ForeignKey('ingredientes.id'))
    id_ingrediente2 = db.Column(db.Integer, db.ForeignKey('ingredientes.id'))
    id_ingrediente3 = db.Column(db.Integer, db.ForeignKey('ingredientes.id'))

    ingrediente1 = db.relationship('Ingrediente', foreign_keys=[id_ingrediente1])
    ingrediente2 = db.relationship('Ingrediente', foreign_keys=[id_ingrediente2])
    ingrediente3 = db.relationship('Ingrediente', foreign_keys=[id_ingrediente3])
    
def insertar_producto(tipo: str, nombre: str, precio: float, id1: int, id2: int, id3: int):
    with app.app_context():
        if not id3:
            id3 = 0
        producto = Producto(tipo=tipo, nombre=nombre, precio=precio, id_ingrediente1=id1, id_ingrediente2=id2, id_ingrediente3=id3)
        db.session.add(producto)
        db.session.commit()
        return 'Producto agregado correctamente'