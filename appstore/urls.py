from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView
from .api import SoftwareAPI

from . import views

urlpatterns = [
    url(r'^sw$',SoftwareAPI.as_view()),
    url(r'^$',TemplateView.as_view(template_name="appstore.html"),name='appstore'),
    url(r'tests$',TemplateView.as_view(template_name="demo.html"))

]