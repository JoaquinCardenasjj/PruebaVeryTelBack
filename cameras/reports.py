from django.db.models import Count, Avg, F, ExpressionWrapper, fields
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Camera, Ticket

@api_view(['GET'])
def dashboard_reports(request):
    # 1. Gráfica de torta: cuántas cámaras hay por estado
    # Devuelve algo como: [{'estado': 'Activa', 'total': 10}, ...]
    camaras_por_estado = Camera.objects.filter(is_deleted=False).values('estado').annotate(total=Count('estado'))

    # 2. Gráfica de barras: tickets por localidad y tipo
    # Devuelve: [{'localidad': 'Teusaquillo', 'tipo': 'Correctivo', 'total': 5}, ...]
    tickets_por_localidad = Ticket.objects.values('camera__localidad', 'tipo').annotate(total=Count('id_ticket'))

    # 3. KPIs: indicadores principales del dashboard
    total_activas = Camera.objects.filter(estado='Activa', is_deleted=False).count()
    tickets_abiertos = Ticket.objects.filter(estado__in=['Nuevo', 'En curso']).count()
    
    # Tiempo promedio de resolución en días
    # Solo consideramos tickets que ya tienen fecha de cierre
    tickets_resueltos = Ticket.objects.filter(estado='Resuelto', fecha_cierre__isnull=False).annotate(
        tiempo_resolucion=ExpressionWrapper(
            F('fecha_cierre') - F('fecha_apertura'),
            output_field=fields.DurationField()
        )
    ).aggregate(promedio=Avg('tiempo_resolucion'))

    promedio_dias = 0
    if tickets_resueltos['promedio']:
        promedio_dias = tickets_resueltos['promedio'].days

    return Response({
        "charts": {
            "camaras_estado": camaras_por_estado,
            "tickets_localidad": tickets_por_localidad,
        },
        "kpis": {
            "total_activas": total_activas,
            "tickets_abiertos": tickets_abiertos,
            "promedio_resolucion_dias": promedio_dias,
        }
    })