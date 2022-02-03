from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import post_list


urlpatterns = [
    path('', post_list, name='homepage')   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)