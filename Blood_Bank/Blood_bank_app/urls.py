from django.urls import path
from . import views
urlpatterns = [
     path('',views.home,name="home"),
     path('login',views.log_in,name="login"),
     path('signup',views.sign_up,name="signin"),
     path('display',views.display,name="display"),
     path('add-donor',views.adddonor,name="add-donor"),
     path('logout',views.logout,name="logout")
]
 