# src/controllers/estudiante_controller.py

from flask import Blueprint, request, jsonify
from src.services.estudiante_service import EstudianteService

# Layer: Controller Layer
# This layer handles the HTTP requests and responses.

estudiante_bp = Blueprint('estudiante_bp', __name__)

estudiante_service = EstudianteService()

@estudiante_bp.route('/', methods=['GET'])
def get_all_estudiantes():
    estudiantes = estudiante_service.get_all_estudiantes()
    return jsonify([{
        'estudiante_id': est.estudiante_id,
        'nombre': est.nombre,
        'apellido': est.apellido,
        'dni': est.dni,
        'email': est.email,
        'fecha_nacimiento': str(est.fecha_nacimiento),
        'direccion': est.direccion,
        'telefono': est.telefono
    } for est in estudiantes])

@estudiante_bp.route('/<int:estudiante_id>', methods=['GET'])
def get_estudiante(estudiante_id):
    estudiante = estudiante_service.get_estudiante_by_id(estudiante_id)
    if estudiante:
        return jsonify({
            'estudiante_id': estudiante.estudiante_id,
            'nombre': estudiante.nombre,
            'apellido': estudiante.apellido,
            'dni': estudiante.dni,
            'email': estudiante.email,
            'fecha_nacimiento': str(estudiante.fecha_nacimiento),
            'direccion': estudiante.direccion,
            'telefono': estudiante.telefono
        })
    return jsonify({'message': 'Estudiante not found'}), 404

@estudiante_bp.route('/', methods=['POST'])
def create_estudiante():
    data = request.get_json()
    estudiante = estudiante_service.create_estudiante(data)
    return jsonify({
        'estudiante_id': estudiante.estudiante_id,
        'nombre': estudiante.nombre,
        'apellido': estudiante.apellido,
        'dni': estudiante.dni,
        'email': estudiante.email,
        'fecha_nacimiento': str(estudiante.fecha_nacimiento),
        'direccion': estudiante.direccion,
        'telefono': estudiante.telefono
    }), 201
