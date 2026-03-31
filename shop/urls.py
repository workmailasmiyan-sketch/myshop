from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'shop'  # Указание app_name для namespace в include

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('catalog/', views.product_list, name='catalog'),
    re_path(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
