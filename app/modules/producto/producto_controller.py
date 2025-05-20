from .producto_model import ProductoModel
from ..marca.marca_model import MarcaModel as Marca

class ProductoController:
    
    @staticmethod
    def get_all():
        productos = ProductoModel.get_all()
        return productos
    
    @staticmethod
    def get_one(id):
        producto = ProductoModel(id=id).get_by_id()
        return producto
    
    @staticmethod
    def crear(data:dict):
        marca = Marca.deserializar(Marca.get_by_id(data['marca_id']))
        producto = ProductoModel( descripcion=data['descripcion'], precio=data['precio'], stock=data['stock'], marca=marca)
        result= producto.create()
        return result
        
    @staticmethod
    def modificar(data:dict):
        marca = Marca.deserializar(Marca.get_by_id(data['marca_id']))    
        data['marca']= marca
        producto = ProductoModel.deserializar(data)
        result = producto.update()
        return result
        
    @staticmethod    
    def eliminar(id):
        result = ProductoModel.delete(id)
        return result

