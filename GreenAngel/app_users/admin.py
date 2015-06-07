__author__ = 'Tarun Behal'

from django.contrib import admin
from .models import Campaign, CampaignZone, Plantation
# Register your models here.


class CampaignZoneInLine(admin.TabularInline):
    model = CampaignZone
    extra = 1


class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_at', 'end_at', 'user',
                    'created_at', 'updated_at')
    fieldsets = [
        (None, {'fields': ['name', 'description', 'user', 'photo']}),
        ("Start & End", {'fields': ['start_at', 'end_at']}),
    ]
    inlines = [CampaignZoneInLine]


admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Plantation)
