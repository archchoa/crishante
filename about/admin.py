from django.contrib import admin

from .models import TeamMember, Service


class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')

admin.site.register(TeamMember, TeamMemberAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Service, ServiceAdmin)
