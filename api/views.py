from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Category, Order
from django.db.models import Q
from .serializers import ProductSerializer, CategorySerializer, OrderSerializer

@api_view(['GET'])
def health_check(request):
    return Response({'status': 'ok', 'shop': 'Knit and Melt'})

class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = Product.objects.filter(is_active=True)
        category = self.request.query_params.get('category')
        if category:
            qs = qs.filter(Q(category__slug=category) | Q(category__name__iexact=category))
        return qs

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        return Response({
            'order_id': order.id,
            'message': 'Order received! We will contact you on WhatsApp.',
            'total': str(order.total_amount),
        }, status=status.HTTP_201_CREATED)
