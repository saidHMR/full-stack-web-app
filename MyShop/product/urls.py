from django.urls import path, include

from .views import LatestProductList, ProductDetail, CategoryDetail

urlpatterns = [
    path('latest-products/', LatestProductList.as_view()), 
    path('products/<slug:category_slug>/<slug:product_slug>/', ProductDetail.as_view()),
    path('products/<slug:category_slug>/', CategoryDetail.as_view())
]