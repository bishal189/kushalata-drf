from django.urls import path
from .views import register_user, login_user, refresh_token,update_membership

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('refresh-token/', refresh_token, name='refresh-token'),
    path('update-membership/', update_membership, name='update-membership'),
]