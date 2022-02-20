
from django.urls import path
from blog.views import BlogPostDetail

from core.tools.url_surrogate import URLSurrogate

urlpatterns = [
]

try: 
    urlpatterns += URLSurrogate.generate_by_slug(
        module_name="blog",
        model_name = "post",
        view_object = BlogPostDetail
    )
except:
    print ("Makemigrations doing.")