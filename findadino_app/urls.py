from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, nmae="dinos-home"),
    path('about/', views.about, nmae="dinos-about"),
]
