from django.urls import path
from url_shortening.views import index, logout_user, profile, redirect_original, \
    RegisterUser, LoginUser

urlpatterns = [
    path('', index, name='index'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('login/profile/', profile, name='profile'),
    path('<str:url_id>', redirect_original, name='redirect_original'),
]
