from django.contrib import admin

from adminsortable.admin import SortableAdmin

from .models import TeamMember, Service


class TeamMemberAdmin(SortableAdmin):
    list_display = ('name', 'position')

admin.site.register(TeamMember, TeamMemberAdmin)


class ServiceAdmin(SortableAdmin):
    list_display = ('name',)

admin.site.register(Service, ServiceAdmin)
