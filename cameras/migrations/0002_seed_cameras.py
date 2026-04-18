from django.db import migrations

def seed_data(apps, schema_editor):
    Camera = apps.get_model('cameras', 'Camera')
    
    cameras_data = [
        {"id_camera": "CAM-001", "modelo": "Cámara PTZ Hikvision DS-2DE4425IW", "ubicacion": "Parque Simón Bolívar", "latitud": 4.658, "longitud": -74.093, "estado": "Activa", "ultimo_mantenimiento": "2025-11-15", "localidad": "Teusaquillo"},
        {"id_camera": "CAM-002", "modelo": "Cámara Fija Dahua IPC-HFW5442H", "ubicacion": "Portal Américas TransMilenio", "latitud": 4.626, "longitud": -74.153, "estado": "Activa", "ultimo_mantenimiento": "2025-08-22", "localidad": "Kennedy"},
        {"id_camera": "CAM-003", "modelo": "Cámara PTZ Axis Q6135-LE", "ubicacion": "Plaza de Bolívar", "latitud": 4.598, "longitud": -74.076, "estado": "En Mantenimiento", "ultimo_mantenimiento": "2026-01-10", "localidad": "Santa Fe"},
        {"id_camera": "CAM-004", "modelo": "Cámara Fija Hikvision DS-2CD2T47G2", "ubicacion": "Estación Calle 72 TM", "latitud": 4.666, "longitud": -74.058, "estado": "Activa", "ultimo_mantenimiento": "2024-12-05", "localidad": "Chapinero"},
        {"id_camera": "CAM-005", "modelo": "Cámara PTZ Dahua SD6AL245XA", "ubicacion": "CAI Kennedy Central", "latitud": 4.630, "longitud": -74.159, "estado": "Inactiva", "ultimo_mantenimiento": "2026-03-01", "localidad": "Kennedy"},
        {"id_camera": "CAM-006", "modelo": "Cámara Fija Axis P1448-LE", "ubicacion": "Centro Comercial Gran Estación", "latitud": 4.649, "longitud": -74.108, "estado": "Activa", "ultimo_mantenimiento": "2025-06-18", "localidad": "Teusaquillo"},
        {"id_camera": "CAM-007", "modelo": "Cámara PTZ Hikvision DS-2DE7A432IW", "ubicacion": "Alcaldía Local Usaquén", "latitud": 4.695, "longitud": -74.032, "estado": "Activa", "ultimo_mantenimiento": "2025-09-30", "localidad": "Usaquén"},
        {"id_camera": "CAM-008", "modelo": "Cámara Fija Dahua IPC-HFW3849T1", "ubicacion": "Terminal de Transporte Salitre", "latitud": 4.653, "longitud": -74.117, "estado": "En Mantenimiento", "ultimo_mantenimiento": "2026-02-14", "localidad": "Fontibón"},
        {"id_camera": "CAM-009", "modelo": "Cámara PTZ Axis Q6318-LE", "ubicacion": "Estación Héroes TransMilenio", "latitud": 4.649, "longitud": -74.068, "estado": "Activa", "ultimo_mantenimiento": "2025-07-25", "localidad": "Chapinero"},
        {"id_camera": "CAM-010", "modelo": "Cámara Fija Hikvision DS-2CD2T86G2", "ubicacion": "Parque El Virrey", "latitud": 4.673, "longitud": -74.049, "estado": "Activa", "ultimo_mantenimiento": "2025-04-12", "localidad": "Chapinero"},
        {"id_camera": "CAM-011", "modelo": "Cámara PTZ Dahua SD8A840XA-HNF", "ubicacion": "CAI Chapinero Central", "latitud": 4.644, "longitud": -74.063, "estado": "Inactiva", "ultimo_mantenimiento": "2026-01-28", "localidad": "Chapinero"},
        {"id_camera": "CAM-012", "modelo": "Cámara Fija Axis M3116-LVE", "ubicacion": "Biblioteca Virgilio Barco", "latitud": 4.659, "longitud": -74.099, "estado": "Activa", "ultimo_mantenimiento": "2025-10-05", "localidad": "Teusaquillo"},
        {"id_camera": "CAM-013", "modelo": "Cámara PTZ Hikvision DS-2DE5425IW", "ubicacion": "Portal Norte TransMilenio", "latitud": 4.763, "longitud": -74.044, "estado": "Activa", "ultimo_mantenimiento": "2025-05-20", "localidad": "Usaquén"},
        {"id_camera": "CAM-014", "modelo": "Cámara Fija Dahua IPC-HFW5541E", "ubicacion": "Hospital Simón Bolívar", "latitud": 4.746, "longitud": -74.039, "estado": "En Mantenimiento", "ultimo_mantenimiento": "2026-03-15", "localidad": "Usaquén"},
        {"id_camera": "CAM-015", "modelo": "Cámara PTZ Axis Q6315-LE", "ubicacion": "Centro Histórico La Candelaria", "latitud": 4.596, "longitud": -74.072, "estado": "Activa", "ultimo_mantenimiento": "2025-12-01", "localidad": "La Candelaria"},
        {"id_camera": "CAM-016", "modelo": "Cámara Fija Hikvision DS-2CD2H86G2", "ubicacion": "Estación Av. Jiménez TM", "latitud": 4.601, "longitud": -74.074, "estado": "Activa", "ultimo_mantenimiento": "2025-03-14", "localidad": "Santa Fe"},
        {"id_camera": "CAM-017", "modelo": "Cámara PTZ Dahua SD6AL830XA", "ubicacion": "Parque Nacional Enrique Olaya", "latitud": 4.622, "longitud": -74.063, "estado": "Activa", "ultimo_mantenimiento": "2025-11-08", "localidad": "Santa Fe"},
        {"id_camera": "CAM-018", "modelo": "Cámara Fija Axis P3267-LVE", "ubicacion": "Terminal Sur de Transporte", "latitud": 4.596, "longitud": -74.129, "estado": "Inactiva", "ultimo_mantenimiento": "2026-02-20", "localidad": "Fontibón"},
        {"id_camera": "CAM-019", "modelo": "Cámara PTZ Hikvision DS-2DE7A825IW", "ubicacion": "Portal Tunal TransMilenio", "latitud": 4.576, "longitud": -74.131, "estado": "Activa", "ultimo_mantenimiento": "2025-08-15", "localidad": "Tunjuelito"},
        {"id_camera": "CAM-020", "modelo": "Cámara Fija Dahua IPC-HFW5842E", "ubicacion": "CAI Santa Fe Centro", "latitud": 4.609, "longitud": -74.078, "estado": "En Mantenimiento", "ultimo_mantenimiento": "2026-04-01", "localidad": "Santa Fe"},
    ]
    
    for cam in cameras_data:
        Camera.objects.create(**cam)

class Migration(migrations.Migration):

    dependencies = [
        ('cameras', '0001_initial'), # Asegúrate de que este nombre coincida con tu primera migración
    ]

    operations = [
        migrations.RunPython(seed_data),
    ]