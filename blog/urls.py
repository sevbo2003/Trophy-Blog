import imp
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import post_list, post_detail

urlpatterns = [
    path('', post_list, name='homepage'),
    path("post/<slug:slug>/", post_detail, name='post_detail')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)