from django.urls import path
from product import views

#rota para acessar essa view de produtos mais recentes
urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view()),
    # Nova rota para buscar detalhes do produto
    # Ex: /api/v1/products/eletronicos/iphone-15/

    path('products/search/', views.Search.as_view()),
    
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),

    # Nova rota para buscar categoria
    # Ex: /api/v1/products/eletronicos/
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
]