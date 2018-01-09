import json
from .callapi import HttpRequestApiSwarm

class ContainerApi(HttpRequestApiSwarm):

	def __stringParseContainers(self):

		containers_param_api = "containers/json?all=1"
		containers_inspect_param_api = "containers/"

		result = {
			'containers_param_api'		   : containers_param_api,
			'containers_inspect_param_api' : containers_inspect_param_api,
		}
		return result

	def fetchAll(self):
		param = self.__stringParseContainers()["containers_param_api"]
		containers_info = self.listAll(param)
		result = []
		parse = {}
		for x in xrange(0,len(containers_info)):
			parse["id"] = containers_info[x]["Id"]
			
			for name in xrange(0,len(containers_info[x]["Names"])):
				parse["full_name"] = containers_info[x]["Names"][name]
				parse["name"] = containers_info[x]["Names"][name].split("/")[2]
				parse["host"] = containers_info[x]["Names"][name].split("/")[1]
			parse["image"] = containers_info[x]["Image"]
			parse["image_id"] = containers_info[x]["ImageID"].split(":")[1]
			parse["command"] = containers_info[x]["Command"]


			### parse port
			result_port = []
			for port in xrange(0,len(containers_info[x]["Ports"])):				
				try:
					type_port = containers_info[x]["Ports"][port]["Type"].strip(" ")
				except:
					type_port = ""

				try:
					private_port = containers_info[x]["Ports"][port]["PrivatePort"]
				except:
					private_port = ""

				try:
					ip_port = containers_info[x]["Ports"][port]["IP"]
				except:
					ip_port = ""	

				try:
					public_port = containers_info[x]["Ports"][port]["PublicPort"]
				except:
					public_port = ""
				if ip_port == "":
					tmp_port = str(type_port) + "://" + str(private_port)  + str(public_port)	
				else:
					tmp_port = str(type_port) + "://" + str(private_port) + "=>" + str(ip_port) + ":" + str(public_port)	
				
				result_port.append(tmp_port)
				tmp_port = ""
			parse["ports"] = result_port

			parse["labels"] = containers_info[x]["Labels"]
			parse["state"] = containers_info[x]["State"]
			parse["status"] = containers_info[x]["Status"]
			parse["host_config"] = containers_info[x]["HostConfig"]
			parse["network_mode"] = containers_info[x]["HostConfig"]["NetworkMode"]
			parse["network_settings"] = containers_info[x]["NetworkSettings"]["Networks"]			
			parse["Mounts"] = containers_info[x]["Mounts"]

			result.append(parse)
			parse = {}
		return result

	def filterContainer(self, product, node, state):

		get_info_container = self.fetchAll()
		containers_filter = []


		################ filter product ############
		if product == "all":
			if node == "all":
				if state == "all":
					containers_filter = get_info_container
				else:
					for x in xrange(0,len(get_info_container)):
						if get_info_container[x]["state"].find(state) == int(-1):
							pass
						else:
							containers_filter.append(get_info_container[x])
			else:
				if state == "all":
					for x in xrange(0,len(get_info_container)):
						if int(get_info_container[x]["host"].find(node)) == int(-1):
							pass
						else:
							containers_filter.append(get_info_container[x])
				else:
					for x in xrange(0,len(get_info_container)):
						if (int(get_info_container[x]["host"].find(node)) != int(-1)) and (int(get_info_container[x]["state"].find(state)) != int(-1)):
							containers_filter.append(get_info_container[x])
						else:
							pass


		else:
			if node == "all":
				if state == "all":
					for x in xrange(0,len(get_info_container)):
						if int(get_info_container[x]["labels"]["mto.product.name"].find(product)) == int(-1):
							pass
						else:
							containers_filter.append(get_info_container[x])
				else:
					for x in xrange(0,len(get_info_container)):
						if (int(get_info_container[x]["labels"]["mto.product.name"].find(product)) != int(-1)) and (int(get_info_container[x]["state"].find(state)) != int(-1)):
							containers_filter.append(get_info_container[x])
						else:
							pass
			else:
				if state == "all":
					for x in xrange(0,len(get_info_container)):
						if (int(get_info_container[x]["host"].find(node)) != int(-1)) and (int(get_info_container[x]["labels"]["mto.product.name"].find(product)) != int(-1)):
							containers_filter.append(get_info_container[x])
						else:
							pass
							
				else:
					for x in xrange(0,len(get_info_container)):
						if (int(get_info_container[x]["labels"]["mto.product.name"].find(product)) != int(-1)) and (int(get_info_container[x]["state"].find(state)) != int(-1))  and (int(get_info_container[x]["host"].find(node)) != int(-1)):
							containers_filter.append(get_info_container[x])
						else:
							pass

				
					
		return 	containers_filter		

	def searchContainer(self, name):

		get_info_container = self.fetchAll()
		containers_filter = []
		for x in xrange(0, len(get_info_container)):
			try:
				if int(get_info_container[x]["name"].find(name)) == int(-1):
					pass
				else:
					containers_filter.append(get_info_container[x])
			except Exception, e:
				print e
				containers_filter = []

					
		return 	containers_filter	

	def inspectConainer(self, containerid):
		result = {}

		param = self.__stringParseContainers()["containers_inspect_param_api"] + containerid + "/json"
		containers_inspect_info = self.listAll(param)

		result["id"] = containers_inspect_info["Id"]
		date = containers_inspect_info["Created"].split("T")[0]
		time = containers_inspect_info["Created"].split("T")[1].split(":")[0] + ":" + containers_inspect_info["Created"].split("T")[1].split(":")[1]
		result["path"] = containers_inspect_info["Path"]
		result["args"] = containers_inspect_info["Args"]

		################################ container state #######################
		result["state"] = { 
							"status": containers_inspect_info["State"]["Status"],
							"created_time": date + " " + time,
							"started_at": containers_inspect_info["State"]["StartedAt"].split("T")[0] + " " + containers_inspect_info["State"]["StartedAt"].split("T")[1].split("Z")[0],
							"restart_count": containers_inspect_info["RestartCount"]
						}
		result["image"] = containers_inspect_info["Image"]
		result["name"] = containers_inspect_info["Name"].strip("/")

		################################ container  configuration ################
		result["config"] = {		
			"id": containers_inspect_info["Id"],
			"name": containers_inspect_info["Name"].strip("/"),
			"domainname": containers_inspect_info["Config"]["Domainname"],
			"user": containers_inspect_info["Config"]["User"],
			"attach_stdin": containers_inspect_info["Config"]["AttachStdin"],
			"attach_stdout": containers_inspect_info["Config"]["AttachStdout"],
			"attach_stderr": containers_inspect_info["Config"]["AttachStderr"],
			"env": containers_inspect_info["Config"]["Env"],
			"cmd": containers_inspect_info["Config"]["Cmd"],
			"image_name": containers_inspect_info["Config"]["Image"],
			"volumes": containers_inspect_info["Config"]["Volumes"],
			"working_dir": containers_inspect_info["Config"]["WorkingDir"],
			"entry_point": containers_inspect_info["Config"]["Entrypoint"],
			"restart_policy": containers_inspect_info["HostConfig"]["RestartPolicy"]["Name"],
			"labels": containers_inspect_info["Config"]["Labels"],	
		}



		############################### resource ###########################
		result["resource"] = {
			###################### resource cpu ############################
			"cpu_shares": str(containers_inspect_info["HostConfig"]["CpuShares"]),
			"cpus_set_cpus": str(containers_inspect_info["HostConfig"]["CpusetCpus"]),
			"cpu_period": str(containers_inspect_info["HostConfig"]["CpuPeriod"]),
			"cpu_quota": str(containers_inspect_info["HostConfig"]["CpuQuota"]),
			"cpu_count": str(containers_inspect_info["HostConfig"]["CpuCount"]),
			"cpu_percent": str(containers_inspect_info["HostConfig"]["CpuPercent"]),

			##################### resource ram #############################
			"memory_limit": str(containers_inspect_info["HostConfig"]["Memory"]/1024/1024),
			"memory_swap": str(containers_inspect_info["HostConfig"]["MemorySwap"]/1024/1024),
			"memory_swappiness": str(containers_inspect_info["HostConfig"]["MemorySwappiness"]/1024/1024),
			"kernel_memory": str(containers_inspect_info["HostConfig"]["KernelMemory"]/1024/1024),
			"memory_reservation": str(containers_inspect_info["HostConfig"]["MemoryReservation"]/1024/1024),


			##################### resource disk #############################
			#"blk_io_Bps": str(containers_inspect_info["HostConfig"]["BlkioBps"]),
			#"blk_io_IOps": str(containers_inspect_info["HostConfig"]["BlkioIOps"]),
			"blk_io_weight": str(containers_inspect_info["HostConfig"]["BlkioWeight"]),
			"blk_io_weight_device": str(containers_inspect_info["HostConfig"]["BlkioWeightDevice"]),
			"blk_io_device_read_IOps": str(containers_inspect_info["HostConfig"]["BlkioDeviceReadIOps"]),
			"blk_io_device_write_IOps": str(containers_inspect_info["HostConfig"]["BlkioDeviceWriteIOps"]),
			"blk_io_device_read_Bps": str(containers_inspect_info["HostConfig"]["BlkioDeviceReadBps"]),
			"blk_io_device_write_Bps": str(containers_inspect_info["HostConfig"]["BlkioDeviceWriteBps"]),
			"disk_quota": str(containers_inspect_info["HostConfig"]["DiskQuota"]),
			"devices": str(containers_inspect_info["HostConfig"]["Devices"]),
		}



		############################### container node ###########################

		############################## node label ################################
		tmp_node_labels = []
		for node_labels in containers_inspect_info["Node"]["Labels"]:
			tmp_label = node_labels + ":" +  containers_inspect_info["Node"]["Labels"][node_labels]
			tmp_node_labels.append(tmp_label)
		result["node"] = {
			
			"id": containers_inspect_info["Node"]["ID"],
			"name": containers_inspect_info["Node"]["Name"],
			"memory": round(float(containers_inspect_info["Node"]["Memory"])/(1024*1024*1024), 2),
			"cpus": str(containers_inspect_info["Node"]["Cpus"]),
			"ip": containers_inspect_info["Node"]["IP"],
			"host": containers_inspect_info["Node"]["Addr"],
			"version": containers_inspect_info["Node"]["Version"],	
			"labels": tmp_node_labels,	
		}

		############################## volumes ###################################
		result["volumes"] = {
			"volume_driver": containers_inspect_info["HostConfig"]["VolumeDriver"],
			"volumes_from": containers_inspect_info["HostConfig"]["VolumesFrom"],
			"volumes": containers_inspect_info["Config"]["Volumes"]


		}


		############################## Mounts ###################################
		result["mounts"] = containers_inspect_info["Mounts"]
		############################## environment ###############################
		result["environment"] = containers_inspect_info["Config"]["Env"]


		############################## port ######################################
		network_setting_port = []
		try:
			for x in containers_inspect_info["NetworkSettings"]["Ports"]:
				try:
					for i in xrange(0, len(containers_inspect_info["NetworkSettings"]["Ports"][x])):
						HostIp = containers_inspect_info["NetworkSettings"]["Ports"][x][i]["HostIp"]
						HostPort = containers_inspect_info["NetworkSettings"]["Ports"][x][i]["HostPort"]
						tmp_port = x + " => " + HostIp + ":" + HostPort	
				except Exception, e:
					HostIp = " "
					HostPort = " "
					tmp_port = x
				network_setting_port.append(tmp_port)
		except Exception, e:
			print e
			network_setting_port = []
		result["ports"]	= network_setting_port


		############################## network ######################################

		result["network"] = {
			"network_mode": containers_inspect_info["HostConfig"]["NetworkMode"],
			"host_name": containers_inspect_info["Config"]["Hostname"],
			"domain_name": containers_inspect_info["Config"]["Domainname"],
			"dns": containers_inspect_info["HostConfig"]["Dns"],
			"mode" : containers_inspect_info["NetworkSettings"]["Networks"],
		}

		result["networkSettings"] = {
			"sandbox_id": containers_inspect_info["NetworkSettings"]["SandboxID"],
			"sandbox_key": containers_inspect_info["NetworkSettings"]["SandboxKey"],
			"ip_address": containers_inspect_info["NetworkSettings"]["IPAddress"],
			"gate_way": containers_inspect_info["NetworkSettings"]["Gateway"],
			"mac_address": containers_inspect_info["NetworkSettings"]["MacAddress"],
			"ports" : network_setting_port,
		}				

		return result		

	def scaleContainer(self, containerid, number):
		param = self.__stringParseContainers()["containers_inspect_param_api"] + containerid + "/json"
		data = {}
		info_container = self.listAll(param)

		try:
			if info_container["Config"]["Volumes"]:
				len_volume = len(info_container["Config"]["Volumes"])
			else:
				len_volume = 0
		except Exception, e:
			len_volume = 0
			print e

		try:
			if info_container["Config"]["ExposedPorts"]:
				len_exposedports = len(info_container["Config"]["ExposedPorts"])
			else:
				len_exposedports = 0
		except Exception, e:
			len_exposedports = 0
			print e



		if  (len_volume > 0) or ( len_exposedports > 0) :
			return 0
		else:

			data = {

					"Image": info_container["Config"]["Image"],
					"AttachStdin": info_container["Config"]["AttachStdin"],
			        "AttachStdout": info_container["Config"]["AttachStdout"],
			        "AttachStderr":  info_container["Config"]["AttachStderr"],
			        "Tty": info_container["Config"]["Tty"],
			        "OpenStdin": info_container["Config"]["OpenStdin"],
			        "StdinOnce": info_container["Config"]["StdinOnce"],

					"Env": info_container["Config"]["Env"],
					"Cmd": info_container["Config"]["Cmd"],
					"HostConfig": info_container["HostConfig"],
			}	
		 	for x in xrange(0, int(number)):
		 		action_scale = self.createContainer(data)
		 		Id_container_scale = json.loads(action_scale["data"])
		 		start_container = self.startContainer(Id_container_scale["Id"])
		 	return 1		
			
	def startContainer(self, containerid, data=""):
		param = self.__stringParseContainers()["containers_inspect_param_api"] + containerid + "/start"
		type_text ="type_text"
		result = self.postUrl(param, data, type_header=type_text)
		return result

	def stopContainer(self, containerid, data=""):
		param = self.__stringParseContainers()["containers_inspect_param_api"] + containerid + "/stop"
		type_text ="type_text"
		result = self.postUrl(param, data, type_header=type_text)
		return result

	def restartContainer(self, containerid, data=""):
		param = self.__stringParseContainers()["containers_inspect_param_api"] + containerid + "/restart"
		type_text ="type_text"
		result = self.postUrl(param, data, type_header=type_text)
		return result

	def killContainer(self, containerid, data=""):
		param = self.__stringParseContainers()["containers_inspect_param_api"] + containerid + "/kill"
		type_text ="type_text"
		result = self.postUrl(param, data, type_header=type_text)
		return result

	def pauseContainer(self, containerid, data=""):
		param = self.__stringParseContainers()["containers_inspect_param_api"] + containerid + "/pause"
		type_text ="type_text"
		result = self.postUrl(param, data, type_header=type_text)
		return result

	def unpauseContainer(self, containerid, data=""):
		param = self.__stringParseContainers()["containers_inspect_param_api"] + containerid + "/unpause"
		type_text ="type_text"
		result = self.postUrl(param, data, type_header=type_text)
		return result				

	def removeContainer(self, containerid, remove_volume="0", remove_force="0"):
		param = self.__stringParseContainers()["containers_inspect_param_api"] + containerid + "?v=" + str(remove_volume) + "&" + "force=" + str(remove_force)
		result = self.deleteUrl(param)
		return result

	def renameContainer(self, containerid, data):
		param = self.__stringParseContainers()["containers_inspect_param_api"] + containerid + "/rename"
		type_text ="type_text"
		result = self.postUrl(param, data, type_header=type_text)
		return result

	def updateContainer(self, containerid, data):
		param = self.__stringParseContainers()["containers_inspect_param_api"] + containerid + "/update"
		result = self.postUrl(param, data)
		return result

	def processContainer(self, containerid):
		param = self.__stringParseContainers()["containers_inspect_param_api"] + containerid + "/top?ps_args=aux"
		try:
			result = self.listAll(param)
		except Exception, e:
			print e
			result = {}
		
		return result
		
	def createContainer(self, data, name=None):
		if name != None:
			param = self.__stringParseContainers()["containers_inspect_param_api"] + "create?name=" + name
		else:
			param = self.__stringParseContainers()["containers_inspect_param_api"] + "create"

		type_header = 'type_json'
		result = self.postUrl(param, data, type_header=type_header)
		return result		

	def statsContainer(self, containerid):

		parse = {}
		######################## per second ##########################
		parse["networks"] = {}
		parse["blockio"] = {}

		parse["blockio"]["total_read_byte_per_second"] = 0
		parse["blockio"]["total_write_byte_per_second"] = 0	
		parse["blockio"]["total_read_io_per_second"] = 0
		parse["blockio"]["total_write_io_per_second"] = 0	

		p1_total_network_rx = 0
		p1_total_network_tx = 0
		p1_total_blockio_read = 0
		p1_total_blockio_write = 0
		p1_total_blockio_iops_read = 0
		p1_total_blockio_iops_write = 0

		p2_total_network_rx = 0
		p2_total_network_tx = 0
		p2_total_blockio_read = 0
		p2_total_blockio_write = 0
		p2_total_blockio_iops_read = 0
		p2_total_blockio_iops_write = 0		

		for times in xrange(0,2):
			if times == 0:
				######################## get vaulue 1 ##############################################################
				param = self.__stringParseContainers()["containers_inspect_param_api"] + containerid + "/stats?stream=0"
				containers_info = self.listAll(param)

				for network_key in containers_info["networks"]:
			######################### network ############################
					p1_total_network_rx = p1_total_network_rx + int(containers_info["networks"][network_key]["rx_bytes"])
					p1_total_network_tx = p1_total_network_tx + int(containers_info["networks"][network_key]["tx_bytes"])

			######################### block io ###########################	
				for i in xrange(0,len(containers_info["blkio_stats"]["io_service_bytes_recursive"])):
					if containers_info["blkio_stats"]["io_service_bytes_recursive"][i]["op"] == "Read":
						p1_total_blockio_read = int(p1_total_blockio_read) + int(containers_info["blkio_stats"]["io_service_bytes_recursive"][i]["value"])

					if containers_info["blkio_stats"]["io_service_bytes_recursive"][i]["op"] == "Write":
						p1_total_blockio_write = int(p1_total_blockio_write) + int(containers_info["blkio_stats"]["io_service_bytes_recursive"][i]["value"])

				for z in xrange(0,len(containers_info["blkio_stats"]["io_serviced_recursive"])):
					if containers_info["blkio_stats"]["io_serviced_recursive"][z]["op"] == "Read":
						p1_total_blockio_iops_read = int(p1_total_blockio_iops_read) + int(containers_info["blkio_stats"]["io_serviced_recursive"][z]["value"])

					if containers_info["blkio_stats"]["io_serviced_recursive"][z]["op"] == "Write":
						p1_total_blockio_iops_write = int(p1_total_blockio_iops_write) + int(containers_info["blkio_stats"]["io_serviced_recursive"][z]["value"])	
			if times >= 1:

				######################## get vaulue 2 ##############################################################
				param = self.__stringParseContainers()["containers_inspect_param_api"] + containerid + "/stats?stream=0"
				containers_info = self.listAll(param)


				########################### time ##############################
				parse["time"] = containers_info["read"].split("T")[1].split("-")[0]

				########################### cpu ###############################
				parse["cpu"] = {}
				cpudelta = int(containers_info["cpu_stats"]["cpu_usage"]["total_usage"]) -  int(containers_info["precpu_stats"]["cpu_usage"]["total_usage"])
				systemdelta = int(containers_info["cpu_stats"]["system_cpu_usage"]) -  int(containers_info["precpu_stats"]["system_cpu_usage"])
				parse["cpu"]["cpu_usage_perct"] = round((float(cpudelta)/float(systemdelta)) * 100, 10)

				######################### ram #################################
				parse["ram"] = {}
				parse["ram"]["ram_usage"] = round(float(containers_info["memory_stats"]["usage"])/1024/1024, 2)
				parse["ram"]["ram_limit"] = round(float(containers_info["memory_stats"]["limit"])/1024/1024, 2)
				parse["ram"]["ram_usage_pect"] = round((float(containers_info["memory_stats"]["usage"])/float(containers_info["memory_stats"]["limit"]))*100, 2)

				for network_key in containers_info["networks"]:
			######################### network ############################
					p2_total_network_rx = p2_total_network_rx + int(containers_info["networks"][network_key]["rx_bytes"])
					p2_total_network_tx = p2_total_network_tx + int(containers_info["networks"][network_key]["tx_bytes"])

			######################### block io ###########################	
				for i in xrange(0,len(containers_info["blkio_stats"]["io_service_bytes_recursive"])):
					if containers_info["blkio_stats"]["io_service_bytes_recursive"][i]["op"] == "Read":
						p2_total_blockio_read = int(p2_total_blockio_read) + int(containers_info["blkio_stats"]["io_service_bytes_recursive"][i]["value"])

					if containers_info["blkio_stats"]["io_service_bytes_recursive"][i]["op"] == "Write":
						p2_total_blockio_write = int(p2_total_blockio_write) + int(containers_info["blkio_stats"]["io_service_bytes_recursive"][i]["value"])

				for z in xrange(0,len(containers_info["blkio_stats"]["io_serviced_recursive"])):
					if containers_info["blkio_stats"]["io_serviced_recursive"][z]["op"] == "Read":
						p2_total_blockio_iops_read = int(p2_total_blockio_iops_read) + int(containers_info["blkio_stats"]["io_serviced_recursive"][z]["value"])

					if containers_info["blkio_stats"]["io_serviced_recursive"][z]["op"] == "Write":
						p2_total_blockio_iops_write = int(p2_total_blockio_iops_write) + int(containers_info["blkio_stats"]["io_serviced_recursive"][z]["value"])	
		
		parse["networks"]["total_rx_per_second"] = p2_total_network_rx - p1_total_network_rx
		parse["networks"]["total_tx_per_second"] = p2_total_network_tx - p1_total_network_tx

		parse["blockio"]["total_read_byte_per_second"] = p2_total_blockio_read - p1_total_blockio_read
		parse["blockio"]["total_write_byte_per_second"] = p2_total_blockio_write - p1_total_blockio_write	
		parse["blockio"]["total_read_io_per_second"] = p2_total_blockio_iops_read - p1_total_blockio_iops_read
		parse["blockio"]["total_write_io_per_second"] = p2_total_blockio_iops_write - p1_total_blockio_iops_write	

		return 	parse						