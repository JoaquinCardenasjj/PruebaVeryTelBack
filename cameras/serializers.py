from rest_framework import serializers
from .models import Camera, Ticket



class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = '__all__'
        
    def update(self, instance, validated_data):
        # Si el cliente intenta cambiar el ID de la cámara en una actualización,
        # lo quitamos para mantener siempre el mismo identificador original.
        validated_data.pop('id_camera', None)
        return super().update(instance, validated_data)
    
    # Esto incluirá la lista de tickets dentro del JSON de la cámara
    tickets = TicketSerializer(many=True, read_only=True)

    class Meta:
        model = Camera
        fields = [
            'id_camera', 'modelo', 'ubicacion', 'latitud', 'longitud', 
            'estado', 'ultimo_mantenimiento', 'localidad', 'is_deleted', 'tickets'
        ]