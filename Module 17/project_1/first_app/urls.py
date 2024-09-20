from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home page"),
    path('signup/', views.SignUpForm, name="signup page"),
    path('login/', views.LoginForm, name="login page"),
    path('logout/', views.LogoutForm, name="logout page"),
    path('pass_change/', views.pass_change, name="passchange"),
    path('pass_change2/', views.pass_change2, name="passchange2"),
    path('profile/', views.profile, name="profile page"),
]