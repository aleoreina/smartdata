from django.contrib import admin
from core.models import Disclaimer
from core.models import SnippetCollection, SnippetItem
from core.models import PageProperties



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