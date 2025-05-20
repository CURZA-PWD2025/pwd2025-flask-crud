from .producto_model import ProductoModel

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
        producto = ProductoModel( descripcion=data['descripcion'], precio=data['precio'], stock=data['stock'])
        result= producto.create()
        return result
        
    @staticmethod
    def modificar(data:dict):
        producto = ProductoModel(id=data['id'], descripcion=data['descripcion'], precio=data['precio'], stock=data['stock'])
        result = producto.update()
        return result
        
    @staticmethod    
    def eliminar(id):
        result = ProductoModel.delete(id)
        return result

