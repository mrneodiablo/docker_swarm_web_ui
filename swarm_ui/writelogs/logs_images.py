from swarm_ui.models import LogsUser

class LogsForImages():

	def logsRemove(self, username_current, image_id, force_remove):
		action = "remove"
		feature = "image"
		message = {
			"image_id": image_id,
			"force_remove": force_remove,
		}
		logs = 	LogsUser(username=username_current, feature=feature, action=action, message=message)
		logs.save()

	def logsPull(self, username_current, image, registry, tag):
		action = "pull"
		feature = "image"
		message = {
			"image_name": image,
			"registry": registry,
			"tag": tag,
		}
		logs = 	LogsUser(username=username_current, feature=feature, action=action, message=message)
		logs.save()

	def logsTag(self, username_current, id_image, repo, tag):
		action = "tag"
		feature = "image"
		message = {
			"image_id": id_image,
			"repo": repo,
			"tag": tag,
		}

		logs = 	LogsUser(username=username_current, feature=feature, action=action, message=message)
		logs.save()				

