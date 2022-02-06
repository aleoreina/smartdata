from django.views.generic import DetailView
from blog.models import Post

class BlogPostDetail(DetailView):
    model = Post
    login_url = '/login/'
    template_name = 'blog/user/blog_view_post.html'
    obj_id = None

    def get_object(self, queryset=None):
        obj = super(BlogPostDetail, self).get_queryset()
        return obj.get(id=self.obj_id)    