from flask import render_template, make_response, request
from flask_restful import Resource
from consola import heladeria1


class Controller_heladeria(Resource):
    
    def get(self):
        return make_response(render_template('ventas.html'))
    
    def post(self):
        nombre_producto = request.form.get('nombre_producto')
        if not nombre_producto:
            return {"message": "Nombre del producto es requerido"}, 400
        
        try:
            result = heladeria1.vender(nombre_producto)
            return {"message": result}, 200
        except ValueError as e:
            return {"message": str(e)}, 400
    