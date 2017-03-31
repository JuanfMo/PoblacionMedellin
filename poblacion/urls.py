from django.conf.urls import url
from . import views


app_name = 'poblacion'

urlpatterns = [

    url(r'^agregar/$', views.agregar, name='agregar'),
    url(r'^$', views.mostrar, name='index'),
]
