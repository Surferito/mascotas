from django.conf.urls import url, include
from rest_framework import routers
from apps.adopcion.views import index, SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete,\
    PersonaViewSet, snippet_detail

router = routers.DefaultRouter()
router.register(r'personas', PersonaViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^snippets/(?P<pk>[0-9]+)$', snippet_detail),
]

'''urlpatterns = [
    url(r'^$', index),
    url(r'solicitud/listar$', SolicitudList.as_view(), name = 'solicitud_listar'),
    url(r'solicitud/nueva$', SolicitudCreate.as_view(), name = 'solicitud_crear'),
    url(r'^solicitud/editar/(?P<pk>\d+)$', SolicitudUpdate.as_view(), name='solicitud_editar'),
    url(r'^solicitud/eliminar/(?P<pk>\d+)$', SolicitudDelete.as_view(), name='solicitud_eliminar'),
]'''