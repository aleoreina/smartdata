from django.db import models
from django.forms import CharField
from core.models import BaseModel

class AuditModel (BaseModel):
    updated_at = models.DateTimeField(auto_now= True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_ip = models.GenericIPAddressField(default='0.0.0.0', editable=False)
    created_country = models.CharField(max_length=50, editable=False)

    class Meta: 
        abstract = True

