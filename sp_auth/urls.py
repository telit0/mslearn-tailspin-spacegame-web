from django.urls import path
from django.contrib.auth.decorators import permission_required
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('signin', views.sign_in, name='signin'),
    path('callback', views.callback, name='callback'),
    path('signout', views.sign_out, name='signout'),
    #TEMP
    path('ps',views.ps,name='ps'),
    
    path('calendar',views.home,name="calendar"), #######
]