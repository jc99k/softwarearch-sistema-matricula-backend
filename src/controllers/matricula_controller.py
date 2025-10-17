# src/controllers/matricula_controller.py

from flask import Blueprint, request, jsonify
from src.services.matricula_service import MatriculaService

# Layer: Controller Layer
# This layer handles the HTTP requests and responses.

matricula_bp = Blueprint('matricula_bp', __name__)

matricula_service = MatriculaService()

@matricula_bp.route('/', methods=['GET'])
def get_all_matriculas():
    matriculas = matricula_service.get_all_matriculas()
    return jsonify([{
        'matricula_id': mat.matricula_id,
        'estudiante_id': mat.estudiante_id,
        'seccion_id': mat.seccion_id,
        'fecha_matricula': str(mat.fecha_matricula),
        'estado': mat.estado,
        'costo': str(mat.costo),
        'metodo_pago': mat.metodo_pago
    } for mat in matriculas])

@matricula_bp.route('/<int:matricula_id>', methods=['GET'])
def get_matricula(matricula_id):
    matricula = matricula_service.get_matricula_by_id(matricula_id)
    if matricula:
        return jsonify({
            'matricula_id': matricula.matricula_id,
            'estudiante_id': matricula.estudiante_id,
            'seccion_id': matricula.seccion_id,
            'fecha_matricula': str(matricula.fecha_matricula),
            'estado': matricula.estado,
            'costo': str(matricula.costo),
            'metodo_pago': matricula.metodo_pago
        })
    return jsonify({'message': 'Matricula not found'}), 404

@matricula_bp.route('/', methods=['POST'])
def create_matricula():
    data = request.get_json()
    matricula = matricula_service.create_matricula(data)
    return jsonify({
        'matricula_id': matricula.matricula_id,
        'estudiante_id': matricula.estudiante_id,
        'seccion_id': matricula.seccion_id,
        'fecha_matricula': str(matricula.fecha_matricula),
        'estado': matricula.estado,
        'costo': str(matricula.costo),
        'metodo_pago': matricula.metodo_pago
    }), 201
