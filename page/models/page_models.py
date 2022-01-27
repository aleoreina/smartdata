from django.db import models
from core.models import User, PageProperties

class Page(PageProperties):   
    content = models.TextField()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.h1

