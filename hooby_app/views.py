from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import profile,reviews
from .forms import UserForm,ProfileForm,ReviewForm
import requests
from django.contrib import messages
from .models import reviews
from django.http.response import HttpResponse,json

def home(request):
  '''
  view function that renders the home page
  '''
  return render(request, 'index.html')

@login_required()
def logout_request(request):
  '''
  view function that logs out a user
  '''
  logout(request)
  return redirect('home')

@login_required()
def user_profile(request):
  '''
  view function that renders the profile
  '''
  title=request.user.username  
  context={    
    'title':title,    
  }
  return render(request,'profile.html',context)

@login_required()
def other_user_profile(request, user_name):
  '''
  view function that renders the profile for other users
  '''
  title=user_name
  user_x=User.objects.get(username=user_name)  
  context={
    'title':title,
    'user_x':user_x,    
  }
  return render(request,'others_profile.html',context)

@login_required()
def update_profile(request):
  '''
  view function that dispays the update profile form  
  '''
  title='Update profile'
  if request.method=='POST':
    user_form=UserForm(request.POST, instance=request.user)
    profile_form=ProfileForm(request.POST, request.FILES, instance=request.user.profile)
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()  
      profile_form.save()          
      return redirect('profile')

  else:
    user_form=UserForm(instance=request.user)      
    profile_form=ProfileForm(instance=request.user.profile)
    context={
      'user_form':user_form,
      'profile_form':profile_form,
      'title':title
    }  
    return render(request, 'updateprofile.html',context)

@login_required()
def fetch_music(request):    
  if request.method=="POST":
    term=request.POST.get('search_term')             
    url = "https://deezerdevs-deezer.p.rapidapi.com/search"
    querystring = {"q":term}
    headers = {
        'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
        'x-rapidapi-key': "e628a84480msh32cd6fd8e2cfc83p162b72jsnc60479d7fd08"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    html=response.json()

    context={
      'musics':html['data']
    }    
    return render(request, 'music.html',context)

  else:    
    url = "https://deezerdevs-deezer.p.rapidapi.com/search"
    querystring = {"q":'hillsong'}
    headers = {
        'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
        'x-rapidapi-key': "e628a84480msh32cd6fd8e2cfc83p162b72jsnc60479d7fd08"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    html=response.json()    
    context={
      'musics':html['data']
    }    
    return render(request, 'music.html',context)

@login_required()
def single_music_item(request, music_id):    
  url = "https://deezerdevs-deezer.p.rapidapi.com/track/{}".format(music_id)    
  headers = {
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
    'x-rapidapi-key': "e628a84480msh32cd6fd8e2cfc83p162b72jsnc60479d7fd08"
    }
  response = requests.request("GET", url, headers=headers)
  # return JsonResponse(response.json(), safe=False)
  html=response.json()    
  music_reviews=reviews.get_reviews(music_id)
  context={
    'music':html,
    'form':ReviewForm(),      
    'reviews':music_reviews,
  }    
  return render(request, 'single_music.html',context)

@login_required()
def add_review(request):
  if request.method=='POST':
    form=ReviewForm(request.POST)
    music_id_x=request.POST.get('music_id')
    if form.is_valid():
      form_x=form.save(commit=False)
      form_x.posted_by=request.user
      form_x.music_id=music_id_x
      form_x.save()      
      return redirect('single_music',music_id=music_id_x )
