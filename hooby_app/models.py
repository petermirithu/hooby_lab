from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class profile(models.Model):
  '''
  class that defines how a users profile shall look like
  '''
  user=models.OneToOneField(User,on_delete=models.CASCADE)
  profile_pic=CloudinaryField('image',blank=True,null=True,default='')  
  status=models.CharField(max_length=100)

  def __str__(self):
      return self.user.username
  

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

class room(models.Model):
  name=models.CharField(max_length=30)
  description=models.CharField(max_length=1000)
  slug=models.CharField(max_length=50)

  def __str__(self):
    return self.name

