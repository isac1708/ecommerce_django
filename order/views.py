from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        stripe_token = request.data.get('stripe_token')
        paid_amount = sum(item.get('quantity') * item.get('product').price for item in serializer.validated_data['items'])
        
        try:
            # Futuramente aqui entra a cobrança no cartão
            # charge = stripe.Charge.create(...)
            
            serializer.save(user=request.user, paid_amount=paid_amount)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)