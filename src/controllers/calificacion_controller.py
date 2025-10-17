# src/controllers/calificacion_controller.py

from flask import Blueprint, request, jsonify
from src.services.calificacion_service import CalificacionService

# Layer: Controller Layer
# This layer handles the HTTP requests and responses.

calificacion_bp = Blueprint('calificacion_bp', __name__)

calificacion_service = CalificacionService()

@calificacion_bp.route('/', methods=['GET'])
def get_all_calificaciones():
    calificaciones = calificacion_service.get_all_calificaciones()
    return jsonify([{
        'calificacion_id': cal.calificacion_id,
        'matricula_id': cal.matricula_id,
        'nota': str(cal.nota),
        'observacion': cal.observacion
    } for cal in calificaciones])

@calificacion_bp.route('/<int:calificacion_id>', methods=['GET'])
def get_calificacion(calificacion_id):
    calificacion = calificacion_service.get_calificacion_by_id(calificacion_id)
    if calificacion:
        return jsonify({
            'calificacion_id': calificacion.calificacion_id,
            'matricula_id': calificacion.matricula_id,
            'nota': str(calificacion.nota),
            'observacion': calificacion.observacion
        })
    return jsonify({'message': 'Calificacion not found'}), 404

@calificacion_bp.route('/', methods=['POST'])
def create_calificacion():
    data = request.get_json()
    calificacion = calificacion_service.create_calificacion(data)
    return jsonify({
        'calificacion_id': calificacion.calificacion_id,
        'matricula_id': calificacion.matricula_id,
        'nota': str(calificacion.nota),
        'observacion': calificacion.observacion
    }), 201
