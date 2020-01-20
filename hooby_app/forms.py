from django import forms
from .models import profile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
  '''
  class that defines how the update user form shall look like
  '''
  class Meta:
    model=User
    fields=['username','email']

class ProfileForm(forms.ModelForm):
  '''
  class that defines how to update  profile form shall look like
  '''
  class Meta:
    model=profile
    fields=['profile_pic','status']
    

