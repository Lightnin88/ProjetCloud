from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('index/', views.index, name='index'),
    path('informations/', views.informations, name='informations'),
]
