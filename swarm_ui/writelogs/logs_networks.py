from swarm_ui.models import LogsUser 

class LogsForNetworks(object):

	def logsRemove(self, username_current, network_id):
		action = "remove"
		feature = "network"
		message = {
			"network_id": network_id,
		}
		logs = 	LogsUser(username=username_current, feature=feature, action=action, message=message)
		logs.save()
	
	def logsCreate(self, username_current, name, dirver, ipam_subnet, ipam_gateway, enable_icc, enable_ip_masquerade, driver_mtu):
		action = "create"
		feature = "network"
		message = {
			"name": name,
			"dirver": dirver,
			"ipam_subnet": ipam_subnet,
			"ipam_gateway": ipam_gateway,
			"enable_icc": enable_icc,
			"enable_ip_masquerade": enable_ip_masquerade,
			"driver_mtu": driver_mtu,
		}
		logs = 	LogsUser(username=username_current, feature=feature, action=action, message=message)
		logs.save()

	def logsDisconnect(self, username_current, network_id, container_id, force):
		action = "disconnect"
		feature = "network"
		message = {
			"network_id": network_id,
			"container_id": container_id,
			"force": force,
		}
		logs = 	LogsUser(username=username_current, feature=feature, action=action, message=message)
		logs.save()

	def logsConnect(self, username_current, network_id, container_id, ip):
		action = "connect"
		feature = "network"
		message = {
			"network_id": network_id,
			"container_id": container_id,
			"ip": ip,
		}
		logs = 	LogsUser(username=username_current, feature=feature, action=action, message=message)
		logs.save()