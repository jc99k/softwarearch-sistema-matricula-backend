# Sistema de Matrícula Universitaria - Backend FastAPI

Este proyecto implementa un sistema de matrícula universitaria como un backend de API RESTful utilizando FastAPI, SQLAlchemy y PostgreSQL. El diseño del proyecto sigue una **Arquitectura en Capas** y se adhiere a los **Principios SOLID**, al mismo tiempo que incorpora conceptos del patrón **Model-View-Controller (MVC)** adaptados para una API.

## Arquitectura del Proyecto

El proyecto está organizado por módulos de características, lo que mejora la cohesión y la escalabilidad. Cada entidad principal (Estudiante, Profesor, Curso, etc.) tiene su propio módulo, que contiene los componentes específicos para esa entidad.

```
src/
├── modules/
│   ├── estudiante/
│   │   ├── __init__.py
│   │   ├── models.py       # Modelos SQLAlchemy específicos de Estudiante
│   │   ├── services.py     # Lógica de negocio de Estudiante
│   │   ├── controllers.py  # Endpoints API de Estudiante
│   │   └── schemas.py      # Esquemas Pydantic de Estudiante
│   ├── profesor/
│   │   ├── ...
│   ├── ... (otros módulos de entidad)
├── database.py             # Configuración de la base de datos y sesión
├── models/                 # (Vacío, los modelos se movieron a los módulos)
├── main.py                 # Aplicación principal de FastAPI
├── config.py               # Configuraciones de la aplicación
└── ...
```

### Alineación con la Arquitectura en Capas

El proyecto está claramente dividido en las siguientes capas lógicas:

1.  **Capa de Persistencia (Modelos):**
    *   **Ubicación:** `src/modules/*/models.py`
    *   **Responsabilidad:** Define la estructura de los datos y cómo se mapean a la base de datos (PostgreSQL a través de SQLAlchemy). Se encarga de las operaciones de bajo nivel de la base de datos (CRUD).
    *   **Tecnologías:** SQLAlchemy ORM.

2.  **Capa de Lógica de Negocio (Servicios):**
    *   **Ubicación:** `src/modules/*/services.py`
    *   **Responsabilidad:** Contiene las reglas de negocio centrales de la aplicación. Orquesta las interacciones entre los modelos, realiza validaciones complejas y aplica la lógica específica del dominio. Actúa como intermediario entre los controladores y los modelos.
    *   **Tecnologías:** Python puro, interactuando con los modelos SQLAlchemy.

3.  **Capa de Presentación/API (Controladores):**
    *   **Ubicación:** `src/modules/*/controllers.py`
    *   **Responsabilidad:** Maneja las solicitudes HTTP entrantes, las analiza, delega las tareas a la capa de servicios y formatea la respuesta (JSON). Define los endpoints de la API.
    *   **Tecnologías:** FastAPI `APIRouter`, Pydantic para validación de entrada/salida.

### Alineación con el Patrón Model-View-Controller (MVC)

Aunque MVC es tradicionalmente para aplicaciones con interfaz de usuario, sus principios de separación de preocupaciones se adaptan bien a las APIs RESTful:

*   **Model (Modelo):** Corresponde a la **Capa de Persistencia** (`src/modules/*/models.py`) y, en un sentido más amplio, a la **Capa de Lógica de Negocio** (`src/modules/*/services.py`), ya que ambas definen y manipulan el estado y las reglas de los datos de la aplicación.
*   **View (Vista):** En una API JSON, la "Vista" es la **respuesta JSON** que se envía al cliente. Los **Esquemas Pydantic** (`src/modules/*/schemas.py`) definen la estructura y validación de esta representación de datos.
*   **Controller (Controlador):** Corresponde directamente a la **Capa de Presentación/API** (`src/modules/*/controllers.py`). Recibe las solicitudes, las interpreta y coordina la interacción con la capa de servicios para generar la respuesta adecuada.

### Alineación con los Principios SOLID

El diseño del proyecto se adhiere firmemente a los principios SOLID:

1.  **S - Principio de Responsabilidad Única (SRP):**
    *   Cada módulo y clase tiene una única razón para cambiar. Los modelos se encargan de la persistencia, los servicios de la lógica de negocio, los controladores de las solicitudes HTTP y los esquemas de la validación y serialización de datos.

2.  **O - Principio Abierto/Cerrado (OCP):**
    *   El diseño modular permite extender la funcionalidad (añadir nuevas entidades o endpoints) sin modificar el código existente de otras entidades. Por ejemplo, añadir un nuevo módulo de `Departamento` no requiere cambios en el módulo de `Estudiante`.

3.  **L - Principio de Sustitución de Liskov (LSP):**
    *   Se aplica a través del uso de la herencia en los modelos SQLAlchemy (todos heredan de `Base`) y en los esquemas Pydantic (ej. `EstudianteCreate` hereda de `EstudianteBase`). Esto asegura que los subtipos pueden ser sustituidos por sus tipos base sin alterar la corrección del programa.

4.  **I - Principio de Segregación de Interfaces (ISP):**
    *   Los clientes (controladores) no se ven forzados a depender de interfaces que no utilizan. Esto se logra mediante esquemas Pydantic específicos para diferentes operaciones (creación, actualización, respuesta completa) y métodos de servicio enfocados que exponen solo la funcionalidad necesaria.

5.  **D - Principio de Inversión de Dependencias (DIP):**
    *   Los módulos de alto nivel (controladores) no dependen de módulos de bajo nivel (implementaciones de base de datos), sino de abstracciones (servicios y modelos). La inyección de dependencias de FastAPI (`Depends(get_db)`) es un claro ejemplo, desacoplando los controladores de los detalles de cómo se obtiene una sesión de base de datos.

## Cómo Ejecutar el Proyecto

1.  **Clonar el repositorio:**
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd softwarearch-sistema-matricula-backend
    ```

2.  **Construir y levantar los contenedores Docker:**
    ```bash
    docker-compose up --build
    ```
    Esto construirá las imágenes Docker (incluyendo la optimización multi-stage) y levantará los servicios de la aplicación web (FastAPI) y la base de datos PostgreSQL.

3.  **Acceder a la API:**
    Una vez que los contenedores estén en funcionamiento, la API de FastAPI estará disponible en:
    *   **Documentación interactiva (Swagger UI):** `http://localhost:8000/docs`
    *   **Documentación alternativa (ReDoc):** `http://localhost:8000/redoc`

    Puedes usar estas interfaces para explorar los endpoints disponibles y probar la API.

---
