from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    # na Raiz do site chamaremos o Template INDEX
    path('', views.index, name='index'),
]
