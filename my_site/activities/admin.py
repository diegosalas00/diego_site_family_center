from django.contrib import admin

from .models import Activity, PartyPackage, Available
# Register your models here.


class PackageInline(admin.StackedInline):
    model = PartyPackage


class ActivityAdmin(admin.ModelAdmin):
    inlines = [PackageInline, ]

admin.site.register(Activity, ActivityAdmin)
admin.site.register(PartyPackage)
admin.site.register(Available)
