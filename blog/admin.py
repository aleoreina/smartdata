from django.contrib import admin
from blog.models import Post
from tinymce.widgets import TinyMCE
from django.db import models

class PostAdmin(admin.ModelAdmin):
    list_display = ('h1', 'head_title', 'meta_description', 'meta_robots', 'slug', 'status')
    autocomplete_fields = ['snippet_collection']
    formfield_overrides = {
    models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(Post, PostAdmin)
