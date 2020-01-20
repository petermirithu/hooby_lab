from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import profile
from .forms import UserForm,ProfileForm

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

