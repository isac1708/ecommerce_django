from django.db.models import Q
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

#busca todos os produtos mais recentes no banco e passa pelo serializer.
from .models import Product
from .serializers import ProductSerializer, CategorySerializer

class LatestProductsList(APIView):
    def get(self, request, format=None):
        # Pega os primeiros 4 produtos (fatiamento de lista [0:4])
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):#Recebe dois slugs (categoria e produto) para garantir URL única e busca o item exato.
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class CategoryDetail(APIView):#Busca a categoria e passa pelo serializer, ele já vai trazer a lista de produtos daquela categoria automaticamente!
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

class Search(APIView):
    def post(self, request, format=None):
        query = request.data.get('query', '') # Pega o termo enviado

        # Busca onde o nome CONTÉM o termo OU a descrição CONTÉM o termo
        # icontains = Case Insensitive (ignora maiúscula/minúscula)
        if query:
            products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)

        # Se não tiver query, retorna lista vazia
        return Response([])