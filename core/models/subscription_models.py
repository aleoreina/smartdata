from django.db import models
from core.models import AuditModel


class Subscription (AuditModel):
    email = models.EmailField(unique=True)

    def __str__ (self):
        return self.email


