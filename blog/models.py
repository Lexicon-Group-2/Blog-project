from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

# Create your models here.
import random
import string

def random_string_generator(str_size):
  allowed_chars = string.ascii_letters
  return ''.join(random.choice(allowed_chars) for x in range(str_size))

class UserProfileInfo(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE, help_text=False)
  portfolio_site = models.URLField(blank=True) # not an error if portfolio empty
  profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

  def __str__(self):
    return self.user.username


class Post(models.Model):
  user  = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=255)
  slug  = models.SlugField()
  intro = models.TextField()
  body  = models.TextField()
  date_added = models.DateTimeField(auto_now_add=True)
  
  # by default it will order by an Id, we will change it to order
  # by desending order which means newest posts are showed first.
  class Meta:
    ordering = ['-date_added']
  
  def __str__(self):
    return self.title

class Comment(models.Model):
  post  = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
  name  = models.ForeignKey(User, on_delete=models.CASCADE)
  body  = models.TextField()
  date_added = models.DateTimeField(auto_now_add=True)
  
  class Meta:
      ordering = ['-date_added']
