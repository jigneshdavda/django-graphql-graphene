from django.urls import path
from .views import (
    ShopListApiView,
    ProductsListApiView
)

urlpatterns = [
    path('shop', ShopListApiView.as_view()),
    path('product', ProductsListApiView.as_view()),
]