from django.urls import path
from stock import views

app_name = 'stock'

urlpatterns = [
    path('', views.stock_entry, name='stock_entry'),
    path('details/<int:pk>', views.stock_entry_detail, name='stock_entry_detail'),
]
