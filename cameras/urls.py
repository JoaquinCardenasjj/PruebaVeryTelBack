from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CameraViewSet, TicketViewSet
from .reports import dashboard_reports

router = DefaultRouter()
router.register(r'cameras', CameraViewSet)
router.register(r'tickets', TicketViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('dashboard-reports/', dashboard_reports, name='dashboard-reports'),
]