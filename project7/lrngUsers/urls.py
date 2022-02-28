from django.urls import path
from lrngUsers import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('',views.index,name='index'),
    path('registration',views.register,name='registration'),
    path('user_login',views.user_login,name='user_login'),
    path('logout',views.user_logout,name='logout'),
    path('special',views.special,name='special'),
]
