from venv import create
from django.db import models
from django.db import models
from core.models import User
from core.models import AuditModel

class Site(AuditModel):
    name = models.CharField(max_length=50)    
    url = models.URLField(max_length=200)
    codename = models.SlugField()

class InviteLink(AuditModel):
    site = models.ForeignKey(Site, related_name='site_invitelink', on_delete=models.CASCADE)
    url = models.URLField(max_length=200)
    user = models.ForeignKey(User, related_name='site_invitelink', on_delete=models.CASCADE)

class InviteLinkHistory(AuditModel):
    invitelink = models.ForeignKey(InviteLink, related_name='history_invitelink', on_delete=models.CASCADE)
