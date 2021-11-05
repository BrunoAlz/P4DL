from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Toda vez que formos para a RAIZ do SITE Chamaremos o CORE.URLS
    path('', include('core.urls')), 
    path('product/', include('product.urls')), 
    path('admin/', admin.site.urls),
]
