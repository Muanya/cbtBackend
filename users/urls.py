from django.urls import path
from rest_framework.routers import DefaultRouter

from users.views import RegistrationView, LoginView, LogoutView, AuthenticatedView

# router = DefaultRouter()
# router.register(r'', RegistrationView, basename='user_api')
#
# urlpatterns = router.urls

urlpatterns = [
    path(r'', RegistrationView.as_view(), name='user_register'),
    path('accounts/login', LoginView.as_view(), name='user_login'),
    path('accounts/logout', LogoutView.as_view(), name='user_logout'),
    path('accounts/change', AuthenticatedView.as_view(), name='trial'),
]

