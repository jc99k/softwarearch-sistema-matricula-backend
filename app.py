# app.py

from flask import Flask
from config import Config
from src.db import db
from src.models import models

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Layer: Persistence Layer
    # Initialize extensions
    db.init_app(app)

    with app.app_context():
        # Create database tables
        db.create_all()

    # Layer: Controller Layer
    # Register blueprints
    from src.controllers.estudiante_controller import estudiante_bp
    app.register_blueprint(estudiante_bp, url_prefix='/api/estudiantes')

    from src.controllers.profesor_controller import profesor_bp
    app.register_blueprint(profesor_bp, url_prefix='/api/profesores')

    from src.controllers.facultad_controller import facultad_bp
    app.register_blueprint(facultad_bp, url_prefix='/api/facultades')

    from src.controllers.carrera_controller import carrera_bp
    app.register_blueprint(carrera_bp, url_prefix='/api/carreras')

    from src.controllers.curso_controller import curso_bp
    app.register_blueprint(curso_bp, url_prefix='/api/cursos')

    from src.controllers.seccion_controller import seccion_bp
    app.register_blueprint(seccion_bp, url_prefix='/api/secciones')

    from src.controllers.matricula_controller import matricula_bp
    app.register_blueprint(matricula_bp, url_prefix='/api/matriculas')

    from src.controllers.pago_controller import pago_bp
    app.register_blueprint(pago_bp, url_prefix='/api/pagos')

    from src.controllers.calificacion_controller import calificacion_bp
    app.register_blueprint(calificacion_bp, url_prefix='/api/calificaciones')

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)