from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('mision/', views.mision , name='mision'),
    path('direccion/', views.direccion , name='direccion'),
    path('aviso/', views.aviso , name='aviso'),

]
