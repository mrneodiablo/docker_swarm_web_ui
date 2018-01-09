from swarm_ui.models import LogsUser

class LogsForRegistry():

	def logsRemoveImage(self, username_current, name_registry, tag_registry):
		action = "remove_image"
		feature = "registry"
		message = {
			"name_registry": name_registry,
			"tag_registry": tag_registry,
		}
		logs = 	LogsUser(username=username_current, feature=feature, action=action, message=message)
		logs.save()

	def logsRemove(self, username_current, name_registry):
		action = "remove"
		feature = "registry"
		message = {
			"name_registry": name_registry,
		}
		logs = 	LogsUser(username=username_current, feature=feature, action=action, message=message)
		logs.save()

	def logsAdd(self, username_current, name_registry, ip_registry, port_registry):
		action = "add"
		feature = "registry"
		message = {
			"name_registry": name_registry,
			"ip_registry": ip_registry,
			"port_registry": port_registry,
		}
		logs = 	LogsUser(username=username_current, feature=feature, action=action, message=message)
		logs.save()
