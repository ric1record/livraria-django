from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from core.views import AutorViewSet, CategoriaViewSet, EditoraViewSet, LivroViewSet

from media.router import router as media_router

router = DefaultRouter()
router.register(r"autores", AutorViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r"editoras", EditoraViewSet)
router.register(r"livros", LivroViewSet)

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),
    # SimpleJWT - Login
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # API DRF
    path("", include(router.urls)),
    # Media
    path("api/media/", include(media_router.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
