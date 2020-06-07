from  django.urls import path

from basic_app import views

app_name= 'basic_app'

urlpatterns = [
path('',views.index,name='index'),
path('other',views.other,name='other'),
path('register',views.register,name='register'),
path('relative',views.relative,name='relative'),
path('logout',views.user_logout,name="logout"),
path('special',views.special,name='special'),
path('login',views.user_login,name="login")
]