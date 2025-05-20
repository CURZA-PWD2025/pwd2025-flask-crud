from ...database.conect_db import ConectDB

class MarcaModel:
    
    def __init__(self, id:int=0, descripcion:str = ""):
        self.id = id
        self.descripcion =descripcion
        
    def serializar(self) -> dict:
        return {
            'id': self.id,
            'descripcion':self.descripcion,
            
        }
    
    @staticmethod
    def deserializar(data:dict):
        return MarcaModel(
            id=data['id'], 
            descripcion=data['descripcion'],
                    
        )
    
    @staticmethod
    def get_all():
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                # ejecuto la query
                cursor.execute(f"SELECT * FROM marcas")
                # guardo en una variable el resultado
                rows = cursor.fetchall()
                # lista de diccionarios
                marcas = []
                if rows:
                    for row in rows:
                        marcas.append(row)
                    return marcas                
                return False
            except Exception as exc:
                return {'mensaje': f" error al listar marcas {exc}"}
            finally:
                cnx.close()
    @staticmethod    
    def get_by_id(id:int):
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                # ejecuto la query
                cursor.execute("SELECT * FROM marcas where id = %s", (id,))
                # guardo en una variable el resultado
                row = cursor.fetchone()
                if row:
                    return row
                return False
            except Exception as exc:
                return {'mensaje':f" error buscar un producto {exc}"}
            finally:
                cnx.close()
                
    def create(self):
        cnx = ConectDB.get_connect()
        with cnx.cursor() as cursor:
            try:
                # ejecuto la query
                cursor.execute("INSERT INTO marcas (descripcion) VALUES (%s)", 
                               (self.descripcion,))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
                
            except Exception as exc:
                cnx.rollback()
                print(f" error crear un producto {exc}")
            finally:
                cnx.close()
        
    def update(self):
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                # ejecuto la query
                cursor.execute("UPDATE marcas SET descripcion = %s where id=%s ", 
                               (self.descripcion,  self.id))
                result = cursor.rowcount
                cnx.commit()
                
                if result > 0:
                    return True
                return False
                
            except Exception as exc:
                cnx.rollback()
                return {'mensaje':f" error buscar un producto {exc}"}
            finally:
                cnx.close()
                
    @staticmethod
    def delete(id:int):
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                # ejecuto la query
                cursor.execute("DELETE FROM marcas where id = %s ", 
                               (id,))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                return {'mensaje':f" error buscar un producto {exc}"}
            finally:
                cnx.close()