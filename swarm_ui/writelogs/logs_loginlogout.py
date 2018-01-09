from swarm_ui.models import LogsLoginLogout 

class LoginLogout(object):

	def logsLogin(self, username_current):
		action = "login"
		logs = LogsLoginLogout(username=username_current, action=action)
		logs.save()

	def logsLogout(self, username_current):
		action = "logout"
		logs = LogsLoginLogout(username=username_current, action=action)
		logs.save() 