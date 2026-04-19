from rest_framework import serializers
from .models import Camera, Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class CameraSerializer(serializers.ModelSerializer):
    # 1. DEBES DECLARAR EL CAMPO AQUÍ
    tickets_abiertos_count = serializers.SerializerMethodField()
    
    # Esto incluirá la lista completa de tickets (opcional, pero está en tus requerimientos)
    tickets = TicketSerializer(many=True, read_only=True)

    class Meta:
        model = Camera
        # 2. DEBES AGREGARLO A LA LISTA DE FIELDS
        fields = [
            'id_camera', 'modelo', 'ubicacion', 'latitud', 'longitud', 
            'estado', 'ultimo_mantenimiento', 'localidad', 'is_deleted', 
            'tickets', 'tickets_abiertos_count'
        ]

    # 3. EL MÉTODO DEBE LLAMARSE IGUAL QUE EL CAMPO (con prefijo get_)
    def get_tickets_abiertos_count(self, obj):
        # Filtramos solo los tickets que no están resueltos
        return obj.tickets.filter(estado__in=['Nuevo', 'En curso']).count()
        
    def update(self, instance, validated_data):
        # Protegemos el ID para que no sea editable
        validated_data.pop('id_camera', None)
        return super().update(instance, validated_data)