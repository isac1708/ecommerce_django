from rest_framework import serializers
from .models import Order, OrderItem
from product.serializers import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            "price",
            "product",
            "quantity",
        )

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "zipcode",
            "place",
            "phone",
            "stripe_token",
            "items",
        )
    
    def create(self, validated_data):
        items_data = validated_data.pop('items') # Tira os itens do pacote
        order = Order.objects.create(**validated_data) # Cria o Pedido principal

        for item_data in items_data: # Cria cada item vinculado ao Pedido
            OrderItem.objects.create(order=order, **item_data)
            
        return order