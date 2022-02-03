from django.contrib import admin

from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('h1', 'head_title', 'meta_description', 'meta_robots', 'slug', 'status')
    autocomplete_fields = ['snippet_collection']

admin.site.register(Post, PostAdmin)
