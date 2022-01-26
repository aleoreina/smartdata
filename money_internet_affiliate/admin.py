from django.contrib import admin
from money_internet_affiliate.models import Site, InviteLink

class SiteAffiliateAdmin(admin.ModelAdmin):
    list_display = ('name', 'codename')

admin.site.register(Site, SiteAffiliateAdmin)

class InviteLinkAdmin(admin.ModelAdmin):
    list_display = ('url', 'user')

admin.site.register(InviteLink, InviteLinkAdmin)
