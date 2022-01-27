from django.db import models
from core.models import BaseModel

class AuditModel (BaseModel):
    updated_at = models.DateTimeField(auto_now= True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta: 
        abstract = True
