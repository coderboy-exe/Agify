from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('human-age/', views.get_age, name='get_age'),
]