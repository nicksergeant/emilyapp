from django.contrib import admin
from events.models import Kid, Event


class KidAdmin(admin.ModelAdmin):
    list_display = ('name', 'user',)
    ordering = ('-created',)

admin.site.register(Kid, KidAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ('user', 'kid', 'typ', 'created',)
    list_filters = ('typ',)
    ordering = ('-created',)

admin.site.register(Event, EventAdmin)
