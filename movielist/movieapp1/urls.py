from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'movieapp1'
urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:movie_id>/', views.details, name='details'),
    path('add/', views.addmovie, name='addmovie'),
    path('update/<int:movie_id>/', views.update, name='update'),
    path('delete/<int:m_id>/', views.delete, name='delete'),
]
