from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('', views.indexView, name='home'),
    path('signup/',views.signUpView, name='signup'),
    path('login/', views.loginView, name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('choice/', views.fkView, name='choice'),
]