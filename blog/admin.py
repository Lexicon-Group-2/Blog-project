from django.contrib import admin
from blog.models import UserProfileInfo, Post, Comment


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display  = ('title', 'slug', 'date_added')
    search_fields = ['title',]
    prepopulated_fields = {'slug': ('title',)}

class PostComment(admin.ModelAdmin):
    list_display  = ('post', 'name', 'email', 'date_added')
    search_fields = ['name',]

admin.site.register(UserProfileInfo)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, PostComment)