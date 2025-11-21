from django.urls import path
from product import views

#rota para acessar essa view de produtos mais recentes
urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view()),
]