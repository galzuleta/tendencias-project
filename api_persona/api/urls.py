from rest_framework.routers import DefaultRouter
from api.views import PersonaViewSet, DocentesViewSet, EstudiantesViewSet

router = DefaultRouter()

router.register('api/persona', PersonaViewSet)
router.register('api/docentes', DocentesViewSet)
router.register('api/estudiantes', EstudiantesViewSet)

urlpatterns = []

urlpatterns += router.urls