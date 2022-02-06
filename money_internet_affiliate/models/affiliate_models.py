from venv import create
from django.db import models
from django.db import models
from django.forms import IntegerField
from core.models import User
from core.models import AuditModel
from core.models import PageProperties

class AffiliatePage(PageProperties):
    name = models.CharField(max_length=50, verbose_name="Affilate Web Page / App : Name")    
    url = models.URLField(max_length=200, verbose_name="URL of reference  Web Page / App")
    codename = models.SlugField()

class Steps (AuditModel):
    affiliatepage = models.ForeignKey(AffiliatePage, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    position = IntegerField()

class StepsItem (AuditModel):
    step = models.ForeignKey(Steps, on_delete=models.CASCADE)
    step_number = IntegerField()
    content_summary = models.TextField()
    content = models.TextField()

class InviteLink(AuditModel):
    site = models.ForeignKey(AffiliatePage, related_name='site_invitelink', on_delete=models.CASCADE)
    url = models.URLField(max_length=200)
    user = models.ForeignKey(User, related_name='site_invitelink', on_delete=models.CASCADE)

class InviteLinkHistory(AuditModel):
    invitelink = models.ForeignKey(InviteLink, related_name='history_invitelink', on_delete=models.CASCADE)
