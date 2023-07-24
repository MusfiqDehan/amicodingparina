from django.urls import path
from . import views

app_name = 'khoj'

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('search/', views.search_view, name="search_view")
]
