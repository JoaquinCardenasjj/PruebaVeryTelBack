1. Stack Elegido
Para el desarrollo de esta solución se optó por un stack Decoupled (Desacoplado):

Backend: Python 3.x con Django REST Framework (DRF).

Razón: La robustez de Django para el manejo de modelos y la facilidad de DRF para exponer una API limpia y estandarizada. 
Su sistema de migraciones es ideal para gestionar cambios en la base de datos de forma segura.

Frontend: PHP con Laravel.

Razón: Aprovechando que tenia un sitio web publicado en ese lenguaje y con una plantilla de navegacion opte, sin embargo podria haberlo echo
sin problema con angular u otro lenguaje front end.

Base de Datos: MySQL aproveche la disponibilidad tambien de un servidor que tengo personal, pero de igual forma pude haberlo desarrollado en 
otra base de datos como Sql server, Oracle o PostgreSQL.

Razón: Soporte sólido para integridad referencial y escalabilidad.

Librerías Principales:

Backend: django-filter (filtros dinámicos),django-restFramework django.


2. Desarrollo de la Solución
El proyecto se organizó siguiendo una arquitectura de API First. Primero se definió el contrato de datos y luego se procedió a la implementación.

Organización y Patrones
Patrón Repository/Service (implícito): Lógica de negocio centralizada en los ViewSets de Django para mantener los modelos limpios.
de igual forma trate de mantener una arquitectura en capas esto para mantener la escalabilidad y mantenibilidad como por ejemplo:
Capa de Datos (Data Layer) - El model.py
Capa de Transformación y Validación (Domain/Contract Layer) - El serializer.py
Capa de Lógica de Negocio y Control (Application Layer) - El view.py


Separación de Concerns: Los reportes de dashboard se separaron en un archivo reports.py independiente para no sobrecargar las vistas del CRUD.

Diagrama de Arquitectura

[ CLIENTE: Navegador ]
	   |
	   v
[ FRONTEND: Laravel ]  <--- Consume JSON ---+
(Renderiza UI, Mapas, Graficas)             |
	   |                                  |
	   v                                  |
[ BACKEND: Django REST ] -------------------+
(Modelos, Validaciones, Auth)
	   |
	   v
[ DB: PostgreSQL / MySQL ]

 3. Uso de Herramientas de IAEn este proyecto se utilizó Gemini (Google AI) como asistente de arquitectura y desarrollo.Tareas realizadas: Generación de estructuras base para modelos,
 ayuda en la configuración de despliegue en entornos cPanel y optimización de consultas de agregación para el dashboard.
 Correcciones necesarias: Se tuvo que ajustar manualmente la lógica del perform_update en los ViewSets. tambien Copilot en Visual Code fue de 
 ayuda para mantener la documentacion del codigo y revisar validaciones
 4. Decisiones de Diseño (Trade-offs)ID Manual vs Auto-incremental: Se decidió usar un CharField para id_camera
 (e.g., CAM-001) para facilitar la búsqueda por parte de los operadores, asumiendo el compromiso de validar manualmente 
 la unicidad.Soft Delete: Se implementó is_deleted = BooleanField en lugar de un borrado físico para preservar el historial
 de tickets asociados, cumpliendo con la integridad referencial. ¿Qué haría diferente con más tiempo? 
 Implementar autenticación basada en JWT (JSON Web Tokens).Agregar Redis para cachear los reportes del Dashboard,
 ya que las agregaciones pueden volverse costosas con miles de registros.Dockerizar la solución completa para un despliegue más rápido.
 5. Tiempo Invertido (Estimado)
 MóduloTiempo EstimadoConfiguración de entorno y Base de Datos 2 horas
 Backend: CRUD Cámaras y Soft Delete 1.5 horas
 Backend: CRUD Tickets y Lógica de Estados 1.5 horas
 Backend: Endpoints de Reportes y KPIs 1 horas 
 Total 5 horas
 Publicacion codigo backend 3.5 horas
 
	  
