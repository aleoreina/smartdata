from django.contrib import admin
from money_internet_affiliate.models import AffiliatePage
from money_internet_affiliate.models.affiliate_models import Steps, StepsItem, InviteLink, InviteLinkHistory
import nested_admin
from tinymce.widgets import TinyMCE
from django.db import models

class InviteLinkAdmin(nested_admin.NestedStackedInline):
    model = InviteLink
    extra = 1


class StepsItemAdmin(nested_admin.NestedStackedInline):
    model = StepsItem
    extra = 0
    formfield_overrides = {
    models.TextField: {'widget': TinyMCE()}
    }

class StepsAdmin(nested_admin.NestedStackedInline):
    model = Steps
    extra = 0
    inlines = [StepsItemAdmin]


class AffiliatePageAdmin(nested_admin.NestedModelAdmin):  
    inlines = [StepsAdmin, InviteLinkAdmin]
    list_display = ('name', 'codename')


admin.site.register(AffiliatePage, AffiliatePageAdmin)



