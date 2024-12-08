from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import ClienteViewSet, PetViewSet, RacaViewSet, AtendimentoViewSet, UsuarioViewSet, \
    EnderecoViewSet
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'endereços', EnderecoViewSet)
router.register(r'pets', PetViewSet)
router.register(r'racas', RacaViewSet)
router.register(r'atendimentos', AtendimentoViewSet)

def home(request):
    return HttpResponse("<h1>Bem-vindo à API do Pet Shop!</h1><p>Use a rota <code>/api/</code> para acessar os endpoints.</p>")

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
