from .marca_model import MarcaModel

class MarcaController:
    
    @staticmethod
    def get_all():
        marcas = MarcaModel.get_all()
        return marcas
    
    @staticmethod
    def get_one(id):
        marca = MarcaModel(id=id).get_by_id()
        return marca
    
    @staticmethod
    def crear(data:dict):
        print(data)
        marca = MarcaModel(descripcion=data['descripcion'])
        result= marca.create()
        return result
        
    @staticmethod
    def modificar(data:dict):
        marca = MarcaModel.deserializar(data)
        result = marca.update()
        return result
        
    @staticmethod    
    def eliminar(id):
        result = MarcaModel.delete(id)
        return result

