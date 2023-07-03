from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name='IND'),
    path('contacto/',contacto,name='CONTAC'),
    path('login/',login,name='LOGIN'),
    path('cerrar/',cerrar_sesion,name='CERRAR'),
    path('registro/',registro,name='REGI'),
    path('nosotros/',sobre_nosotros,name='NOSTRO'),
    path('subirnoticia/',subir_noticia,name='SUBIRNOT'),
    path('administrarnoticias/',admin_noticias,name='ADMINNOT'),
    path('noticiapandemia/',noticia_pandemia,name='NOTPANDE'),
    path('noticiaUdechile/',noticia_Uchile,name='NOTUDECHI'),
    path('galeria/',galeria,name='GALE'),
    path('buscarpalabra/', Buscar_Palabra,name='BUSCARPALA'),
    path('buscarcategoria/',Buscar_Categoria,name='BUSCARCATE'),
    path('buscar/',Buscar,name='BUSCAR'),
    path('buscador/',Buscador,name='BUSCA'),
    path('rechazar_not/<id>/',rechazar,name="RECHANOT"),
    path('modificar_not/<id>/',modificar,name="MODINOT"),
    path('modificar/',realizar_modificacion,name="MODI"),
    path('mercancia/',mercancia,name='MERCA'),
    path('agregst_prod/<id_producto>/',agregar_producto,name='AP'),
    path('restar_prod/<id_producto>/',restar_producto,name='RP'),
    path('carrito/',carrito,name='CARRI'),
]
