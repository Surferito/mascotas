from django.conf.urls import url, include
from apps.registro.views import RegistroUsuario


urlpatterns = [
    url(r'^$', RegistroUsuario.as_view(), name="registro"),
]