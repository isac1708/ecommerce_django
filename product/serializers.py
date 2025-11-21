from rest_framework import serializers
from .models import Category, Product


#serializador para produtos faz o front end conversar com o back end transformando os dados em JSON
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url", # Vamos adicionar esse método no model logo abaixo
            "description",
            "price",
            "get_image", # Vamos adicionar esse método no model também
        )

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True) # Traz os produtos aninhados (opcional)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products",
        )