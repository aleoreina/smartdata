from ast import For
from django.db import models
from django.forms import CharField
from core.models import AuditModel


class SnippetItem (AuditModel):
    name = models.CharField(max_length=50)
    content = models.TextField()

    def __str__ (self):
        return self.name

class SnippetCollection (AuditModel):
    name = models.CharField(max_length=50)
    collection = models.ManyToManyField(SnippetItem)

    def __str__ (self):
        return self.name

