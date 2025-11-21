from rest_framework.views import APIView
from rest_framework.response import Response

#busca todos os produtos mais recentes no banco e passa pelo serializer.
from .models import Product
from .serializers import ProductSerializer

class LatestProductsList(APIView):
    def get(self, request, format=None):
        # Pega os primeiros 4 produtos (fatiamento de lista [0:4])
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)