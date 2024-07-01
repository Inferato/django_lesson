from django.urls import path
from .views import (
    LoginView, 
    RegistrationView, 
    logout_view, 
    CheckUserExistsView
)

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('check_user_exists/', CheckUserExistsView.as_view(), name='chec_user_exists'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
]