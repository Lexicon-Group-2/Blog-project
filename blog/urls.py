from django.urls import path
from blog import views


app_name = 'blog'

url_patterns = [
  path('register/', views.register, name='register'),
  

]