from django.contrib import admin
from .models import Post,New,Video

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
  
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author','created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','created_on')
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(New,NewsAdmin)
admin.site.register(Video,VideoAdmin)