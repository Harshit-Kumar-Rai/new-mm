from django.contrib import admin
from .models import Master



class MasterAdmin(admin.ModelAdmin):
  list_display = ['name', 'contact', 'city', 'state']
  search_fields = ['contact', 'city', 'state']
    
admin.site.register(Master, MasterAdmin)