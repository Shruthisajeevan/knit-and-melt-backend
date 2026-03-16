from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health_check),
    path('products/', views.ProductListView.as_view()),
    path('products/<int:pk>/', views.ProductDetailView.as_view()),
    path('categories/', views.CategoryListView.as_view()),
    path('orders/', views.OrderCreateView.as_view()),
]
