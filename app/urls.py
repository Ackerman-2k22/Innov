from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.home, name='home'),
    path('signalization/', views.signalization, name='signalization'),
    path('depot-signal/', views.depot, name='depot-signal'),
    path('collect/', views.collect, name='collect'),
    path('marketplace_accueil/', views.marketplace, name='marketplace_accueil'),
    path('annonces/', views.annonces, name='annonces'),
    path('product_view/', views.product_view, name='product_view'),
    path('product2/', views.product2, name='product2'),


 #   path('utilisateurs/', views.utilisateurs, name='utilisateurs'),
  #  path('list-utilisateurs/', views.list_utilisateurs, name='list-utilisateurs'),
   # path('search-utilisateurs/', csrf_exempt(views.search_utilisateurs), name="search_utilisateurs"),
    #path('details/<int:id_utilisateur>/', views.details, name='details'),
]