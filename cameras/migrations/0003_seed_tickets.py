from django.db import migrations
from datetime import datetime

def seed_tickets(apps, schema_editor):
    Ticket = apps.get_model('cameras', 'Ticket')
    Camera = apps.get_model('cameras', 'Camera')
    
    tickets_data = [
        {"id_ticket": "TKT-2026-001", "camera_id": "CAM-003", "tipo": "Correctivo", "descripcion": "Falla en motor de rotación PTZ", "estado": "En curso", "prioridad": "Alta", "fecha_apertura": "2026-01-12", "fecha_cierre": None},
        {"id_ticket": "TKT-2026-002", "camera_id": "CAM-005", "tipo": "Correctivo", "descripcion": "Sin señal de video - fuente dañada", "estado": "Nuevo", "prioridad": "Crítica", "fecha_apertura": "2026-03-02", "fecha_cierre": None},
        {"id_ticket": "TKT-2026-003", "camera_id": "CAM-008", "tipo": "Preventivo", "descripcion": "Limpieza de domo y revisión de cableado", "estado": "En curso", "prioridad": "Media", "fecha_apertura": "2026-02-15", "fecha_cierre": None},
        {"id_ticket": "TKT-2026-004", "camera_id": "CAM-014", "tipo": "Correctivo", "descripcion": "Imagen borrosa - lente desenfocado", "estado": "En curso", "prioridad": "Alta", "fecha_apertura": "2026-03-16", "fecha_cierre": None},
        {"id_ticket": "TKT-2026-005", "camera_id": "CAM-011", "tipo": "Correctivo", "descripcion": "Corte de fibra óptica en poste", "estado": "Nuevo", "prioridad": "Crítica", "fecha_apertura": "2026-01-30", "fecha_cierre": None},
        {"id_ticket": "TKT-2026-006", "camera_id": "CAM-020", "tipo": "Preventivo", "descripcion": "Actualización de firmware v4.2.1", "estado": "En curso", "prioridad": "Media", "fecha_apertura": "2026-04-02", "fecha_cierre": None},
        {"id_ticket": "TKT-2026-007", "camera_id": "CAM-018", "tipo": "Correctivo", "descripcion": "Vandalismo - carcasa rota", "estado": "Nuevo", "prioridad": "Alta", "fecha_apertura": "2026-02-22", "fecha_cierre": None},
        {"id_ticket": "TKT-2026-008", "camera_id": "CAM-001", "tipo": "Preventivo", "descripcion": "Inspección trimestral programada", "estado": "Resuelto", "prioridad": "Baja", "fecha_apertura": "2025-12-10", "fecha_cierre": "2025-12-12"},
        {"id_ticket": "TKT-2026-009", "camera_id": "CAM-006", "tipo": "Correctivo", "descripcion": "Sobrecalentamiento por exposición solar", "estado": "Resuelto", "prioridad": "Media", "fecha_apertura": "2025-07-20", "fecha_cierre": "2025-07-23"},
        {"id_ticket": "TKT-2026-010", "camera_id": "CAM-010", "tipo": "Preventivo", "descripcion": "Reemplazo preventivo de fuente PoE", "estado": "Resuelto", "prioridad": "Baja", "fecha_apertura": "2025-05-01", "fecha_cierre": "2025-05-03"},
        {"id_ticket": "TKT-2026-011", "camera_id": "CAM-002", "tipo": "Correctivo", "descripcion": "Pérdida intermitente de conexión", "estado": "Resuelto", "prioridad": "Alta", "fecha_apertura": "2025-09-15", "fecha_cierre": "2025-09-18"},
        {"id_ticket": "TKT-2026-012", "camera_id": "CAM-013", "tipo": "Preventivo", "descripcion": "Calibración de preset de patrullaje", "estado": "Resuelto", "prioridad": "Media", "fecha_apertura": "2025-06-10", "fecha_cierre": "2025-06-11"},
        {"id_ticket": "TKT-2026-013", "camera_id": "CAM-007", "tipo": "Correctivo", "descripcion": "Falla en IR - visión nocturna", "estado": "Resuelto", "prioridad": "Alta", "fecha_apertura": "2025-10-20", "fecha_cierre": "2025-10-24"},
        {"id_ticket": "TKT-2026-014", "camera_id": "CAM-009", "tipo": "Preventivo", "descripcion": "Limpieza semestral y ajuste de ángulo", "estado": "Resuelto", "prioridad": "Baja", "fecha_apertura": "2025-08-05", "fecha_cierre": "2025-08-06"},
        {"id_ticket": "TKT-2026-015", "camera_id": "CAM-015", "tipo": "Correctivo", "descripcion": "Interferencia eléctrica en imagen", "estado": "Resuelto", "prioridad": "Media", "fecha_apertura": "2026-01-05", "fecha_cierre": "2026-01-09"},
    ]

    for tkt in tickets_data:
        # Convertimos las fechas de string a objeto date/datetime para Django
        apertura = datetime.strptime(tkt['fecha_apertura'], '%Y-%m-%d')
        cierre = datetime.strptime(tkt['fecha_cierre'], '%Y-%m-%d') if tkt['fecha_cierre'] else None
        
        Ticket.objects.create(
            id_ticket=tkt['id_ticket'],
            camera_id=tkt['camera_id'],
            tipo=tkt['tipo'],
            descripcion=tkt['descripcion'],
            estado=tkt['estado'],
            prioridad=tkt['prioridad'],
            fecha_apertura=apertura,
            fecha_cierre=cierre
        )

class Migration(migrations.Migration):

    dependencies = [
        ('cameras', '0002_seed_cameras'), # Asegúrate que dependa de la carga de cámaras
    ]

    operations = [
        migrations.RunPython(seed_tickets),
    ]