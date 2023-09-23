# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/clientes/', views.ClienteListCreateAPI.as_view(), name='cliente-api-list-create'),
    path('clientes/', views.ClienteListView.as_view(), name='cliente-list'),
    path('clientes/add/', views.cliente_create_view, name='cliente-add'),
    path('clientes/<int:pk>/edit/', views.cliente_update_view, name='cliente-edit'),
    path('clientes/<int:pk>/delete/', views.cliente_delete_view, name='cliente-delete'),
]
