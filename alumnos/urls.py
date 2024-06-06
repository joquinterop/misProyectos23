#from django.conf.urls import url

from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('listadoSQL', views.listadoSQL,name='listadoSQL'),
    path('listado_generos',views.lista_generos,name='lista_generos'),
    path('crud',views.crud,name='crud'),
    path('alumnosAdd',views.alumno_agregar,name='alumnoAdd'),
]

#La funcion PATH en su estructura separa los parametros por comas ()