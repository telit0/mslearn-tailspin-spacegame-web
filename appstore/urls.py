from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .api import SoftwareAPI,SoftwareInfo

from appstore.views import AppStoreView

from . import helper

urlpatterns = [
    #SoftwareAPI
    url(r'^sw$',SoftwareAPI.as_view()),
    path('sw/<int:id>',SoftwareInfo.as_view()),

    #AppStore
    url(r'^$',login_required(AppStoreView.as_view()),name='appstore'),
    url(r'tests$',login_required(TemplateView.as_view(template_name="demo.html"))),
    path('install/<int:id>',login_required(helper.install))

]