from rest_framework import filters,viewsets, status, serializers
from rest_framework.response import Response
from .models import Camera, Ticket
from .serializers import CameraSerializer, TicketSerializer
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend

class CameraViewSet(viewsets.ModelViewSet):
    # Mostramos solo las cámaras que siguen activas en el sistema
    queryset = Camera.objects.filter(is_deleted=False)
    serializer_class = CameraSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    
    # Filtros exactos
    filterset_fields = ['estado', 'localidad']
    
    # Búsqueda por texto libre (Modelo, Ubicación o ID)
    search_fields = ['modelo', 'ubicacion', 'id_camera']

    # Cambiamos el borrado normal por uno suave que marca la cámara como inactiva
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response(
            {"message": "Cámara eliminada correctamente (Soft Delete)"},
            status=status.HTTP_204_NO_CONTENT
        )
    
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all().order_by('-fecha_apertura')
    serializer_class = TicketSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['estado', 'tipo', 'prioridad']
    # Para el rango de fechas en tickets, usaremos un FilterSet más tarde si es necesario

    def perform_update(self, serializer):
        instance = serializer.instance
        nuevo_estado = serializer.validated_data.get('estado')

        # No permitimos que el ticket vuelva a un estado anterior
        if instance.estado == 'Resuelto' and nuevo_estado in ['Nuevo', 'En curso']:
            raise serializers.ValidationError("No se puede reabrir un ticket resuelto.")
        if instance.estado == 'En curso' and nuevo_estado == 'Nuevo':
            raise serializers.ValidationError("No se puede regresar un ticket a estado Nuevo.")

        # Si el ticket se resuelve, registramos la fecha de cierre automáticamente
        if nuevo_estado == 'Resuelto' and instance.estado != 'Resuelto':
            serializer.save(fecha_cierre=timezone.now())
        else:
            serializer.save()