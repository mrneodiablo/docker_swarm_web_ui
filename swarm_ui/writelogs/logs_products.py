from swarm_ui.models import LogsUser

class LogsForProduct():

	def logsRemove(self, username_current, product_name, vlan_name):
		action = "remove"
		feature = "product"
		message = {
			"product_name": product_name,
			"vlan_name": vlan_name
		}
		logs = 	LogsUser(username=username_current, feature=feature, action=action, message=message)
		logs.save()

	def logsAdd(self, username_current,  product_name, vlan_name, product_status, vlan_subnet, vlan_gateway, vlan_scope):
		action = "add"
		feature = "product"
		message = {
			"product_name": product_name,
			"vlan_name": vlan_name,
			"product_status": product_status,
			"vlan_subnet": vlan_subnet,
			"vlan_gateway": vlan_gateway,
			"vlan_scope": vlan_scope
		}
		logs = 	LogsUser(username=username_current, feature=feature, action=action, message=message)
		logs.save()
