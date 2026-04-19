from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Camera, Ticket
from .serializers import CameraSerializer, TicketSerializer

class CameraViewSet(viewsets.ModelViewSet):
    # Mostramos solo las cámaras que siguen activas en el sistema
    queryset = Camera.objects.filter(is_deleted=False)
    serializer_class = CameraSerializer

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