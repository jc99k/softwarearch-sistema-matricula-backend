# src/controllers/facultad_controller.py

from flask import Blueprint, request, jsonify
from src.services.facultad_service import FacultadService

# Layer: Controller Layer
# This layer handles the HTTP requests and responses.

facultad_bp = Blueprint('facultad_bp', __name__)

facultad_service = FacultadService()

@facultad_bp.route('/', methods=['GET'])
def get_all_facultades():
    facultades = facultad_service.get_all_facultades()
    return jsonify([{
        'facultad_id': fac.facultad_id,
        'nombre': fac.nombre,
        'descripcion': fac.descripcion,
        'ubicacion': fac.ubicacion,
        'decano': fac.decano
    } for fac in facultades])

@facultad_bp.route('/<int:facultad_id>', methods=['GET'])
def get_facultad(facultad_id):
    facultad = facultad_service.get_facultad_by_id(facultad_id)
    if facultad:
        return jsonify({
            'facultad_id': facultad.facultad_id,
            'nombre': facultad.nombre,
            'descripcion': facultad.descripcion,
            'ubicacion': facultad.ubicacion,
            'decano': facultad.decano
        })
    return jsonify({'message': 'Facultad not found'}), 404

@facultad_bp.route('/', methods=['POST'])
def create_facultad():
    data = request.get_json()
    facultad = facultad_service.create_facultad(data)
    return jsonify({
        'facultad_id': facultad.facultad_id,
        'nombre': facultad.nombre,
        'descripcion': facultad.descripcion,
        'ubicacion': facultad.ubicacion,
        'decano': facultad.decano
    }), 201
