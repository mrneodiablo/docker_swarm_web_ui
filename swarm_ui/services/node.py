from .callapi import HttpRequestApiSwarm
from .consul import ConsulApi

class NodeApi(HttpRequestApiSwarm):
	
	def __stringParseNode(self):
		node_param_api = "info"
		node_string_id = '  ' + unichr(0x2514) + ' ' + 'ID'	
		node_string_status = '  ' + unichr(0x2514) + ' ' + 'Status'	
		node_string_containers = '  ' + unichr(0x2514) + ' ' + 'Containers'	
		node_string_cpus = '  ' + unichr(0x2514) + ' ' + 'Reserved CPUs'	
		node_string_ram = '  ' + unichr(0x2514) + ' ' + 'Reserved Memory'	

		node_string_labels = '  ' + unichr(0x2514) + ' ' + 'Labels'	
		node_string_updatedat = '  ' + unichr(0x2514) + ' ' + 'UpdatedAt'
		node_string_serverversion = '  ' + unichr(0x2514) + ' ' + 'ServerVersion'
		result = {
			'node_param_api'		   : node_param_api,
			'node_string_id'           : node_string_id,
			'node_string_status'       : node_string_status,
			'node_string_containers'   : node_string_containers,
			'node_string_cpus'         : node_string_cpus,
			'node_string_ram'          : node_string_ram,
			'node_string_labels'       : node_string_labels,
			'node_string_updatedat'    : node_string_updatedat,
			'node_string_serverversion': node_string_serverversion, }

		return result

	def searchNode(self, value):
		get_info_node = self.fetchAll()
		node_search = []
		for x in xrange(0,len(get_info_node)):
			if int(get_info_node[x]["name"].find(value)) == int(-1):
				pass
			else:
				node_search.append(get_info_node[x])
					
		return 	node_search

	def fetchNodeBase(self):
		param = self.__stringParseNode()["node_param_api"]
		docker_info = self.listAll(param)
		### get node swarm  detail
		host = []
		
		for x in xrange(4, len(docker_info["SystemStatus"])):
			key = docker_info["SystemStatus"][x][0][4] + docker_info["SystemStatus"][x][0][5]
			if key == 'ID':
				host.append(int(x)-1)
			if x == (len(docker_info["SystemStatus"]) - 1):
				host.append(x)

		get_item_node = self.__stringParseNode()
		result = []
		for i in xrange(0, len(host)-1):
			node_info = {}
			for z in xrange(host[i], host[i+1]):
				if z == (host[i]):
					node_info["name"] = docker_info["SystemStatus"][z][0].strip(" ")
					node_info["ip"] = docker_info["SystemStatus"][z][1].strip(" ")
				if docker_info["SystemStatus"][z][0] == (get_item_node["node_string_id"]):
					node_info["id"] = docker_info["SystemStatus"][z][1].strip(" ")	
			result.append(node_info)											
		return 	result	

	def fetchAll(self):
		param = self.__stringParseNode()["node_param_api"]
		docker_info = self.listAll(param)

		### get node swarm  detail
		host = []
		
		for x in xrange(4, len(docker_info["SystemStatus"])):
			key = docker_info["SystemStatus"][x][0][4] + docker_info["SystemStatus"][x][0][5]
			if key == 'ID':
				host.append(int(x)-1)
			if x == (len(docker_info["SystemStatus"]) - 1):
				host.append(x)

		get_item_node = self.__stringParseNode()
		result = []
		for i in xrange(0, len(host)-1):
			node_info = {}
			for z in xrange(host[i], host[i+1]):
				if z == (host[i]):
					node_info["name"] = docker_info["SystemStatus"][z][0].strip(" ")
					node_info["ip"] = docker_info["SystemStatus"][z][1].strip(" ")

				if docker_info["SystemStatus"][z][0] == (get_item_node["node_string_id"]):
					node_info["id"] = docker_info["SystemStatus"][z][1].strip(" ")

				if docker_info["SystemStatus"][z][0] == get_item_node["node_string_status"]:
					node_info["status"] = docker_info["SystemStatus"][z][1].strip(" ")

				if docker_info["SystemStatus"][z][0] == get_item_node["node_string_containers"]:
					node_info["containers"] = docker_info["SystemStatus"][z][1].strip(" ")

				if docker_info["SystemStatus"][z][0] == get_item_node["node_string_cpus"]:
					node_info["cpus"] = docker_info["SystemStatus"][z][1].strip(" ")

				if docker_info["SystemStatus"][z][0] == get_item_node["node_string_ram"]:
					node_info["ram"] = docker_info["SystemStatus"][z][1].strip(" ")

				if docker_info["SystemStatus"][z][0] == get_item_node["node_string_labels"]:
					node_info["label"] = docker_info["SystemStatus"][z][1].strip(" ")
					try:
						node_info["executiondriver"] = docker_info["SystemStatus"][z][1].strip(" ").split(",")[0].split("=")[1]
						node_info["kernelversion"] = docker_info["SystemStatus"][z][1].strip(" ").split(",")[1].split("=")[1]
						node_info["operatingsystem"] = docker_info["SystemStatus"][z][1].strip(" ").split(",")[2].split("=")[1]
						node_info["storagedriver"] = docker_info["SystemStatus"][z][1].strip(" ").split(",")[3].split("=")[1]
					except Exception, e:
						print e
						node_info["executiondriver"] = ""
						node_info["kernelversion"] = ""
						node_info["operatingsystem"] = ""
						node_info["storagedriver"] = ""




				if docker_info["SystemStatus"][z][0] == get_item_node["node_string_updatedat"]:
					date = docker_info["SystemStatus"][z][1].split("T")[0]
					time = docker_info["SystemStatus"][z][1].split("T")[1].split("Z")[0]
					node_info["updatedat"] =  date + " " + time

				if docker_info["SystemStatus"][z][0] == get_item_node["node_string_serverversion"]:

					node_info["serverversion"] = docker_info["SystemStatus"][z][1].strip(" ")

			result.append(node_info)

		return 	result

	def removeNode(self, ip):
		consul = ConsulApi()
		key_ip = "docker/swarm/nodes/" + ip
		list_key_node = consul.listKeys()["respone_content"]
		for list_key in list_key_node:
			if list_key["Key"] == key_ip:
				mdindex = list_key["ModifyIndex"]
				remove = consul.removeKeys(key=key_ip, mdindex=mdindex)
			else:
				remove = None	
		return remove