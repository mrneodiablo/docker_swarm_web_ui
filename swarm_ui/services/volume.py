from .callapi import HttpRequestApiSwarm

class VolumesApi(HttpRequestApiSwarm):

	def __stringParseVolumes(self):

		volumes_param_api = "volumes"

		result = {
		  "volumes_param_api": volumes_param_api,
		}
		return result

	def fetchAll(self):
		param = self.__stringParseVolumes()["volumes_param_api"]
		volumes_info = self.listAll(param)
		result = []
	
		if volumes_info["Volumes"] == None:
			return result
		else:
			for x in xrange(0,len(volumes_info["Volumes"])):
				############ parse volumes##########
				parse = {}
				tmp_name = volumes_info["Volumes"][x]["Name"].split("/")
				parse["name_id"] = volumes_info["Volumes"][x]["Name"]
				parse["host"] = tmp_name[0]
				parse["name"] = tmp_name[1]
				parse["driver"] = volumes_info["Volumes"][x]["Driver"]
				parse["mount_point"] = volumes_info["Volumes"][x]["Mountpoint"]
				parse["scope"] = volumes_info["Volumes"][x]["Scope"]
				parse["labels"] = volumes_info["Volumes"][x]["Labels"]
				result.append(parse)
			return result
	def createVolumes(self, name, dirver='None', driver_opts={}, labels={}):
		param = self.__stringParseVolumes()["volumes_param_api"] + "/" + "create"

		data = {
			'Name': name,
			'Driver': dirver,
			'DriverOpts': driver_opts,
			'Labels': labels,
		}
		type_header = 'type_json'
		volume_create_info = self.postUrl(param, data, type_header)
		return volume_create_info

	def removeVolumes(self, id_volume):
		param = self.__stringParseVolumes()["volumes_param_api"] + "/" + id_volume	
		volume_delete_info = self.deleteUrl(param)
		volume_delete_info["id"] = id_volume
		return volume_delete_info

	def inspectVolume(self, name_volume):
		param = self.__stringParseVolumes()["volumes_param_api"] + '/' + name_volume
		volumes_inspect_info = self.listAll(param)	
		return volumes_inspect_info

	def searchVolume(self, value):
		get_info_volume = self.fetchAll()
		volume_search = []
		for x in xrange(0,len(get_info_volume)):
			if int(get_info_volume[x]["name_id"].find(value)) == int(-1):
				pass
			else:
				volume_search.append(get_info_volume[x])
					
		return 	volume_search	

	def filterVolume(self, node, driver):

		get_info_volume = self.fetchAll()
		volume_filter = []


		################ filter images ############
		if node == "all":
			if driver == "all":
				volume_filter = get_info_volume
			else:
				for x in xrange(0,len(get_info_volume)):
					if get_info_volume[x]["driver"].find(driver) == int(-1):
						pass
					else:
						volume_filter.append(get_info_volume[x])
		else:
			if driver == "all":
				for x in xrange(0,len(get_info_volume)):
					if int(get_info_volume[x]["host"].find(node)) == int(-1):
						pass
					else:
						volume_filter.append(get_info_volume[x])
			else:
				for x in xrange(0,len(get_info_volume)):
					if (int(get_info_volume[x]["host"].find(node)) != int(-1)) and (int(get_info_volume[x]["driver"].find(driver)) != int(-1)):
						volume_filter.append(get_info_volume[x])
					else:
						pass			
					
		return 	volume_filter	