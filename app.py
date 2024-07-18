from aplicacion import app, api
from dotenv import load_dotenv
from models.model_ingrediente import insertar_ingrediente
from models.model_producto import insertar_producto
from controllers.controller_punto2 import Controller_punto2
from controllers.controller_heladeria import Controller_heladeria
from db import db


load_dotenv()
api.add_resource(Controller_punto2, '/')
api.add_resource(Controller_heladeria, '/vender')




    