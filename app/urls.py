from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('utilisateurs/', views.utilisateurs, name='utilisateurs'),
    path('list-utilisateurs/', views.list_utilisateurs, name='list-utilisateurs'),
    path('search-utilisateurs/', csrf_exempt(views.search_utilisateurs), name="search_utilisateurs"),
    path('details/<int:id_utilisateur>/', views.details, name='details'),
]