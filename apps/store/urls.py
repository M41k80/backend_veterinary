from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CartViewSet, CartItemViewSet
from .views import StripeCheckoutSession
from .views import OrderViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'cart-items', CartItemViewSet, basename='cart-item')
router.register(r'orders', OrderViewSet, basename='orders')

urlpatterns = [
    path('store/', include(router.urls)),
    path('store/create-checkout-session/', StripeCheckoutSession.as_view(), name='stripe-checkout-session'),
]
