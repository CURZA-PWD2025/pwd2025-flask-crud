from .producto_controller import ProductoController
from flask import jsonify, request, Blueprint

producto_bp=Blueprint("producto", __name__)

@producto_bp.route("/productos/")
def get_all():
    try:
        productos = ProductoController.get_all()
        if productos:
            return jsonify(productos), 200
        else:
            return jsonify({'mensaje': 'no se encontraron productos'}),404
        
    except Exception as exc:
         return jsonify({'mensaje': f" error : {str(exc)}"}), 500
@producto_bp.route("/productos/<int:id>")
def get_one(id):
    try:
        producto = ProductoController.get_one(id)
        if producto:
            return jsonify(producto), 200
        else:
            return jsonify({'mensaje': 'no se encontro el producto'}),404
        
    except Exception as exc:
         return jsonify({'mensaje': f" error : {str(exc)}"}), 500
@producto_bp.route("/productos/", methods=["POST"])
def crear():
    try:
        data = request.get_json()
        if data is None:
            return  jsonify({'mensaje': "no se recibieron dato"})
        result = ProductoController.crear(data)
        if result:
            return jsonify({'mensaje':'producto creado correctamente'}), 201
        else:
            return jsonify({'mensaje': 'error al crear un producto'}),500
        
    except Exception as exc:
         return jsonify({'mensaje': f" error : {str(exc)}"}), 500
    
@producto_bp.route("/productos/<int:id>", methods=["PUT"])
def modificar(id):
    try:
        data = request.get_json()
        data['id'] = id
        result = ProductoController.modificar(data)
        if result:
            return jsonify({'mensaje':'producto modificado correctamente'}), 200
        else:
            return jsonify({'mensaje': 'error al modificar un producto'}),500
        
    except Exception as exc:
         return jsonify({'mensaje': f" error : {str(exc)}"}), 500

@producto_bp.route("/productos/id", methods=["DELETE"])
def eliminar(id):
    try:
        result = ProductoController.eliminar(id)
        if result:
            return jsonify({'mensaje':"producto eliminado con exito"})
        return jsonify({'mensaje':"error al eliminar un producto"})
    except Exception as exc:
        return jsonify({'mensaje':f"error str{exc}"})
