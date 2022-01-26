from django.db import models
from core.models import User, PageProperties


class Post(PageProperties):

    STATUS = (
        (0,"Draft"),
        (1,"Publish")
    )
    
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.h1

