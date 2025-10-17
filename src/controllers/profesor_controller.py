# src/controllers/profesor_controller.py

from flask import Blueprint, request, jsonify
from src.services.profesor_service import ProfesorService

# Layer: Controller Layer
# This layer handles the HTTP requests and responses.

profesor_bp = Blueprint('profesor_bp', __name__)

profesor_service = ProfesorService()

@profesor_bp.route('/', methods=['GET'])
def get_all_profesores():
    profesores = profesor_service.get_all_profesores()
    return jsonify([{
        'profesor_id': prof.profesor_id,
        'nombre': prof.nombre,
        'apellido': prof.apellido,
        'dni': prof.dni,
        'email': prof.email,
        'especialidad': prof.especialidad,
        'titulo_academico': prof.titulo_academico,
        'telefono': prof.telefono
    } for prof in profesores])

@profesor_bp.route('/<int:profesor_id>', methods=['GET'])
def get_profesor(profesor_id):
    profesor = profesor_service.get_profesor_by_id(profesor_id)
    if profesor:
        return jsonify({
            'profesor_id': profesor.profesor_id,
            'nombre': profesor.nombre,
            'apellido': profesor.apellido,
            'dni': profesor.dni,
            'email': profesor.email,
            'especialidad': profesor.especialidad,
            'titulo_academico': profesor.titulo_academico,
            'telefono': profesor.telefono
        })
    return jsonify({'message': 'Profesor not found'}), 404

@profesor_bp.route('/', methods=['POST'])
def create_profesor():
    data = request.get_json()
    profesor = profesor_service.create_profesor(data)
    return jsonify({
        'profesor_id': profesor.profesor_id,
        'nombre': profesor.nombre,
        'apellido': profesor.apellido,
        'dni': profesor.dni,
        'email': profesor.email,
        'especialidad': profesor.especialidad,
        'titulo_academico': profesor.titulo_academico,
        'telefono': profesor.telefono
    }), 201
