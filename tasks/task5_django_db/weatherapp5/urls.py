from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('refresh/', views.refresh, name='refresh'),
    path('search/', views.search, name='search'),
    path('compare/', views.compare, name='compare'),
]

