from django.contrib import admin
from rest_framework import routers
from .views import PostViewSet, DescriptionViewSet
from django.urls import path,include


router= routers.DefaultRouter()
router.register('post', PostViewSet)
router.register('description', DescriptionViewSet)
urlpatterns = [
    path('api/', include(router.urls)),
]
