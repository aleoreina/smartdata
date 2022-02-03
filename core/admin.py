from django.contrib import admin
from core.models import Disclaimer

@admin.register(Disclaimer)
class DisclaimerAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
          return False
        else:
          return True   