from django.urls import path
from . import views
from django.conf.urls import url, include

urlpatterns = [
    path('index/', views.index, name='index'),
    #path('login/', views.login, include('social_django.urls', namespace='social')),


]
