from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save_location/', views.save_location, name='save_location'),
    path('get_shortest_route/', views.get_shortest_route, name='get_shortest_route'),
]