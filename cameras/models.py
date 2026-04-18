from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Camera(models.Model):
    # Identificador único de la cámara usado como clave primaria
    id_camera = models.CharField(max_length=50, primary_key=True, verbose_name="ID Cámara")
    modelo = models.CharField(max_length=150)
    ubicacion = models.TextField()
    
    # Coordenadas válidas dentro del área de Bogotá
    latitud = models.FloatField(
        validators=[MinValueValidator(4.4), MaxValueValidator(4.9)]
    )
    longitud = models.FloatField(
        validators=[MinValueValidator(-74.3), MaxValueValidator(-73.9)]
    )
    
    ESTADO_CHOICES = [
        ('Activa', 'Activa'),
        ('Inactiva', 'Inactiva'),
        ('En Mantenimiento', 'En Mantenimiento'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Activa')
    
    ultimo_mantenimiento = models.DateField(null=True, blank=True)
    localidad = models.CharField(max_length=100)
    
    # Marca si la cámara ya no está activa en el sistema, en vez de borrarla físicamente
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id_camera} - {self.modelo}"

class Ticket(models.Model):
    id_ticket = models.CharField(max_length=50, primary_key=True, verbose_name="ID Ticket")
    
    # Cada ticket está vinculado a una cámara mediante su ID
    camera = models.ForeignKey(
        Camera, 
        on_delete=models.CASCADE, 
        related_name='tickets',
        to_field='id_camera'
    )
    
    TIPO_CHOICES = [
        ('Correctivo', 'Correctivo'),
        ('Preventivo', 'Preventivo'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    
    descripcion = models.TextField()
    
    ESTADO_TICKET_CHOICES = [
        ('Nuevo', 'Nuevo'),
        ('En curso', 'En curso'),
        ('Resuelto', 'Resuelto'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADO_TICKET_CHOICES, default='Nuevo')
    
    PRIORIDAD_CHOICES = [
        ('Crítica', 'Crítica'),
        ('Alta', 'Alta'),
        ('Media', 'Media'),
        ('Baja', 'Baja'),
    ]
    prioridad = models.CharField(max_length=20, choices=PRIORIDAD_CHOICES)
    
    fecha_apertura = models.DateTimeField(auto_now_add=True)
    fecha_cierre = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.id_ticket} - {self.camera_id}"