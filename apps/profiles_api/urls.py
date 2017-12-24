from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cabify', views.Cabify.as_view(), name='cabify'),

]