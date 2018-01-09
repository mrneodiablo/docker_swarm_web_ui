from django.conf import settings
from .callapi import HttpRequestApiSwarm

class InfoApi(HttpRequestApiSwarm):
	
	def fetchAll(self):
		
		param = "info"
		docker_info = self.listAll(param)
		containers_total = docker_info["Containers"]
		images_total = docker_info["Images"]
		swarm_status_total = docker_info["SystemStatus"]
		### get node swarm 
		for x in xrange(0,len(swarm_status_total)):
			if swarm_status_total[x][0] == "Nodes":
				nodes_total = swarm_status_total[x][1]
				break
			else:
				nodes_total = 0

		for x in xrange(0,len(swarm_status_total)):
			if swarm_status_total[x][0] == "Role":
				swarm_role = swarm_status_total[x][1]
				break
			else:
				swarm_role = 0
		for x in xrange(0,len(swarm_status_total)):
			if swarm_status_total[x][0] == "Strategy":
				swarm_strategy = swarm_status_total[x][1]
				break
			else:
				swarm_strategy = 0	

		for x in xrange(0,len(swarm_status_total)):
			if swarm_status_total[x][0] == "Filters":
				swarm_filters = swarm_status_total[x][1]
				break
			else:
				swarm_filters = 0

		##### get cpu ########
						
		cpu_total = docker_info["NCPU"]
		cpus_node = 0
		string_cpus = '  ' + unichr(0x2514) + ' ' + 'Reserved CPUs'
		for x in xrange(0,len(swarm_status_total)):
			if docker_info["SystemStatus"][x][0] == string_cpus:
				get_cpu_usage = docker_info["SystemStatus"][x][1].split(" ")
				cpus_node = cpus_node + int(get_cpu_usage[0])
		try:
			cpu_available = (cpus_node/cpu_total)*100
		except Exception, e:
			print  e
			cpu_available = 0


		#### get memory #########
		ram_total = int(docker_info["MemTotal"])/(1024*1024*1024)
		ram_node = 0
		string_ram = '  ' + unichr(0x2514) + ' ' + 'Reserved Memory'
		for x in xrange(0,len(swarm_status_total)):
			if docker_info["SystemStatus"][x][0] == string_ram:
				get_ram_usage = docker_info["SystemStatus"][x][1].split(" ")
				ram_node = ram_node + float(get_ram_usage[0])
		try:
			ram_available = round((float(ram_node)/float(ram_total))*100, 2)
		except Exception, e:
			print   e
			ram_available = 0
		

		result = {
			'containers_total': containers_total,
			'images_total'    : images_total,
			'nodes_total'     : nodes_total,
			'swarm_role'	  : swarm_role,
			'swarm_strategy'  : swarm_strategy,
			'swarm_filters'   : swarm_filters,
			'swarm_version'	  : docker_info["ServerVersion"],
			'swarm_security'  : docker_info["SecurityOptions"],
			'swarm_manager'  :  settings.API_DOCKER_SWARM["PROTOCOL"] +'://' +  settings.API_DOCKER_SWARM["HOST"] + ':'+ settings.API_DOCKER_SWARM["PORT"],
			'consul_manager'  : settings.API_CONSUL_MANAGER["HOST"] + ':'+ settings.API_CONSUL_MANAGER["PORT"],
			"cpu_total"       : cpu_total,
			"cpus_node"       : cpus_node,
			"cpu_available"   : cpu_available,
			"ram_available"	  : ram_available,
			"ram_node"	      : ram_node,
			"ram_total"	      : ram_total,


		}
		return result