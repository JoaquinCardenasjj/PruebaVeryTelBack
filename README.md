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
