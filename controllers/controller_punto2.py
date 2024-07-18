from flask import render_template, make_response
from flask_restful import Resource
from consola import heladeria1
from db import db

class Controller_punto2(Resource):
    def get(self):
        return make_response(render_template('index.html', productos = heladeria1.getProductos(), ingredientes = heladeria1.getIngredientes(),ventas = str(heladeria1.getVentasDia()), masRentable = heladeria1.producto_mas_rentable()))
    