# src/controllers/pago_controller.py

from flask import Blueprint, request, jsonify
from src.services.pago_service import PagoService

# Layer: Controller Layer
# This layer handles the HTTP requests and responses.

pago_bp = Blueprint('pago_bp', __name__)

pago_service = PagoService()

@pago_bp.route('/', methods=['GET'])
def get_all_pagos():
    pagos = pago_service.get_all_pagos()
    return jsonify([{
        'pago_id': p.pago_id,
        'matricula_id': p.matricula_id,
        'fecha_pago': str(p.fecha_pago),
        'monto': str(p.monto),
        'metodo_pago': p.metodo_pago,
        'referencia': p.referencia,
        'estado': p.estado
    } for p in pagos])

@pago_bp.route('/<int:pago_id>', methods=['GET'])
def get_pago(pago_id):
    pago = pago_service.get_pago_by_id(pago_id)
    if pago:
        return jsonify({
            'pago_id': pago.pago_id,
            'matricula_id': pago.matricula_id,
            'fecha_pago': str(pago.fecha_pago),
            'monto': str(pago.monto),
            'metodo_pago': pago.metodo_pago,
            'referencia': pago.referencia,
            'estado': pago.estado
        })
    return jsonify({'message': 'Pago not found'}), 404

@pago_bp.route('/', methods=['POST'])
def create_pago():
    data = request.get_json()
    pago = pago_service.create_pago(data)
    return jsonify({
        'pago_id': pago.pago_id,
        'matricula_id': pago.matricula_id,
        'fecha_pago': str(pago.fecha_pago),
        'monto': str(pago.monto),
        'metodo_pago': pago.metodo_pago,
        'referencia': pago.referencia,
        'estado': pago.estado
    }), 201
