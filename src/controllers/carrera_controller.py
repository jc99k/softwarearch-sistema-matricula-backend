# src/controllers/carrera_controller.py

from flask import Blueprint, request, jsonify
from src.services.carrera_service import CarreraService

# Layer: Controller Layer
# This layer handles the HTTP requests and responses.

carrera_bp = Blueprint('carrera_bp', __name__)

carrera_service = CarreraService()

@carrera_bp.route('/', methods=['GET'])
def get_all_carreras():
    carreras = carrera_service.get_all_carreras()
    return jsonify([{
        'carrera_id': car.carrera_id,
        'facultad_id': car.facultad_id,
        'nombre': car.nombre,
        'descripcion': car.descripcion,
        'duracion_semestres': car.duracion_semestres,
        'titulo_otorgado': car.titulo_otorgado
    } for car in carreras])

@carrera_bp.route('/<int:carrera_id>', methods=['GET'])
def get_carrera(carrera_id):
    carrera = carrera_service.get_carrera_by_id(carrera_id)
    if carrera:
        return jsonify({
            'carrera_id': carrera.carrera_id,
            'facultad_id': carrera.facultad_id,
            'nombre': carrera.nombre,
            'descripcion': carrera.descripcion,
            'duracion_semestres': carrera.duracion_semestres,
            'titulo_otorgado': carrera.titulo_otorgado
        })
    return jsonify({'message': 'Carrera not found'}), 404

@carrera_bp.route('/', methods=['POST'])
def create_carrera():
    data = request.get_json()
    carrera = carrera_service.create_carrera(data)
    return jsonify({
        'carrera_id': carrera.carrera_id,
        'facultad_id': carrera.facultad_id,
        'nombre': carrera.nombre,
        'descripcion': carrera.descripcion,
        'duracion_semestres': carrera.duracion_semestres,
        'titulo_otorgado': carrera.titulo_otorgado
    }), 201
