from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView
from .api import SoftwareAPI,SoftwareInfo

from . import helper

urlpatterns = [
    #SoftwareAPI
    url(r'^sw$',SoftwareAPI.as_view()),
    path('sw/<int:id>',SoftwareInfo.as_view()),

    #AppStore
    url(r'^$',TemplateView.as_view(template_name="appstore.html"),name='appstore'),
    url(r'tests$',TemplateView.as_view(template_name="demo.html")),
    path('install/<int:id>',helper.install)

]