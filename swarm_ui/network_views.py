from django.shortcuts import render, redirect
from django.http import HttpResponse
from swarm_ui.models import DriverNetworks
from django.views.decorators.csrf import csrf_exempt
import json
from . import services
from . import writelogs

class Networks():

	def __init__(self):
		self.__network_read_only = "10"
		self.__network_admin = "5"
		self.__admin = "1"

	
	def decorator_network_permission(func):
		def case_decorator(self, request, *args, **kwargs):
			try:
				session_vali = request.session["username"]
			except:
				session_vali = None

			if session_vali != None:

				if  self.__admin in request.session["permission"] or self.__network_admin in request.session["permission"] or self.__network_read_only in request.session["permission"]:
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

				if  self.__admin in request.session["permission"] or self.__network_admin in request.session["permission"]:
					return func(self, request, *args, **kwargs)
				else:
					return redirect("PermissionDeny")	
			else:
				return redirect("LoginBoard")	
		return case_decorator


	@decorator_network_permission
	def board(self, request):
	
		networkinfo = services.NetworkApi()
		nodeinfo = services.NodeApi()
		productinfo = services.ProductApi()
		result = {}

		result["return_list_node"] = nodeinfo.fetchNodeBase()
		result["return_list_product"] = productinfo.listProduct()
		result["return_list_driver_network"] = DriverNetworks.objects.all()
		if request.POST.get("ok_find") and request.POST.get("ok_find") == "ok_find":
			if request.POST.get("search_network") and request.POST.get("search_network") != "":
				param_search = request.POST.get("search_network")
				result["return_value"] = networkinfo.searchNetwork(param_search)
			else:
				result["return_value"] = networkinfo.fetchAll()
			return render(request, "swarm_ui/templates/dashboard/network_board.html", result)

		if request.POST.get("ok_filter") and request.POST.get("ok_filter") == "ok_filter":
			node_filter = request.POST.get("node")
			product_filter = request.POST.get("product")
			driver_filter = request.POST.get("driver")
			result["return_value"] = networkinfo.filterNetwork(node=node_filter, product=product_filter, driver=driver_filter)
			return render(request, "swarm_ui/templates/dashboard/network_board.html", result)

		if request.POST.get("ok_remove") and request.POST.get("ok_remove") != "":
			if  self.__admin in request.session["permission"] or self.__network_admin in request.session["permission"]:
				id_network = request.POST.get("ok_remove")
				result["return_value"] = networkinfo.removeNework(id_network)

				#@@write logs##############################
				logs = writelogs.LogsForNetworks()
				logs.logsRemove(username_current=request.session["username"], network_id=id_network)

			else:
				return redirect("PermissionDeny")	
		result["return_value"] = networkinfo.fetchAll()
		return render(request, "swarm_ui/templates/dashboard/network_board.html", result)	

	@decorator_network_permission
	def detail(self, request, network_id):	
  		networkinfo = services.NetworkApi()
  		containerinfo = services.ContainerApi()
  		list_network = networkinfo.fetchAll()

  		result = {}
		result["node_name"] = None
  		if request.method == "POST":
  			if  self.__admin in request.session["permission"] or self.__network_admin in request.session["permission"]:
	  			if request.POST.get("ok_remove"):
	  				result = networkinfo.removeNework(request.POST.get("ok_remove"))
	  				
	  				#@@write logs ##################
					logs = writelogs.LogsForNetworks()
					id_network = request.POST.get("ok_remove")
					logs.logsRemove(username_current=request.session["username"], network_id=id_network)			  				

	  				return redirect('NetworksBoard')
	  			if request.POST.get("ok_disconnect"):
	  				container_id =  request.POST.get("ok_disconnect")
	  				force = request.POST.get("force_disconnect")
	  				result = networkinfo.disconnectNetwork(network_id, container_id, force)

	  				#@@write logs ##################
					logs = writelogs.LogsForNetworks()
					logs.logsDisconnect(username_current=request.session["username"], network_id=network_id, container_id=container_id, force=force)				  				
				if request.POST.get("ok_connect"):
	  				container_id =  request.POST.get("choose_container")
	  				ip = request.POST.get("ip_connect")
	  				result = networkinfo.connectNetwork(network_id, container_id=container_id, ip=ip)

	  				#@@write logs ##################
					logs = writelogs.LogsForNetworks()
					logs.logsConnect(username_current=request.session["username"], network_id=network_id, container_id=container_id, ip=ip)				  				

			else:
				return redirect("PermissionDeny")

  		result["container_list"] = containerinfo.fetchAll() 						
		result["return_value"] = networkinfo.inspectNetwork(network_id)
  		for value_network in list_network:
  			if value_network["id"] == result["return_value"]["Id"]:
  				result["node_name"] = value_network["host"]
		try:
			result["return_product"] = networkinfo.inspectNetwork(network_id)["Labels"]["product"]
		except Exception, e:
			print e
			result["return_product"] = None
		
		return render(request, "swarm_ui/templates/dashboard/network_detail.html", result)
	
		
	@decorator_admin_permission
	def create(self, request):			
		networksinfo = services.NetworkApi()
		result = {}
		result["return_list_driver"] = DriverNetworks.objects.values("driver")
		if request.method == "POST":
			if request.POST.get("ok_create") and request.POST.get("ok_create") == "ok_create":

				name = request.POST.get("name")
				driver = request.POST.get("driver")

				if request.POST.get("check_duplicate") == "1":
					check_duplicate = True
				else:
					check_duplicate = False	

				if request.POST.get("internal") == "1":
					internal = True
				else:
					internal = False

				if request.POST.get("enableipv6") == "1":
					enableipv6 = True
				else:
					enableipv6 = False


				## get post ipam
				if request.POST.get("subnet") and request.POST.get("subnet") !="":
					ipam_subnet = request.POST.get("subnet")
				else:
					ipam_subnet = None

				if request.POST.get("gateway") and request.POST.get("gateway")!="":
					ipam_gateway = request.POST.get("gateway")
				else:
					ipam_gateway = None

				if request.POST.get("iprange") and request.POST.get("iprange")!="":
					ipam_iprange = request.POST.get("iprange")
				else:
					ipam_iprange = None
					

				# get post options
				default_bridge = request.POST.get("default_bridge")
				enable_icc = request.POST.get("enable_icc")
				enable_ip_masquerade = request.POST.get("enable_ip_masquerade")

				if request.POST.get("host_binding_ipv4") and request.POST.get("host_binding_ipv4")!="":
					host_binding_ipv4 = request.POST.get("host_binding_ipv4")
				else:
					host_binding_ipv4 = "0.0.0.0"			

				if request.POST.get("driver_mtu") and request.POST.get("driver_mtu")!="":
					driver_mtu = request.POST.get("driver_mtu")
				else:
					driver_mtu = "1500"	
				
				# get label
				labels = {}
				if request.POST.get("label_key_1") and request.POST.get("label_key_1") != "" and request.POST.get("label_value_1") and request.POST.get("label_value_1") != "":
					labels[request.POST.get("label_key_1")] = request.POST.get("label_value_1")

				if request.POST.get("label_key_2") and request.POST.get("label_key_2") != "" and request.POST.get("label_value_2") and request.POST.get("label_value_2") != "":
					labels[request.POST.get("label_key_2")] = request.POST.get("label_value_2")

				if request.POST.get("label_key_3") and request.POST.get("label_key_3") != "" and request.POST.get("label_value_3") and request.POST.get("label_value_3") != "":
					labels[request.POST.get("label_key_3")] = request.POST.get("label_value_3")					

				networksinfo.createNetwork(name=name, checkduplicate=check_duplicate, dirver=driver, internal=internal, ipam_subnet=ipam_subnet, ipam_iprange=ipam_iprange, ipam_gateway=ipam_gateway, enableipv6=enableipv6,  default_bridge=default_bridge, enable_icc=enable_icc, enable_ip_masquerade=enable_ip_masquerade, host_binding_ipv4=host_binding_ipv4, driver_mtu=driver_mtu, labels=labels)


				#@@write logs ########################################
				logs = writelogs.LogsForNetworks()
				logs.logsCreate(username_current=request.session["username"], name=name, dirver=driver, ipam_subnet=ipam_subnet, ipam_gateway=ipam_gateway, enable_icc=enable_icc, enable_ip_masquerade=enable_ip_masquerade, driver_mtu=driver_mtu)

				return redirect("NetworksBoard")
		else:
			return render(request,"swarm_ui/templates/dashboard/network_create.html", result)				
	

	@decorator_admin_permission		
	def connect(self, request):
		containerinfo = services.ContainerApi()
		networkinfo = services.NetworkApi()
		result = {}
		if request.method == "POST":
			if request.POST.get("ok_connect") != "None":

				containerid = request.POST.get("container_name")
				networkid = request.POST.get("list_network_connect")
				ip = request.POST.get("ip_connect")
				if containerid == "None":
					result["return_list_container"] = containerinfo.fetchAll()
				else:
	  				networkinfo.connectNetwork(network_id=networkid, container_id=containerid, ip=ip)

	  				#@@write logs ##################
					logs = writelogs.LogsForNetworks()
					logs.logsConnect(username_current=request.session["username"], network_id=networkid, container_id=containerid, ip=ip)	
					return redirect("/swarm/networks/" + networkid)
			else:
				return redirect("PermissionDeny")	
		else:
			result["return_list_container"] = containerinfo.fetchAll()	
		return render(request, "swarm_ui/templates/dashboard/network_connect.html", result)	

	@decorator_admin_permission
	def disconnect(self, request):
		containerinfo = services.ContainerApi()
		networkinfo = services.NetworkApi()
		result = {}
		if request.method == "POST":
			if request.POST.get("ok_disconnect") == "ok_disconnect":
				containerid = request.POST.get("container_name")
				if containerid == "None":
					result["return_list_container"] = containerinfo.fetchAll()
				else:
					networkid = request.POST.get("list_network_disconnect")
	  				networkinfo.disconnectNetwork(networkid, containerid, 1)
	  				#@@write logs ##################
					logs = writelogs.LogsForNetworks()
					logs.logsDisconnect(username_current=request.session["username"], network_id=networkid, container_id=containerid, force=1)
					return redirect("/swarm/networks/" + networkid)
			else:
				return redirect("PermissionDeny")	
		else:
			result["return_list_container"] = containerinfo.fetchAll()	
		return render(request, "swarm_ui/templates/dashboard/network_disconnect.html", result)	
				

	#get list network from containerID
	@csrf_exempt
	def apiGetNetwork(self, request):
		containerinfo = services.ContainerApi()
		networkinfo = services.NetworkApi()
		result = {}

		if request.method == "POST":
			try:
				containerid = request.POST.get("containerid")
			except:
				containerid = None 

			if  containerid != "None":
				info_container = containerinfo.inspectConainer(containerid)
				list_network = containerinfo.searchContainer(name=info_container["name"])
				list_vlan = networkinfo.filterNetwork(node=info_container["node"]["name"], product=info_container["config"]["labels"]["mto.product.name"], driver="macvlan")

				result =  {
					"status": 1,
					"containerid": containerid,
					"list_network": list_network,
					"list_vlan": list_vlan,

				}

			else:
				result = {
					"status": 0,
					"data": "containerid None",
					}									
		else:
			result = {
				"status": 0,
				"data": "method fail",
				}		


		return HttpResponse(json.dumps(result))


	@csrf_exempt
	def apiListVlan(self, request):
		networkinfo = services.NetworkApi()
		result = {}

		if request.method == "POST":
			try:
				node = request.POST.get("node")
			except:
				node = None 
			list_vlan = networkinfo.filterNetwork(node=node, product="all", driver="macvlan")

			result =  {
				"status": 1,
				"list_vlan": list_vlan,

			}
								
		else:
			result = {
				"status": 0,
				"data": "method fail",
				}		


		return HttpResponse(json.dumps(result))		