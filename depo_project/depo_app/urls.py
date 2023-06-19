# urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('depo/<int:depo_id>/', views.depo_detail, name='depo_detail'),
    path('trolleybuses/', views.trolleybuses, name='trolleybuses'),

]
