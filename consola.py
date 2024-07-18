from clases.base import Base
from clases.complemento import Complemento
from clases.copa import Copa
from clases.malteada import Malteada
from clases.heladeria import Heladeria
from models.model_ingrediente import insertar_ingrediente
from models.model_producto import insertar_producto
from db import db
heladeria1 = Heladeria()

base1 = Base('fresa extrema', 3000, 125, 30, False, 'fresa')
base2 = Base('chocolate cherry', 4500.20, 225, 10, False, 'chocolate')
complemento1 = Complemento('mani', 1500, 65, 1000, True)



# Ingredientes Base
helado_fresa = Base(precio=1200, calorias=150, nombre="Helado de Fresa", inventario=10, esVegetariano=True, sabor="Fresa")
helado_vainilla = Base(precio=1000, calorias=200, nombre="Helado de Vainilla", inventario=15, esVegetariano=True, sabor="Vainilla")

# Ingredientes Complemento
chispas_chocolate = Complemento(precio=500, calorias=50, nombre="Chispas de Chocolate", inventario=20, esVegetariano=True)
mani_japones = Complemento(precio=900, calorias=100, nombre="Mani Japonés", inventario=5, esVegetariano=True)

copa1 = Copa('copa tentacion', 15000, 'large',[base1, base2, complemento1])
malteada1 = Malteada('copa chocolate', 9000, 10, [base1, base2, complemento1])
malteada2 = Malteada('explosion amarilla', 4000, 10, [base1, base2, complemento1])
# Crear productos
copa_fresa = Copa(
    nombre="Copa Fresa",
    precioPublico=7500,
    tipoVaso="Mediano",
    ingredientes=[helado_fresa, chispas_chocolate]
)

malteada_vainilla = Malteada(
    nombre="Malteada Vainilla",
    precioPublico=8500,
    volumen=500,
    ingredientes=[helado_vainilla, mani_japones]
)


heladeria1.setIngredientes([base1, base2, complemento1, helado_fresa, helado_vainilla, chispas_chocolate, mani_japones])
heladeria1.setProductos([copa1, malteada1, malteada2, copa_fresa, malteada_vainilla])

""" print(heladeria1.producto_mas_rentable())
print(heladeria1.vender('copa '))
print("Venta de Copa Fresa:", heladeria1.vender("Copa Fresa"))
print("Venta de Malteada Vainilla:", heladeria1.vender("Malteada Vainilla"))
print("Venta de Copa Fresa nuevamente:", heladeria1.vender("Copa Fresa"))
print(heladeria1.getVentasDia())
print(heladeria1.getIngredientes()[0].getNombre()) """

#insertar_ingrediente('arequioe', 3000, 200, 10, False)
#insertar_producto('Copa', 'felicidad roja', 9200, 5, 6, 7)
""" ingrediente = Ingrediente('fresas frescas', 2300, 15, 100, True)
db.session.add(ingrediente)
db.session.commit()
 """

""" message = heladeria1.vender('berries')
print(message) """
print(heladeria1.getProductos())