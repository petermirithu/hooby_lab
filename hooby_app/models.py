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
  

class reviews(models.Model):
  music_id=models.CharField(max_length=20)
  body=models.CharField(max_length=1000)
  posted_by=models.ForeignKey(User, on_delete=models.CASCADE)
  posted_on=models.DateField(auto_now_add=True)

  def __str__(self):
    return self.body

  @classmethod
  def get_reviews(cls,music_id):
    reviews=cls.objects.filter(music_id__icontains=music_id)
    return reviews
  
