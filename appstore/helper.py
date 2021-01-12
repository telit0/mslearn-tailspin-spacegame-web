from .api import SoftwareAPI,SoftwareInfo
from django.shortcuts import render
from subprocess import Popen, PIPE, STDOUT
import sys,json
from datetime import datetime

def install(request,id=0):
    if id==0:
        return
    else:
        #build a dict with the data based on the id
        info= SoftwareInfo.get_param(id).content.decode('utf-8')
        d=json.loads(info)[0]
        
        #Expiration

        #por cada parametro hay un installstr
        
        params=[
            'powershell.exe', 
            #'"C:\\Users\\marce\\OneDrive\\Documents\\Telito Inc\\Numiato\\SP\\SchoolPortal\\appstore\\powershell\\Installer.ps1"',
            r'C:\ps\installer.ps1',
            str(request.session['oauth_token']['access_token']),
            str(request.session['oauth_token']['expires_at']) #Validate it still valid
            ,str('"'+str(d)+'"')
            ]
        print(params)
        process=Popen(params,stdout=sys.stdout)
        #guarda los parametros en text.txt file 
        file=open("c:\\ps\\text.txt","a")
        for param in params:
            file.write(str(param)+ " \n ")
            
        file.close
        
        print(info)
        return render(request,'demo.html')