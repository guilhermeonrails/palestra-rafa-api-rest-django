from django import urls
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from aluraflix.views import FilmeViewSet

router = routers.DefaultRouter()
router.register('alura', FilmeViewSet)  

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
