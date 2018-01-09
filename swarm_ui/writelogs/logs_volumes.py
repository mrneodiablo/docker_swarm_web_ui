from swarm_ui.models import LogsUser 

class LogsForVolumes(object):

	def logsRemove(self, username_current, volume_id):
		action = "remove"
		feature = "volume"
		message = {
			"volume_id": volume_id,
		}
		logs = 	LogsUser(username=username_current, feature=feature, action=action, message=message)
		logs.save()
	
	def logsCreate(self, username_current, volume_name, volume_driver, driver_opts, labels):
		action = "create"
		feature = "volume"
		message = {
			"volume_name": volume_name,
			"volume_driver": volume_driver,
			"driver_opts": driver_opts,
			"labels": labels,
		}
		logs = 	LogsUser(username=username_current, feature=feature, action=action, message=message)
		logs.save()
