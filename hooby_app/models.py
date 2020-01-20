from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
class profile(models.Model):
  '''
  class that defines how a users profile shall look like
  '''
  user=models.OneToOneField(User,on_delete=models.CASCADE)
  profile_pic=ImageField(blank=True,manual_crop='')
  status=models.CharField(max_length=100)

  # def __str__(self):
  #     return self.user.username`
  

