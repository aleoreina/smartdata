from django.contrib import admin
from core.models import Disclaimer
from core.models import SnippetCollection, SnippetItem
from core.models import PageProperties, Subscription
from core.models import FooterLink, ColumnLinkFooter, HeaderLink, ColumnLinkHeader
import nested_admin

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at', 'created_country')
    readonly_fields = ('created_ip','created_country', )

admin.site.register(Subscription, SubscriptionAdmin)


class PagePropertiesAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(PageProperties, PagePropertiesAdmin)


class SnippetItemAdmin(admin.ModelAdmin):
    pass

class SnippetCollectionAdmin(admin.ModelAdmin):
    search_fields = ['name']
    filter_horizontal = ('collection',)

admin.site.register(SnippetItem, SnippetItemAdmin)
admin.site.register(SnippetCollection,SnippetCollectionAdmin)

@admin.register(Disclaimer)
class DisclaimerAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
          return False
        else:
          return True   


class ColumnLinkHeaderAdmin(nested_admin.NestedStackedInline):
    model = ColumnLinkHeader
    autocomplete_fields = ['pageproperties']
    extra = 0

class HeaderLinkAdmin(nested_admin.NestedModelAdmin):  
    inlines = [ColumnLinkHeaderAdmin]
    list_display = ('name',)

    def has_add_permission(self, request):
        return not self.model.objects.exists()

admin.site.register(HeaderLink, HeaderLinkAdmin)


class ColumnLinkFooterAdmin(nested_admin.NestedStackedInline):
    model = ColumnLinkFooter
    autocomplete_fields = ['pageproperties']
    extra = 0

class FooterLinkAdmin(nested_admin.NestedModelAdmin):  
    inlines = [ColumnLinkFooterAdmin]
    list_display = ('name',)

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 3:
          return False
        else:
          return True

admin.site.register(FooterLink, FooterLinkAdmin)


