from .api import SoftwareAPI
from django.shortcuts import render

def install(request,id=0):
    if id==0:
        return
    else:
        return render(request,'appstore.html')