from django.contrib import admin
from blog.models import UserProfileInfo, Post, Comment


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display  = ('title', 'slug', 'date_added')
    #list_filter   = ("status",)
    search_fields = ['title',]
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(UserProfileInfo)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)