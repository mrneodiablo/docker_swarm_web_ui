from django.shortcuts import render, redirect
from django.http import HttpResponse
from swarm_ui.models import Registry, Product
from django.db.models import Count
from . import services 
from . import writelogs
import json

class Containers(object):

	def __init__(self):
		self.__container_read_only = "7"
		self.__container_admin = "2"
		self.__admin = "1"

	def decorator_container_permission(func):
		def case_decorator(self, request, *args, **kwargs):
			try:
				session_vali = request.session["username"]
			except:
				session_vali = None

			if session_vali != None:

				if  self.__admin in request.session["permission"] or self.__container_read_only in request.session["permission"] or self.__container_admin in request.session["permission"]:
					return func(self, request, *args, **kwargs)
				else:
					return redirect("PermissionDeny")	
			else:
				return redirect("LoginBoard")	
		return case_decorator

	def decorator_admin_permission(func):
		def case_decorator(self, request, *args, **kwargs):
			try:
				session_vali = request.session["username"]
			except:
				session_vali = None

			if session_vali != None:

				if  self.__admin in request.session["permission"] or self.__container_admin in request.session["permission"]:
					return func(self, request, *args, **kwargs)
				else:
					return redirect("PermissionDeny")	
			else:
				return redirect("LoginBoard")	
		return case_decorator

	@decorator_container_permission
	def board(self, request):

		nodeinfo = services.NodeApi()
		coninfo = services.ContainerApi()
		productinfo = services.ProductApi()

		key_search = "None"
		result = {}
		if request.method != "POST":		
			result = {"return_value": coninfo.fetchAll(), "node_value": nodeinfo.fetchAll(),  "product_value": productinfo.listProduct()}

			return render(request, "swarm_ui/templates/dashboard/container_board.html", result)
		else:
			
			key_search = str(request.POST.get("search_container"))
			if key_search != "None":
			 	result = {"return_value": coninfo.searchContainer(key_search), "node_value": nodeinfo.fetchAll(), "product_value": productinfo.listProduct()}	
			else:
				product = str(request.POST.get("product"))
				node = str(request.POST.get("node"))
				state = str(request.POST.get("state"))

				result = {"return_value": coninfo.filterContainer(product, node, state), "node_value": nodeinfo.fetchAll(), "product_value": productinfo.listProduct()}

			return render(request, "swarm_ui/templates/dashboard/container_board.html", result)	

	@decorator_container_permission
	def detail(self, request, containerid):		
		coninfo = services.ContainerApi()
		result = {}
		if request.method == "POST":
			if  self.__admin in request.session["permission"] or self.__container_admin in request.session["permission"]:
				if request.POST.get("stop") and request.POST.get("stop") == "stop":
					coninfo.stopContainer(containerid)

					#@@write log ############################
					logs = writelogs.LogsForContainers()
					logs.logsstop(username_current=request.session["username"], container_id=containerid)	

				if request.POST.get("pause") and request.POST.get("pause") == "pause":
					coninfo.pauseContainer(containerid)
					#@@write log ############################
					logs = writelogs.LogsForContainers()
					logs.logsPause(username_current=request.session["username"], container_id=containerid)

				if request.POST.get("unpause") and request.POST.get("unpause") == "unpause":
					coninfo.unpauseContainer(containerid)
					#@@write log ############################
					logs = writelogs.LogsForContainers()
					logs.logsUnpause(username_current=request.session["username"], container_id=containerid)

				if request.POST.get("restart") and request.POST.get("restart") == "restart":
					coninfo.restartContainer(containerid)
					#@@write log ############################
					logs = writelogs.LogsForContainers()
					logs.logsrestart(username_current=request.session["username"], container_id=containerid)

				if request.POST.get("ok_rename"):
					if request.POST.get("newname"):
						new_name = request.POST.get("newname")
					else:
						new_name = ""				
					
					data = {
						"name": new_name,
					}
					coninfo.renameContainer(containerid=containerid, data=data)

					#@@write logs #############
					logs = writelogs.LogsForContainers()
					logs.logsRename(username_current=request.session["username"], container_id=containerid, container_data=data)

				if request.POST.get("ok_remove") and request.POST.get("ok_remove") == "ok_remove":
					if request.POST.get("force_remove_volume"):
						remove_volume = request.POST.get("force_remove_volume")
					else:
						remove_volume = 0

					if request.POST.get("force_remove_container"):
						remove_force = request.POST.get("force_remove_container")
					else:
						remove_force = 0				
					coninfo.removeContainer(containerid=containerid, remove_volume=remove_volume, remove_force=remove_force )
					#@@write logs ########################
					logs = writelogs.LogsForContainers()
					logs.logsRemove(username_current=request.session["username"], container_id=containerid, remove_volume=remove_volume, remove_force=remove_force)							
					return redirect("ContainerBoard")
			else:
				return redirect("PermissionDeny")	


		result["return_value"] = coninfo.inspectConainer(containerid)
		result["return_process_value"] = coninfo.processContainer(containerid)
		
		return render(request, "swarm_ui/templates/dashboard/container_detail.html", result)

	@decorator_admin_permission
	def start(self, request, containerid):
		coninfo = services.ContainerApi()
		coninfo.startContainer(containerid)

		#@@write log ############################
		logs = writelogs.LogsForContainers()
		logs.logsstart(username_current=request.session["username"], container_id=containerid)

		return redirect("ContainerBoard")

	@decorator_admin_permission
	def stop(self, request, containerid):
	
				coninfo = services.ContainerApi()
				coninfo.stopContainer(containerid)

				#@@write log ############################
				logs = writelogs.LogsForContainers()
				logs.logsstop(username_current=request.session["username"], container_id=containerid)				
				return redirect("ContainerBoard")

	@decorator_admin_permission
	def kill(self, request, containerid):
		coninfo = services.ContainerApi()
		coninfo.killContainer(containerid)

		#@@write log ############################
		logs = writelogs.LogsForContainers()
		logs.logskill(username_current=request.session["username"], container_id=containerid)

		return redirect("ContainerBoard")

	@decorator_admin_permission
	def restart(self, request, containerid):	
		coninfo = services.ContainerApi()
		coninfo.restartContainer(containerid)

		#@@write log ############################
		logs = writelogs.LogsForContainers()
		logs.logsrestart(username_current=request.session["username"], container_id=containerid)

		return redirect("ContainerBoard")

	@decorator_admin_permission
	def pause(self, request, containerid):		
				coninfo = services.ContainerApi()
				coninfo.pauseContainer(containerid)

				#@@write log ############################
				logs = writelogs.LogsForContainers()
				logs.logsPause(username_current=request.session["username"], container_id=containerid)
				return redirect("ContainerBoard")

	@decorator_admin_permission
	def unpause(self, request, containerid):			
		coninfo = services.ContainerApi()
		coninfo.unpauseContainer(containerid)

		#@@write log ############################
		logs = writelogs.LogsForContainers()
		logs.logsUnpause(username_current=request.session["username"], container_id=containerid)

		return redirect("ContainerBoard")

	@decorator_admin_permission
	def rename(self, request):

		coninfo = services.ContainerApi()
		if request.method == "POST":
			if request.POST.get("ok_rename"):
				containerid = request.POST.get("ok_rename")
				if request.POST.get("new_name"):
					new_name = request.POST.get("new_name")
				else:
					new_name = ""				
				
				data = {
					"name": new_name,
				}
				coninfo.renameContainer(containerid=containerid, data=data)

				#@@write logs #############
				logs = writelogs.LogsForContainers()
				logs.logsRename(username_current=request.session["username"], container_id=containerid, container_data=data)

				return redirect("ContainerBoard")
			else:
				return redirect("ContainerBoard")	
		else:
			return redirect("ContainerBoard")					

	@decorator_admin_permission
	def remove(self, request):
		
				coninfo = services.ContainerApi()
				if request.method == "POST":
					if request.POST.get("force_remove_volume"):
						remove_volume = request.POST.get("force_remove_volume")
					else:
						remove_volume = 0

					if request.POST.get("force_remove_container"):
						remove_force = request.POST.get("force_remove_container")
					else:
						remove_force = 0	

					if request.POST.get("ok_remove"):
						containerid = request.POST.get("ok_remove")
						coninfo.removeContainer(containerid=containerid, remove_volume=remove_volume, remove_force=remove_force )

						#@@write logs ########################
						logs = writelogs.LogsForContainers()
						logs.logsRemove(username_current=request.session["username"], container_id=containerid, remove_volume=remove_volume, remove_force=remove_force)

						return redirect("ContainerBoard")
					else:
						return redirect("ContainerBoard")

	@decorator_admin_permission
	def create(self, request):
		registry = Registry.objects.all().values("name", "ip", "port")
		registry_result = []
		for x in xrange(0, len(registry)):
			tmp = {}		
			tmp["name"] = 	registry[x]["name"]
			registry_result.append(tmp)

		coninfo = services.ContainerApi()
		nodeinfo = services.NodeApi()
		result = {}
		result["return_list_node"] = nodeinfo.fetchNodeBase()
		result["return_list_product"] = Product.objects.filter(status=1).values("name").annotate(dcount=Count('name'))
		result["return_list_registry"] = registry_result
		################# init value #############################
		Image = ""
		Hostname = ""
		Domainname = ""

		AttachStdin = False    	
		AttachStdout = False
		AttachStderr = False
		Tty = True
		OpenStdin = True
		StdinOnce = False

		###########################################
		Env = []
		Cmd = []
		Volumes = {}
		HostConfig = {}
		NetworkingConfig = {}
		Labels = {}
		ExposedPorts = {}
		IPAMConfig = {}
		#####################
		HostConfig["Binds"] = []
		HostConfig["Links"] = []
		HostConfig["Dns"] = []
		HostConfig["DnsOptions"] = []
		HostConfig["DnsSearch"] = []
		HostConfig["RestartPolicy"] =  { "Name": "", "MaximumRetryCount": 0 }
		HostConfig["NetworkMode"] =  ""
		HostConfig["Privileged"] =  False
		HostConfig["PublishAllPorts"] =  False
		HostConfig["CapAdd"] = ["NET_ADMIN"]
		HostConfig["CapDrop"] = None
		HostConfig["Sysctls"] = {

						"net.core.somaxconn":"32768",
						"net.ipv4.ip_forward":"1",
						"net.ipv4.ip_local_port_range":"1024 65534"			
		}
		HostConfig["OomScoreAdj"] = 0
		HostConfig["OomKillDisable"] = None

		if request.method == "POST" and request.POST.get("ok_create") == "ok_create":
			if request.POST.get("list_images"):
				Image = request.POST.get("list_images")

			if request.POST.get("cmd") and request.POST.get("cmd") != "":
				Cmd.append(request.POST.get("cmd"))

			if request.POST.get("hostname"):
				Hostname = request.POST.get("hostname")
			else:
				Hostname = ""

			
			if request.POST.get("hostpath") and request.POST.get("Containerpath"):
				HostConfig["Binds"].append(request.POST.get("hostpath")+ ":" + request.POST.get("Containerpath")) 


			if  request.POST.get("containerDns"):
				HostConfig["Dns"].append(request.POST.get("containerDns"))


			if request.POST.get("restart_policy") and request.POST.get("restart_policy")!="":
				HostConfig["RestartPolicy"]["Name"] = request.POST.get("restart_policy")
				if request.POST.get("MaximumRetryCount") >= 0:
					HostConfig["RestartPolicy"]["MaximumRetryCount"] = int(request.POST.get("MaximumRetryCount"))

			if request.POST.get("list_network"):
				HostConfig["NetworkMode"] = request.POST.get("list_network")
				vlan_mode = request.POST.get("list_network")


			if request.POST.get("ip_addess"):
				IPAMConfig["IPv4Address"] = request.POST.get("ip_addess")

			vlan = {
				"IPAMConfig": IPAMConfig,
			}

			NetworkingConfig["EndpointsConfig"] = {
				vlan_mode : vlan
			}


			if request.POST.get("privileged") and request.POST.get("privileged") == "True":
				HostConfig["Privileged"] =  True

			if request.POST.get("node") and request.POST.get("node") != "":
				node_search = nodeinfo.searchNode(request.POST.get("node"))
				for x in node_search:
					ip_node = x["ip"].split(":")[0]
					cpu_node = x["cpus"].split("/")[1].strip(" ")
				Labels["com.docker.swarm.constraints"] = "[" + '"ip' + "==" + ip_node +'"'+ "]"

			if request.POST.get("list_product") and request.POST.get("list_product") != "":
				Labels["mto.product.name"] = request.POST.get("list_product")

			if request.POST.get("cpus") and request.POST.get("cpus") != "":
				HostConfig["CpuShares"] = int(request.POST.get("cpus"))
				if int(cpu_node)-2 <= 1:
					HostConfig["CpusetCpus"]  = "0" 
				else:
					HostConfig["CpusetCpus"]  = "1-%s" %(int(cpu_node)-2)


			if request.POST.get("memory") and request.POST.get("memory") != "":
				HostConfig["Memory"] = int(request.POST.get("memory"))*1024*1024
				HostConfig["MemorySwap"] = int(request.POST.get("memory"))*1024*1024
				HostConfig["MemorySwappiness"] = int(-1)			
					 	

			data = {
				"Image": Image,
				"Hostname": Hostname,
				"Domainname": Domainname,
				"Labels": Labels,
				"AttachStdin": AttachStdin,
		        "AttachStdout": AttachStdout,
		        "AttachStderr": AttachStderr,
		        "Tty": Tty,
		        "OpenStdin": OpenStdin,
		        "StdinOnce": StdinOnce,
		        "ExposedPorts": ExposedPorts,
				"Env": Env,
				"Cmd": Cmd,
				"Volumes": Volumes,
				"HostConfig": HostConfig,
				"NetworkingConfig": NetworkingConfig,
			}	


			if request.POST.get("container_name") and request.POST.get("container_name") != None:
				name = 	request.POST.get("container_name")
				result = coninfo.createContainer(name=name, data=data)
				try:
					decode_id =  result["respone_content"]
					id_container = decode_id["Id"]
					coninfo.startContainer(id_container)
				except:
					print result

				#@@write logs #############
				logs = writelogs.LogsForContainers()
				logs.logsCreate(username_current=request.session["username"], container_data=data) 

				return redirect("ContainerBoard")
			else:
				result = coninfo.createContainer(data=data)
				try:
					decode_id =  result["respone_content"]
					id_container = decode_id["Id"]
					coninfo.startContainer(id_container)
				except:
					print result


				#@@write logs #############
				logs = writelogs.LogsForContainers()
				logs.logsCreate(username_current=request.session["username"], container_data=data) 

				return redirect("ContainerBoard")

		else:
			return render(request, "swarm_ui/templates/dashboard/container_create.html", result)	
	
	@decorator_admin_permission
	def scale(self, request):
		coninfo = services.ContainerApi()
		if request.POST.get("ok_scale"):
			containerid = request.POST.get("ok_scale")
			if request.POST.get("number") and  request.POST.get("number") > 0:
				number = request.POST.get("number")
				coninfo.scaleContainer(containerid=containerid, number=number)
				

				#@@write logs ###############################
				logs = writelogs.LogsForContainers()
				logs.logsScale( username_current=request.session["username"], container_id=containerid, number=number)

				return redirect("ContainerBoard")
		else:
			return redirect("ContainerBoard")

	@decorator_container_permission
	def chart(self, request, containerid):
		coninfo = services.ContainerApi()
		result = {"return_value": coninfo.inspectConainer(containerid)}
		result["value_stats"] = coninfo.statsContainer(containerid)
		return render(request, "swarm_ui/templates/dashboard/container_chart.html", result)	

	@decorator_container_permission
	def monitor(self, request, containerid):			
		coninfo = services.ContainerApi()
		result = coninfo.statsContainer(containerid=containerid)
		
		#@@ write log@@@@
		logs = writelogs.LogsForContainers()
		logs.logsMonitor(username_current=request.session["username"], container_id=containerid)

		return HttpResponse(json.dumps(result))		

