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


class InviteLinkHistoryAdmin(admin.ModelAdmin):  
    list_display = ('created_at', 'invitelink__platform', 'invitelink__user')

    @staticmethod
    def invitelink__user(obj):
        return obj.invitelink.user.first_name

    @staticmethod
    def invitelink__platform(obj):
        return obj.invitelink.site.name


admin.site.register(InviteLinkHistory, InviteLinkHistoryAdmin)




