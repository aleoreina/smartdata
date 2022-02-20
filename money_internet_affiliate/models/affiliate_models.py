from django.db import models
from django.forms import IntegerField, URLField
from core.models import User
from core.models import AuditModel
from core.models import PageProperties

def affiliate_page_product_path(instance, filename):
    return 'inversion/opcion/{0}'.format(filename)

class AffiliatePage(PageProperties):
    name = models.CharField(max_length=50, verbose_name="Affilate Web Page / App : Name")    
    image_1_file = models.ImageField(upload_to=affiliate_page_product_path, unique=True, blank=True)
    image_1_alt = models.CharField(max_length=100, verbose_name="Title of Image (Alt Attribute)", unique=True, blank=True)
    image_1_filename = models.CharField(max_length=100, verbose_name="Filename (image 1)", unique=True, blank=True)
    description = models.TextField()
    url = models.URLField(max_length=200, verbose_name="URL of reference  Web Page / App")
    codename = models.SlugField()
    telegram_group_link = models.URLField()

    @property
    def steps(self):
        return self.steps_set.all()

class Steps (AuditModel):
    affiliatepage = models.ForeignKey(AffiliatePage, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    position = IntegerField()

    @property
    def stepsitem (self):
        return self.stepsitem_set.all()

class StepsItem (AuditModel):
    step = models.ForeignKey(Steps, on_delete=models.CASCADE)
    step_number = IntegerField()
    name = models.CharField(max_length=50)
    content_summary = models.TextField()
    content = models.TextField()

class InviteLink(AuditModel):
    site = models.ForeignKey(AffiliatePage, related_name='site_invitelink', on_delete=models.CASCADE)
    url = models.URLField(max_length=200)
    user = models.ForeignKey(User, related_name='site_invitelink', on_delete=models.CASCADE)

class InviteLinkHistory(AuditModel):
    invitelink = models.ForeignKey(InviteLink, related_name='history_invitelink', on_delete=models.CASCADE)
