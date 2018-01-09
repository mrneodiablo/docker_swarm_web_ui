from swarm_ui.models import LogsUser 
		
class LogsForContainers(object):

	def logsMonitor(self, username_current, container_id):
		action = "monitor"
		feature = "container"
		message = {
			"container_id": container_id,
		}
		logs = 	LogsUser(username=username_current, feature=feature, action=action, message=message)
		logs.save()

	def logsScale(self, username_current, container_id, number):
		action = "scale"
		feature = "container"
		message = {
			"container_id": container_id,
			"number": number,
		}

		logs = 	LogsUser(username=username_current, feature=feature, action=action, message=message)
		logs.save()

	def logsCreate(self, username_current, container_data):
		action = "create"
		feature = "container"
		message = {
			"container_data": container_data,
		}
		logs = 	LogsUser(username=username_current, feature=feature, action=action, message=message)
		logs.save()

	def logsRemove(self, username_current, container_id, remove_volume, remove_force):
		action = "remove"
		feature = "container"
		message = {
			"container_id": container_id,
			"remove_volume": remove_volume,
			"remove_force": remove_force,
		}
		logs = 	LogsUser(username=username_current, feature=feature, action=action, message=message)
		logs.save()

	def logsRename(self, username_current, container_id, container_data):
		action = "rename"
		feature = "container"
		message = {
			"container_id": container_id,
			"container_data": container_data,
		}
		logs = 	LogsUser(username=username_current, feature=feature, action=action, message=message)
		logs.save()

	def logsUnpause(self, username_current, container_id):
		action = "unpause"
		feature = "container"
		message = {
			"container_id": container_id,
		}
		logs = 	LogsUser(username=username_current, feature=feature, action=action, message=message)
		logs.save()

	def logsPause(self, username_current, container_id):
		action = "pause"
		feature = "container"
		message = {
			"container_id": container_id,
		}
		logs = 	LogsUser(username=username_current, feature=feature, action=action, message=message)
		logs.save()

	def logsrestart(self, username_current, container_id):
		action = "restart"
		feature = "container"
		message = {
			"container_id": container_id,
		}
		logs = 	LogsUser(username=username_current, feature=feature, action=action, message=message)
		logs.save()

	def logskill(self, username_current, container_id):
		action = "kill"
		feature = "container"
		message = {
			"container_id": container_id,
		}
		logs = 	LogsUser(username=username_current, feature=feature, action=action, message=message)
		logs.save()


	def logsstop(self, username_current, container_id):
		action = "stop"
		feature = "container"
		message = {
			"container_id": container_id,
		}
		logs = 	LogsUser(username=username_current, feature=feature, action=action, message=message)
		logs.save()	

	def logsstart(self, username_current, container_id):
		action = "start"
		feature = "container"
		message = {
			"container_id": container_id,
		}
		logs = 	LogsUser(username=username_current, feature=feature, action=action, message=message)
		logs.save()			