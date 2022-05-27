"""django_blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from blog import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name='register'),
    path('user/', views.user, name='user'),
    path('admin/', admin.site.urls),
    path('logout/', views.user_logout, name="logout"),
    path('login/', views.user_login, name="user_login"),
    path('login/', views.login_page, name="login_page"),
    path('blog/', views.blog, name="blog"),
    path('<slug:slug>/', views.post_detail, name="post_detail"),
    path('<post_id>',views.delete_post,name='delete_post'),
    path('/<int:id>',views.delete_comment,name='delete_comment'),
    path('<int:id>',views.update_post,name='update_post'),
    path('write_post/',views.write_post,name='write_post'),
]

# this part is for user profile pictures
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)