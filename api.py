from rest_framework import routers
from Galaxia import api_views as myapp_views


router = routers.DefaultRouter()
router.register("personas", myapp_views.PersonaViewSet)
router.register("planetas", myapp_views.PlanetaViewSet)
router.register("especies", myapp_views.EspecieViewSet)
router.register("vehiculos", myapp_views.VehiculoViewSet)
router.register("naves", myapp_views.NaveViewSet)
router.register("peliculas", myapp_views.PeliculaViewSet)
