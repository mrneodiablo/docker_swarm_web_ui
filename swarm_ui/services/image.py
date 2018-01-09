from .callapi import HttpRequestApiSwarm
import datetime

class ImagesApi(HttpRequestApiSwarm):

	def __stringPareseImages(self):

		images_param_api = "images/json?all=1"
		images_action_create = "images/create"
		images_action = "images/"


		result = {
		  "images_param_api": images_param_api,
		  "images_action_create": images_action_create,
		  "images_action": images_action,
		}
		return result
	
	def fetchAll(self):
		param = self.__stringPareseImages()["images_param_api"]
		images_info = self.listAll(param)
		result = []
		
		for x in xrange(0,len(images_info)):
			parse = {}
			parse["id"] = images_info[x]["Id"]
			parse["id_only"] = images_info[x]["Id"].split(":")[1]
			parse["link"] = images_info[x]["Id"].split(":")[1]
			parse["parent_id"] = images_info[x]["ParentId"]
			parse["repo_tags"] = []
			for repotags in xrange(0,len(images_info[x]["RepoTags"])):
				try:
					tmp_repo_tags = images_info[x]["RepoTags"][repotags]
				except Exception, e:
					print e
					tmp_repo_tags = []
				parse["repo_tags"].append(tmp_repo_tags)
			parse["repo_digests"] = images_info[x]["RepoDigests"]
			year_time =  datetime.datetime.fromtimestamp(images_info[x]["Created"]).year
			month_time =  datetime.datetime.fromtimestamp(images_info[x]["Created"]).month
			day_time =  datetime.datetime.fromtimestamp(images_info[x]["Created"]).day
			hour_time =  datetime.datetime.fromtimestamp(images_info[x]["Created"]).hour
			minute_time =  datetime.datetime.fromtimestamp(images_info[x]["Created"]).minute
			second_time =  datetime.datetime.fromtimestamp(images_info[x]["Created"]).second
			parse["created"] = "%s-%s-%s %s:%s:%s" % (year_time, month_time, day_time, hour_time, minute_time, second_time)
			parse["virtual_size"] = round(float(images_info[x]["VirtualSize"])/(1024*1024),2)
			parse["Labels"] = images_info[x]["Labels"]
			result.append(parse)
		return result

	def removeImage(self, image_id, force_remove_image="0"):
		if force_remove_image == "0":
			param = self.__stringPareseImages()["images_action"] + image_id
		else:
			param = self.__stringPareseImages()["images_action"] + image_id + "?force=1"	
		images_delete_info = self.deleteUrl(param)
		return images_delete_info

	def pullImage(self, registry_adress, name_image, tag):

		param = self.__stringPareseImages()["images_action_create"] 

		if registry_adress:
			image_pull = registry_adress + '/' + name_image
		else:	
			image_pull =  name_image

		

		data = { 
				'fromImage': image_pull,
				'tag': tag
				}
		type_header = 'type_text'
		images_pull_info = self.postUrl(param, data, type_header)
		return images_pull_info		

	def searchImage(self, name):
		get_info_image = self.fetchAll()
		image_filter = []
		for x in xrange(0, len(get_info_image)):
			for y in xrange(0,len(get_info_image[x]["repo_tags"])):
				try: 
					if int(get_info_image[x]["repo_tags"][y].find(name)) == int(-1):
						pass
					else:
						image_filter.append(get_info_image[x])
				except Exception, e:
					print e
					image_filter = []
				
		return 	image_filter	

	def inspectImage(self, id_image):
		result = {}

		param = self.__stringPareseImages()["images_action"] + id_image + "/json"
		image_inspect_info = self.listAll(param)
		if image_inspect_info and image_inspect_info != "":
			result["id"] = image_inspect_info["Id"]
			result["id_only"] = image_inspect_info["Id"].split(":")[1]
			result["container"] = image_inspect_info["Container"]
			result["comment"] = image_inspect_info["Comment"]
			result["os"] = image_inspect_info["Os"]
			result["architecture"] = image_inspect_info["Architecture"]
			date = image_inspect_info["Created"].split("T")[0]
			time = image_inspect_info["Created"].split("T")[1].split(":")[0] + ":" + image_inspect_info["Created"].split("T")[1].split(":")[1]
			result["docker_version"] = image_inspect_info["DockerVersion"]
			result["virtual_size"] = round( float(image_inspect_info["VirtualSize"])/(1024*1024), 2)
			result["size"] = image_inspect_info["Size"]
			result["author"] = image_inspect_info["Author"]
			result["repo_digests"] = image_inspect_info["RepoDigests"]
			result["repo_tags"] = image_inspect_info["RepoTags"]

			################################ images state #######################
			result["created_time"] = date + " " + time 

			result["image"] = image_inspect_info["Config"]["Image"]

			################################ images  configuration ################
			try:
				export_port = image_inspect_info["ContainerConfig"]["ExposedPorts"]
			except Exception, e:
				print e
				export_port = ""
			result["container_config"] = {		
				"hostname": image_inspect_info["ContainerConfig"]["Hostname"],
				"domainname": image_inspect_info["ContainerConfig"]["Domainname"],
				"user": image_inspect_info["ContainerConfig"]["User"],
				"attach_stdin": image_inspect_info["ContainerConfig"]["AttachStdin"],
				"attach_stdout": image_inspect_info["ContainerConfig"]["AttachStdout"],
				"attach_stderr": image_inspect_info["ContainerConfig"]["AttachStderr"],
				"exposed_ports": export_port,
				"env": image_inspect_info["ContainerConfig"]["Env"],
				"cmd": image_inspect_info["ContainerConfig"]["Cmd"],
				"volumes": image_inspect_info["ContainerConfig"]["Volumes"],
				"working_dir": image_inspect_info["ContainerConfig"]["WorkingDir"],
				"entry_point": image_inspect_info["ContainerConfig"]["Entrypoint"],
				"labels": image_inspect_info["ContainerConfig"]["Labels"],	
			}
			result["root_fs"] = image_inspect_info["RootFS"]

				
		return result	

	def historyImage(self, id_image):
		param = self.__stringPareseImages()["images_action"] + id_image + '/history'
		images_history_info = self.listAll(param)
		result = []
		for x in xrange(0,len(images_history_info)):
			parse = {}
			parse["id"] = images_history_info[x]["Id"]

			year_time =  datetime.datetime.fromtimestamp(images_history_info[x]["Created"]).year
			month_time =  datetime.datetime.fromtimestamp(images_history_info[x]["Created"]).month
			day_time =  datetime.datetime.fromtimestamp(images_history_info[x]["Created"]).day
			hour_time =  datetime.datetime.fromtimestamp(images_history_info[x]["Created"]).hour
			minute_time =  datetime.datetime.fromtimestamp(images_history_info[x]["Created"]).minute
			second_time =  datetime.datetime.fromtimestamp(images_history_info[x]["Created"]).second
			parse["created"] = "%s-%s-%s %s:%s:%s" % (year_time, month_time, day_time, hour_time, minute_time, second_time)
			
			parse["created_by"] = images_history_info[x]["CreatedBy"]
			parse["tags"] = images_history_info[x]["Tags"]
			parse["size"] = round(float(images_history_info[x]["Size"])/(1024*1024))
			parse["comment"] = images_history_info[x]["Comment"]
			result.append(parse)
		return result

	def tagImage(self, id_image, repo, force, tag):
		param = self.__stringPareseImages()["images_action"] + id_image + '/tag'
		data = {
			'repo' : repo,
			'force': force,
			'tag'  : tag,
		}
		type_header = 'type_text'
		image_tag_info =self.postUrl(param, data, type_header)
		return image_tag_info