from django.db import models
from core.models import User, PageProperties

class Page(PageProperties):

    TYPE_CHOICES = (
        ('no_regular',"Customized Template for this Page"),
        ('regular',"Basic Template of Page")
    )
    
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    type = models.CharField(choices=TYPE_CHOICES, default="page", max_length=200,)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.h1

