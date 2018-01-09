from swarm_ui.models import LogsUser

class LogsForusers(object):
	
	def logsRemove(self, username_remove, username_current):
		action = "remove"
		feature = "user"
		message = {
			"user": username_remove
		}
		logs = 	LogsUser(username=username_current, feature=feature, action=action, message=message)
		logs.save()

	def logsUpdate(self, username_current, username, firstname, lastname, permission_user_logs=[]):
		action = "update"
		feature = "user"
		message = {
			"user": username,
			"firstname": firstname,
			"lastname": lastname,
			"permission": permission_user_logs,
		}
		logs = 	LogsUser(username=username_current, feature=feature, action=action, message=message)
		logs.save()

	def logsCreate(self, username_current,  username, firstname, lastname, permission_user_logs=[]):
		action = "create"
		feature = "user"
		message = {
			"user": username,
			"firstname": firstname,
			"lastname": lastname,
			"permission": permission_user_logs,

		}
		logs = 	LogsUser(username=username_current, feature=feature, action=action, message=message)
		logs.save()

						 