from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from money_internet_affiliate.models import AffiliatePage
from money_internet_affiliate.models.affiliate_models import Steps, StepsItem, InviteLink, InviteLinkHistory
import nested_admin



class InviteLinkAdmin(nested_admin.NestedStackedInline):
    model = InviteLink
    extra = 1


class StepsItemAdmin(nested_admin.NestedStackedInline):
    model = StepsItem
    extra = 1

class StepsAdmin(nested_admin.NestedStackedInline):
    model = Steps
    extra = 1
    inlines = [StepsItemAdmin]


class AffiliatePageAdmin(nested_admin.NestedModelAdmin, SummernoteModelAdmin):
    
    inlines = [StepsAdmin, InviteLinkAdmin]
    list_display = ('name', 'codename')
    summernote_fields = '__all__'

admin.site.register(AffiliatePage, AffiliatePageAdmin)



