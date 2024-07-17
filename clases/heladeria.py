from clases.ingrediente import Ingrediente
from clases.iProducto import iProducto

class Heladeria:
    def __init__(self):
        self._productos = []
        self._ingredientes = []
        self._ventas_del_dia = 0
    
    def producto_mas_rentable(self) -> str:
        return max(self._productos, key=lambda producto: producto.calcularRentabilidad()).getNombre()
    
    def vender(self, nombre_producto: str) -> bool:
        producto = next((p for p in self._productos if p.getNombre() == nombre_producto), None)
        if not producto:
            return False

        # Verificar inventario
        for ingrediente in producto.getIngredientes():
            inventario_ingrediente = next((i for i in self._ingredientes if i.getNombre() == ingrediente.getNombre()), None)
            if not inventario_ingrediente or inventario_ingrediente.getInventario() < 1:
                return False

        # Actualizar inventario
        for ingrediente in producto.getIngredientes():
            inventario_ingrediente = next(i for i in self._ingredientes if i.getNombre() == ingrediente.getNombre())
            inventario_ingrediente.actInventario()

        self._ventas_del_dia += 1
        return True
    
    def getProductos(self) -> list[iProducto]:
        return self._productos
    
    def setProductos(self, nuevosProductos: list[iProducto]):
        self._productos = nuevosProductos
        
    
    def getIngredientes(self):
        return self._ingredientes
    
    def setIngredientes(self, nuevosIngredientes: list[Ingrediente]):
        self._ingredientes = nuevosIngredientes
    
    def getVentasDia(self):
        return self._ventas_del_dia
    
    def setVentasDia(self, nuevasVentas: int):
        self._ventas_del_dia = nuevasVentas
    
