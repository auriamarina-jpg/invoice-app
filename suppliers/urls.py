from django.urls import path
from .views import home, fornecedor_list, fornecedor_create

urlpatterns = [
    path("", home, name="home"),
    path("fornecedores/", fornecedor_list, name="fornecedor_list"),
    path("fornecedores/novo/", fornecedor_create, name="fornecedor_create"),
]

