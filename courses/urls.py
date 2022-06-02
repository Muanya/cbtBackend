from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import index

# router = DefaultRouter()
# router.register(r'', Viewset, basename='user_api')
#
# urlpatterns = router.urls

urlpatterns = [
    path('', index),
]
