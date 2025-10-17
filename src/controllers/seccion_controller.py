# src/controllers/seccion_controller.py

from flask import Blueprint, request, jsonify
from src.services.seccion_service import SeccionService

# Layer: Controller Layer
# This layer handles the HTTP requests and responses.

seccion_bp = Blueprint('seccion_bp', __name__)

seccion_service = SeccionService()

@seccion_bp.route('/', methods=['GET'])
def get_all_secciones():
    secciones = seccion_service.get_all_secciones()
    return jsonify([{
        'seccion_id': sec.seccion_id,
        'curso_id': sec.curso_id,
        'profesor_id': sec.profesor_id,
        'codigo': sec.codigo,
        'capacidad_maxima': sec.capacidad_maxima,
        'aula': sec.aula,
        'horario': sec.horario,
        'dias': sec.dias,
        'periodo_academico': sec.periodo_academico,
        'fecha_inicio': str(sec.fecha_inicio),
        'fecha_fin': str(sec.fecha_fin)
    } for sec in secciones])

@seccion_bp.route('/<int:seccion_id>', methods=['GET'])
def get_seccion(seccion_id):
    seccion = seccion_service.get_seccion_by_id(seccion_id)
    if seccion:
        return jsonify({
            'seccion_id': seccion.seccion_id,
            'curso_id': seccion.curso_id,
            'profesor_id': seccion.profesor_id,
            'codigo': seccion.codigo,
            'capacidad_maxima': seccion.capacidad_maxima,
            'aula': seccion.aula,
            'horario': seccion.horario,
            'dias': seccion.dias,
            'periodo_academico': seccion.periodo_academico,
            'fecha_inicio': str(seccion.fecha_inicio),
            'fecha_fin': str(seccion.fecha_fin)
        })
    return jsonify({'message': 'Seccion not found'}), 404

@seccion_bp.route('/', methods=['POST'])
def create_seccion():
    data = request.get_json()
    seccion = seccion_service.create_seccion(data)
    return jsonify({
        'seccion_id': seccion.seccion_id,
        'curso_id': seccion.curso_id,
        'profesor_id': seccion.profesor_id,
        'codigo': seccion.codigo,
        'capacidad_maxima': seccion.capacidad_maxima,
        'aula': seccion.aula,
        'horario': seccion.horario,
        'dias': seccion.dias,
        'periodo_academico': seccion.periodo_academico,
        'fecha_inicio': str(seccion.fecha_inicio),
        'fecha_fin': str(seccion.fecha_fin)
    }), 201
