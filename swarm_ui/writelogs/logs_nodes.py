from swarm_ui.models import LogsUser

class LogsForNodes():

	def logsRemove(self, username_current, node_ip):
		action = "remove"
		feature = "node"
		message = {
			"node_ip": node_ip,
		}
		logs = 	LogsUser(username=username_current, feature=feature, action=action, message=message)
		logs.save()

