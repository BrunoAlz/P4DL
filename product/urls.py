from django.urls import path
from product import views

app_name = 'product'

urlpatterns = [
    path('', views.list_product, name='list_product'),
    path('<int:pk>/', views.detail_product, name='detail_product'),
    path('add/', views.ProductCreate.as_view(), name='add_product'),
    path('<int:pk>/edit', views.ProductUpdate.as_view(), name='edit_product'),
]
