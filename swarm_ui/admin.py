# -*- coding: utf-8 -*-
from django.contrib import admin
from swarm_ui.models import DriverNetworks
from swarm_ui.models import DriverVolumes 
from swarm_ui.models import Permissions
from swarm_ui.models import UserPermissions
from swarm_ui.models import LogsLoginLogout
from swarm_ui.models import LogsUser
from swarm_ui.models import Product
from swarm_ui.models import Registry

class AdminDriverNetworks(admin.ModelAdmin):
	fields = ('driver', 'scope')
	list_display = ('__str__','scope')

class AdminDriverVolumes(admin.ModelAdmin):
	fields = ('driver', 'scope')
	list_display = ('__str__', 'scope')

class AdminPermissions(admin.ModelAdmin):
	list_display = ('__str__', 'code')
	fields = ('name',)

class AdminUserPermissions(admin.ModelAdmin):
	list_display = ('username', 'permission_code')
	list_display_links = None

class AdminLogsLoginLogout(admin.ModelAdmin):
	list_display = ('__str__', 'action', 'time')
	list_display_links = None

class AdminLogsUser(admin.ModelAdmin):
	list_display = ('__str__', 'action', 'feature', 'message', 'container', 'node', 'time')
	list_display_links = None

class AdminProduct(admin.ModelAdmin):
	list_display = ('__str__','vlan', 'scope', 'subnet', 'gateway', 'container', 'status')
	fields = ('name','vlan', 'scope', 'subnet', 'gateway', 'container', 'status')

class AdminRegistry(admin.ModelAdmin):
	list_display = ('__str__','ip', 'port')
	fields = ('name','ip', 'port')

admin.site.register(DriverNetworks, AdminDriverNetworks)
admin.site.register(DriverVolumes, AdminDriverVolumes)	
admin.site.register(Permissions, AdminPermissions)	
admin.site.register(UserPermissions, AdminUserPermissions)
admin.site.register(LogsLoginLogout, AdminLogsLoginLogout)
admin.site.register(LogsUser, AdminLogsUser)
admin.site.register(Product, AdminProduct)	
admin.site.register(Registry, AdminRegistry)	