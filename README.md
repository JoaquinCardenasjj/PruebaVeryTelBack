Backend API - Sistema de Monitoreo de Cámaras (Django)
Este es el motor de base de datos y API REST encargado de gestionar los activos (cámaras) y los registros de mantenimiento (tickets).

Instalación y Setup
Clonar el repositorio y entrar a la carpeta del backend.

Crear y activar un entorno virtual (recomendado):

Bash
python -m venv venv
# En Windows:
.\venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
Instalar dependencias:

Bash
pip install -r requirements.txt
Configurar base de datos: Asegúrate de que las credenciales en settings.py coincidan con tu servidor MySQL.

Ejecutar migraciones:

Bash
python manage.py migrate
Pruebas Unitarias (Testing)
Se ha implementado una suite de pruebas para garantizar la calidad del código y la integridad de los datos.

Ejecución de los Tests
Para correr las pruebas unitarias, ejecuta el siguiente comando en la raíz:

Bash
python manage.py test
¿Qué validan estas pruebas?
Las pruebas están diseñadas para ejecutarse en una base de datos SQLite en memoria, lo que permite una ejecución rápida y segura sin afectar los datos de producción.

Integridad de Modelos: Verifica que no se puedan crear cámaras sin datos obligatorios (como Latitud o Longitud).

Disponibilidad de API: Asegura que los endpoints retornen un estado 200 OK.

Lógica de Relaciones: Valida que cada Ticket de mantenimiento esté correctamente vinculado a una Cámara existente.

🛠️ Tecnologías Utilizadas
Django & Django Rest Framework: Para la construcción de la API.

MySQL: Base de datos principal.

SQLite: Utilizada exclusivamente para el entorno de pruebas automatizadas.

Django Filter: Para la búsqueda dinámica de registros.


# Sistema de Videovigilancia Bogotá - Backend API (Python)

Este es el núcleo de procesamiento de datos para la gestión de cámaras de seguridad y tickets de mantenimiento. Proporciona una API REST robusta consumida por un frontend en Laravel.

## 🚀 Stack Tecnológico

- **Lenguaje:** Python 3.x
- **Framework:** Django 4.2+
- **API Engine:** Django Rest Framework (DRF)
- **Base de Datos:** MySQL

## 🏗️ Arquitectura

El backend se encarga de:

1. Gestión del inventario de cámaras y lógica de geofencing (Bogotá).
2. Lógica de negocio para tickets de mantenimiento.
3. Exposición de endpoints RESTful para integración con el frontend.

## 🛠️ Instalación y Configuración

1. Clonar el repositorio.
2. Crear entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
   Instalar dependencias:
   pip install -r requirements.txt
   Configurar variables de entorno en el settings.py (MySQL).
   Ejecutar migraciones y carga de datos semilla:
   python manage.py migrate
