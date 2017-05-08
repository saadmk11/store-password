from django.contrib import admin

# Register your models here.
from .models import Pass

class PassAdmin(admin.ModelAdmin):
    pass
admin.site.register(Pass, PassAdmin)