from .callapi import HttpRequestApiSwarm

class NetworkApi(HttpRequestApiSwarm):

	def __stringParseNetworks(self):

		network_param_api = "networks"

		result = {
		  "network_param_api": network_param_api,
		}
		return result
	
	def fetchAll(self):
		param = self.__stringParseNetworks()["network_param_api"]
		networks_info = self.listAll(param)
		result = []
		for x in xrange(0,len(networks_info)):
			############ parse network##########
			parse = {}
			parse["name_full"] = networks_info[x]["Name"]
			try:
				tmp_name = networks_info[x]["Name"].split("/")
				if tmp_name[1]:
					parse["host"] = tmp_name[0]
					parse["name"] = tmp_name[1]
				else:
					parse["host"]= ""
					parse["name"] = tmp_name[0]
			except Exception, e:
				print e
				parse["host"]= ""
				parse["name"] = tmp_name[0]
			parse["id"] = networks_info[x]["Id"]
			parse["scope"] = networks_info[x]["Scope"]
			parse["driver"] = networks_info[x]["Driver"]
			parse["enable_ipv6"] = networks_info[x]["EnableIPv6"]
			parse["ipam"] = networks_info[x]["IPAM"]
			parse["internal"] = networks_info[x]["Internal"]
			parse["containers"] = networks_info[x]["Containers"]
			parse["options"] = networks_info[x]["Options"]
			parse["Labels"] = networks_info[x]["Labels"]
			result.append(parse)
		return result	

	def inspectNetwork(self, id_network):
		param = self.__stringParseNetworks()["network_param_api"] + '/' + id_network
		network_inspect_info = self.listAll(param)
		return network_inspect_info

	def searchNetwork(self, name_network):
		get_info_network = self.fetchAll()
		network_search = []
		for x in xrange(0,len(get_info_network)):
			if int(get_info_network[x]["name"].find(name_network)) == int(-1):
				pass
			else:
				network_search.append(get_info_network[x])
					
		return 	network_search	

	def filterNetwork(self, node, product, driver):

		get_info_network = self.fetchAll()
		network_filter = []

        ###########################################
		if product == "all":
			if node == "all":
				if driver == "all":
					network_filter = get_info_network
				else:
					for x in xrange(0,len(get_info_network)):
						if get_info_network[x]["driver"].find(driver) == int(-1):
							pass
						else:
							network_filter.append(get_info_network[x])
			else:
				if driver == "all":
					for x in xrange(0,len(get_info_network)):
						if int(get_info_network[x]["host"].find(node)) == int(-1):
							pass
						else:
							network_filter.append(get_info_network[x])
				else:
					for x in xrange(0,len(get_info_network)):
						if (int(get_info_network[x]["host"].find(node)) != int(-1)) and (int(get_info_network[x]["driver"].find(driver)) != int(-1)):
							network_filter.append(get_info_network[x])
						else:
							pass

		else:
			if node == "all":
				if driver == "all":
					for x in xrange(0,len(get_info_network)):
						if get_info_network[x]["Labels"] == {} or int(get_info_network[x]["Labels"]["product"].find(product)) == int(-1):
							pass
						else:
							network_filter.append(get_info_network[x])
				else:
					for x in xrange(0,len(get_info_network)):
						if (get_info_network[x]["Labels"] != {}) and (int(get_info_network[x]["Labels"]["product"].find(product)) != int(-1)) and (int(get_info_network[x]["driver"].find(driver)) != int(-1)):
							network_filter.append(get_info_network[x])
						else:
							pass
			else:
				if driver == "all":
					for x in xrange(0,len(get_info_network)):
						if get_info_network[x]["Labels"] == {} or int(get_info_network[x]["Labels"]["product"].find(product)) == int(-1) or int(get_info_network[x]["host"].find(node)) == int(-1):
							pass
						else:
							network_filter.append(get_info_network[x])
				else:
					for x in xrange(0,len(get_info_network)):
						if (get_info_network[x]["Labels"] != {}) and (int(get_info_network[x]["Labels"]["product"].find(product)) != int(-1)) and (int(get_info_network[x]["driver"].find(driver)) != int(-1))  and (int(get_info_network[x]["host"].find(node)) != int(-1)):
							network_filter.append(get_info_network[x])
						else:
							pass
		return 	network_filter	

	def removeNework(self, id_network, data={}):
		param = self.__stringParseNetworks()["network_param_api"] + "/" + id_network
		network_delete_info = self.deleteUrl(param)
		network_delete_info["id"] = id_network
		return network_delete_info	

	def createNetwork(self, name, checkduplicate, dirver, internal, enableipv6, ipam_subnet=None, ipam_iprange=None, ipam_gateway=None, default_bridge=None, enable_icc=None, enable_ip_masquerade=None, host_binding_ipv4=None, driver_mtu=None, labels={}):
		param = self.__stringParseNetworks()["network_param_api"] + "/" + "create"
		get_info_network = self.fetchAll()


		flash_match = 0
		for x in xrange(0,len(get_info_network)):
			if name == get_info_network[x]["name"]:
				flash_match = 1
			else:
				pass

		if flash_match == 0:
			ipam_config = {}

			if ipam_subnet != None:
				ipam_config['Subnet'] = ipam_subnet
			if ipam_iprange != None:
				ipam_config['IPRange'] = ipam_iprange
			if ipam_gateway != None:
				ipam_config['Gateway'] = ipam_gateway
			
			

			ipam_configure_pool = []
			ipam_configure_pool.append(ipam_config)

			if ipam_configure_pool[0] == {}:
				ipam = {
						"Driver": "default" }
			else:
				ipam = {
							"Config": ipam_configure_pool,
							"Driver": "default" }

			options = {
					    "com.docker.network.bridge.enable_icc": enable_icc,
					    "com.docker.network.bridge.enable_ip_masquerade": enable_ip_masquerade,
					    "com.docker.network.bridge.host_binding_ipv4": host_binding_ipv4,
					    "com.docker.network.driver.mtu": driver_mtu,
			}		

			data = {
				'Name': name,
				'CheckDuplicate ': checkduplicate,
				'Driver': dirver,
				'Internal': internal,
				'IPAM': ipam,
				'EnableIPv6': enableipv6,
				'Options': options,
				'Labels': labels,
			} 
			type_header = 'type_json'
			network_create_info = self.postUrl(param, data, type_header)
			return network_create_info
		else:
			network_create_info = {
				'msg': 'Network with name ' + name + ' already exists',
				'code': 400,
				'data': '',
			}
			return network_create_info		

	def disconnectNetwork(self, id_network, container_id, force=False):
		param = self.__stringParseNetworks()["network_param_api"] + "/" + id_network + "/disconnect"
		data = {
			'Container': container_id,
			'Force ': force,
		}
		type_header = 'type_json'
		network_disconnect_info = self.postUrl(param, data, type_header)
		return network_disconnect_info

	def connectNetwork(self, network_id, ip, container_id):
		param = self.__stringParseNetworks()["network_param_api"] + "/" + network_id + "/connect"

		endpoint_config = {}
		ipam_config = {}

		ipam_config['IPv4Address'] = ip
		endpoint_config['IPAMConfig'] = ipam_config

		data = {
				  "Container": container_id,
				  "EndpointConfig": endpoint_config,
				}
		type_header = 'type_json'
		network_connect_info = self.postUrl(param, data, type_header)
		return network_connect_info