from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('geo/', views.geo, name='geo'),
    path('github/', views.github, name='github'),
    path('dictionary/', views.dictionary, name='dictionary'),
    path('error/', views.error, name='error')
]