from multiprocessing import AuthenticationError
from django.shortcuts import render, redirect
from blog.forms import UserForm, UserProfileInfoForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import Post, Comment, UserProfileInfo
from django.urls import reverse
#from numpy import true_divide

def index(request):
  return render(request, 'blog/index.html')

def register(request):

  registered = False

  if request.method == 'POST':
    user_form = UserForm(data = request.POST)
    profile_form = UserProfileInfoForm(data = request.POST)

    if user_form.is_valid() and profile_form.is_valid():
      user = user_form.save()
      user.set_password(user.password)
      user.save()
      
      profile = profile_form.save(commit=False)
      profile.user = user

      if 'profile_pic' in request.FILES:
        profile.profile_pic = request.FILES['profile_pic']
        profile.save()
        
      registered = True
    else:
      print(user_form.errors, profile_form.errors)
  else:
    user_form = UserForm()
    profile_form = UserProfileInfoForm()

  return render(request, 'blog/registration.html',
  {'user_form': user_form,
    'profile_form': profile_form,
    'registered': registered
  })

def user_login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    # use django authentication function
    user = authenticate(username=username, password=password)
    
    # check if user passed the authentication process
    if user:
      if user.is_active:
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
      else:
        return HttpResponse("Account not active")
    else:
      return HttpResponse("Invalid login details!")

  return render(request, 'blog/login.html', {})


@login_required
def user_logout(request):
  logout(request)
  return HttpResponseRedirect(reverse('index'))


def blog(request):
  posts = Post.objects.all()
  return render(request, 'blog/blog.html', {'posts': posts})

def login_page(request):
  return render(request, 'blog/login.html')



def post_detail(request, slug):
  form  = CommentForm()
  post  = Post.objects.get(slug=slug)
  name  = request.user
  body  = request.POST.get('body')
  user  = User.objects.get(id=name.id)

  if request.method == 'POST':
    comment = Comment(post=post, name=name, body=body)
    comment.save()
    return redirect('post_detail', slug=post.slug)
    
  else:
    form = CommentForm()
    
  return render(request, 'blog/post_detail.html', {'post': post, 'form': form})




@login_required
def user(request):
  profile = UserProfileInfo.objects.filter(user=request.user)
  posts = Post.objects.all().filter(user=request.user)
  
  context = {'profile': profile, 'posts': posts}
  return render(request, 'blog/user.html', context = context)

