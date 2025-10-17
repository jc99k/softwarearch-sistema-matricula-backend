# src/controllers/curso_controller.py

from flask import Blueprint, request, jsonify
from src.services.curso_service import CursoService

# Layer: Controller Layer
# This layer handles the HTTP requests and responses.

curso_bp = Blueprint('curso_bp', __name__)

curso_service = CursoService()

@curso_bp.route('/', methods=['GET'])
def get_all_cursos():
    cursos = curso_service.get_all_cursos()
    return jsonify([{
        'curso_id': cur.curso_id,
        'carrera_id': cur.carrera_id,
        'codigo': cur.codigo,
        'nombre': cur.nombre,
        'descripcion': cur.descripcion,
        'creditos': cur.creditos,
        'nivel_semestre': cur.nivel_semestre
    } for cur in cursos])

@curso_bp.route('/<int:curso_id>', methods=['GET'])
def get_curso(curso_id):
    curso = curso_service.get_curso_by_id(curso_id)
    if curso:
        return jsonify({
            'curso_id': curso.curso_id,
            'carrera_id': curso.carrera_id,
            'codigo': curso.codigo,
            'nombre': curso.nombre,
            'descripcion': curso.descripcion,
            'creditos': curso.creditos,
            'nivel_semestre': curso.nivel_semestre
        })
    return jsonify({'message': 'Curso not found'}), 404

@curso_bp.route('/', methods=['POST'])
def create_curso():
    data = request.get_json()
    curso = curso_service.create_curso(data)
    return jsonify({
        'curso_id': curso.curso_id,
        'carrera_id': curso.carrera_id,
        'codigo': curso.codigo,
        'nombre': curso.nombre,
        'descripcion': curso.descripcion,
        'creditos': curso.creditos,
        'nivel_semestre': curso.nivel_semestre
    }), 201
