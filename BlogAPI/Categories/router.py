from email.mime import base
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet

router_categories = DefaultRouter()
router_categories.register(prefix='categories', basename='categories', viewset=CategoryViewSet)