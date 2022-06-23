from django.urls import path
from .views import una_vista, un_template
from .models import Prueba

urlpatterns = [
    path('', una_vista),  
    path('mi-template', un_template),
]