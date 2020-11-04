from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from sp_auth.auth_helper import get_sign_in_url, get_token_from_code, store_token, store_user, remove_user_and_token, get_token
from django.contrib.auth import authenticate,logout,login
import subprocess

from sp_auth.graph_helper import get_user

# Create your views here.
def home(request):
    context = initilize_context(request)
    if(request.user.is_authenticated):
      displayName=request.user.get_full_name()
      return render(request,'home.html',context)
    else:
      return render(request,'login.html',context)

################ TEMP #######################

def ps(request):
    subprocess.Popen(['C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe', 'C:\\ps\\test.ps1 "',  str(get_token(request)) ,'" name'])
    return render(request,'home.html')

#############################################


def initilize_context(request):
    context={}

    # Check errors in the session

    error = request.session.pop('flash_error',None)

    if error!=None:
        context['errors']=[]
        context['errors'].append(error)

    # Check for user in the session

    context['user'] = request.session.get('user',{'is_authenticated':False})
    return context

def sign_in(request):
  # Get the sign-in URL
  sign_in_url, state = get_sign_in_url()
  # Save the expected state so we can validate in the callback
  request.session['auth_state'] = state
  # Redirect to the Azure sign-in page
  return HttpResponseRedirect(sign_in_url)

def callback(request):
  # Get the state saved in session
  expected_state = request.session.pop('auth_state', '')
  # Make the token request
  token = get_token_from_code(request.get_full_path(), expected_state)
  # Get the user's profile
  user = get_user(token)
   # Save token and user
  store_token(request, token)
  store_user(request, user)

  return HttpResponseRedirect(reverse('home'))

def sign_out(request):
  # Clear out the user and token
  remove_user_and_token(request)
  logout(request)
  return HttpResponseRedirect(reverse('home'))