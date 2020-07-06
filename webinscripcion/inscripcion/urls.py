from django.urls import path
from .views import AlumnoCreate, AlumnoggCreate, ActanCreate, FichamedicaCreate, FichadvaCreate, TratamientoCreate, DiscapacidadCreate, FamiliaCreate, ResponsableCreate, ArchivoCreate, SaleInvoicePdfView


inscripcion_patterns = ([
    path('alumno/', AlumnoCreate.as_view(), name='alumno'),
    path('alumnogg/', AlumnoggCreate.as_view(), name='alumnogg'),
    path('actan/', ActanCreate.as_view(), name='actan'),
    path('fmedica/', FichamedicaCreate.as_view(), name='fmedica'),  
    path('fmdva/', FichadvaCreate.as_view(), name='fmdva'),
    path('tratamiento/', TratamientoCreate.as_view(), name='tratamiento'),
    path('discapacidad/', DiscapacidadCreate.as_view(), name='discapacidad'),
    path('familia/', FamiliaCreate.as_view(), name='familia'),
    path('tutor/', ResponsableCreate.as_view(), name='tutor'),
    path('file/', ArchivoCreate.as_view(), name='file'),
    path('pdf/<slug:pk>/', SaleInvoicePdfView.as_view(), name='pdf'),
],'inscripcion')
