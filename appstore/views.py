from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


class AppStoreView(TemplateView):
    template_name = "appstore.html"
    

