from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="inicio"),

    path('clientes/', clientes, name="clientes"),
    path('ropa/', ropa, name="ropa"),

    path('cliente_form/', clienteForm, name="cliente_form"),
    path('cliente_form2/', clienteForm2, name="cliente_form2"),

    path('buscar_comision/', buscarComision, name="buscar_comision"),
    path('buscar2/', buscar2, name="buscar2"),
#_______________________
    path('juguetes/', juguetes, name="juguetes"),
    path('update_juguete/<id_juguete>/', updateJuguete, name="update_juguete"),
    path('delete_juguete/<id_juguete>/', deletejuguete, name="delete_juguete"),
    path('create_juguete/', createjuguete, name="create_juguete"),

    path('hogar/', HogarList.as_view(), name="hogar"),
    path('create_hogar/', HogarCreate.as_view(), name="create_hogar"),
    path('detail_hogar/<int:pk>/', HogarDetail.as_view(), name="detail_hogar"),
    path('update_hogar/<int:pk>/', HogarUpdate.as_view(), name="update_hogar"),
    path('delete_hogar/<int:pk>/', HogarDelete.as_view(), name="delete_hogar"),
]
