from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'mamazon'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('products/', views.ProductListView.as_view(), name='product-list')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
