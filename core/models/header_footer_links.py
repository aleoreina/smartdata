from django.db import models
from core.models import AuditModel
from core.models import PageProperties


class FooterLink(AuditModel):
    name = models.CharField(max_length=155)

    class meta:
        verbose_name = "Footer Link"
        verbose_name_plural = "Footer Links"
    
    def get_links():
        return ColumnLinkFooter.objects.all()


class HeaderLink(AuditModel):
    name = models.CharField(max_length=155)

    class meta:
        verbose_name = "Header Link"
        verbose_name_plural = "Header Links"

    def get_links():
        return ColumnLinkHeader.objects.all()

class ColumnLinkFooter(AuditModel):
    pageproperties = models.ForeignKey(PageProperties, blank=True, null=True, on_delete=models.PROTECT)
    position = models.PositiveIntegerField()
    text = models.CharField(max_length=155)
    custom_url = models.CharField(max_length=512, blank=True, null=True)
    use_custom_url = models.BooleanField(default=False)
    footerlink = models.ForeignKey(FooterLink, on_delete=models.PROTECT)

    class meta:
        ordering = ['-position']

class ColumnLinkHeader(AuditModel):
    pageproperties = models.ForeignKey(PageProperties, blank=True, null=True, on_delete=models.PROTECT)
    position = models.PositiveIntegerField()
    text = models.CharField(max_length=155)
    custom_url = models.CharField(max_length=512, blank=True, null=True)
    use_custom_url = models.BooleanField(default=False)
    headerlink = models.ForeignKey(HeaderLink, on_delete=models.PROTECT)

    class meta:
        ordering = ['-position']
