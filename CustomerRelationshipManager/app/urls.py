from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='Home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='log_out'),
    path('register/', views.register_user, name='register'),
]
