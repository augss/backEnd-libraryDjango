from rest_framework.routers import DefaultRouter

from user import views

app_name = "user"

router = DefaultRouter()
router.register("usuarios", views.UsuarioViewSet)
