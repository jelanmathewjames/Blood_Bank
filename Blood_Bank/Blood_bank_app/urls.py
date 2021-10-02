from django.urls import path
from . import views
urlpatterns = [
     path('',views.home,name="home"),
     path('login',views.log_in,name="login"),
     path('signin',views.sign_in,name="signin"),
     path('display',views.display,name="display"),
     path('add-donor',views.adddonor,name="add-donor"),
     path('logout',views.logout,name="logout")
]
 