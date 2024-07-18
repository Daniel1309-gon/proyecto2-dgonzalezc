import unittest
from aplicacion import app
from db import db
from models.model_ingrediente import Ingrediente
from models.model_producto import Producto
from clases.heladeria import Heladeria
from sqlalchemy.exc import SQLAlchemyError
from clases.complemento import Complemento
heladeria1 = Heladeria()

try:
    with app.app_context():
        ingredientes = db.session.query(Ingrediente).all()
        productos = db.session.query(Producto).all()
except SQLAlchemyError as sqle:
    raise sqle
        


heladeria1.setIngredientes(ingredientes)
heladeria1.setProductos(productos)

class TestHeladeria(unittest.TestCase):
    
    def test_producto_mas_rentable(self):
        self.assertEqual(heladeria1.producto_mas_rentable(), 'berries')
        
    def test_vender(self):
        self.assertEqual(heladeria1.vender('felicidad roja'), '¡Vendido!')
        with self.assertRaises(ValueError) as context:
            heladeria1.vender('felicidad')
            self.assertEqual(str(context.exception), 'Este producto no existe')
    
    def test_rentabilidad(self):
        with app.app_context():
            self.assertEqual(db.session.query(Producto).filter_by(nombre='berries').first().calcularRentabilidad(), 5900)
            
    def test_esSano(self):
        self.assertEqual(ingredientes[0].esSano(), True)
        
    def test_abastecer(self):
        self.assertEqual(heladeria1.abastecerIngrediente(5, 100),'Inventario actualizado.')
        
    def test_renovarInventario(self):
        complemento1 = Complemento('nueces', 800, 30, 30, True)
        complemento1.renovarInventario()
        self.assertEqual(complemento1.getInventario(), 0)
    
    def test_calorias(self):
        with app.app_context():
            producto = db.session.query(Producto).first()
            calProduct = sum(ing.calorias for ing in producto.getIngredientes())
            self.assertEqual(calProduct, 225)
            
    def test_costoProduccion(self):
        with app.app_context():
            producto = db.session.query(Producto).first()
            costos = sum(ing.precio for ing in producto.getIngredientes())
            self.assertEqual(costos, 5300)
        
