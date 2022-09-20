from django.contrib import admin
from home import views
from django.urls import path,include

urlpatterns = [
    path("",views.index,name="home"),
    path("login",views.login_user,name="login"),
    path("logout",views.logout_user,name="logout")

]