from django.shortcuts import render, redirect
from swarm_ui.models import DriverVolumes
from . import services
from . import writelogs

class Volumes(object):

	__volume_read_only = "9"
	__volume_admin = "4"
	__admin = "1"

	def checksession(func):
		def wrapper(self, request):
			try:
				session_vali = request.session["username"]
			except:
				session_vali = None

			if session_vali != None:

				if  self.__admin in request.session["permission"] or self.__registry_admin in request.session["permission"] or self.__registry_read_only in request.session["permission"]:
					return func(self, request)
				else:
					return redirect("PermissionDeny")	
			else:
				return redirect("LoginBoard")	
		return wrapper

	@checksession
	def board(self, request):	
		volumesinfo = services.VolumesApi()
		nodesinfo = services.NodeApi()
		result = {}
		result["return_list_driver"] = DriverVolumes.objects.all()
		result["return_list_node"] = nodesinfo.fetchNodeBase()

		if request.POST.get("ok_find") and request.POST.get("ok_find") == "ok_find":
			if request.POST.get("search_volume"):
				param_search = request.POST.get("search_volume")
				result["return_value"] = volumesinfo.searchVolume(param_search)
			else:
				result["return_value"] = volumesinfo.fetchAll()
			return render(request, "swarm_ui/templates/dashboard/volumes_board.html", result)

		if request.POST.get("ok_filter") and request.POST.get("ok_filter") == "ok_filter":
			if request.POST.get("filter_driver") and request.POST.get("filter_node"):
				param_driver = request.POST.get("filter_driver")
				param_node = request.POST.get("filter_node")
				result["return_value"] = volumesinfo.filterVolume(param_node, param_driver)
			else:
				result["return_value"] = volumesinfo.fetchAll()

			return render(request, "swarm_ui/templates/dashboard/volumes_board.html", result)
		if request.POST.get("ok_remove_volume") and request.POST.get("ok_remove_volume") !="" :
			if  self.__admin in request.session["permission"] or self.__volume_admin in request.session["permission"]:
				id_volume = request.POST.get("ok_remove_volume")
				response = volumesinfo.removeVolumes(id_volume)
				result["response_remove"] = response

				#@@write logs #################################
				logs = writelogs.LogsForVolumes()
				logs.logsRemove(username_current=request.session["username"], volume_id=id_volume)

			else:
				return redirect("PermissionDeny")	
		result["return_value"] = volumesinfo.fetchAll()
		return render(request, "swarm_ui/templates/dashboard/volumes_board.html", result)

	@checksession
	def create(self, request):		
		volumesinfo = services.VolumesApi()
		result = {}
		result["return_list_driver"] = DriverVolumes.objects.all()
		if request.method == "POST":
			if request.POST.get("ok_create") and request.POST.get("ok_create") == "ok_create":
				volume_name = request.POST.get("volume_name")
				volume_driver = request.POST.get("volume_driver")
				opt_driver = {}
				if request.POST.get("opt_key_1") and request.POST.get("opt_key_1") != "" and request.POST.get("opt_value_1") and request.POST.get("opt_value_1") != "":
					opt_driver[request.POST.get("opt_key_1")] = request.POST.get("opt_value_1")

				if request.POST.get("opt_key_2") and request.POST.get("opt_key_2") != "" and request.POST.get("opt_value_2") and request.POST.get("opt_value_2") != "":
					opt_driver[request.POST.get("opt_key_2")] = request.POST.get("opt_value_2")

				if request.POST.get("opt_key_3") and request.POST.get("opt_key_3") != "" and request.POST.get("opt_value_3") and request.POST.get("opt_value_3") != "":
					opt_driver[request.POST.get("opt_key_3")] = request.POST.get("opt_value_3")	


				labels = {}
				if request.POST.get("label_key_1") and request.POST.get("label_key_1") != "" and request.POST.get("label_value_1") and request.POST.get("label_value_1") != "":
					labels[request.POST.get("label_key_1")] = request.POST.get("label_value_1")

				if request.POST.get("label_key_2") and request.POST.get("label_key_2") != "" and request.POST.get("label_value_2") and request.POST.get("label_value_2") != "":
					labels[request.POST.get("label_key_2")] = request.POST.get("label_value_2")

				if request.POST.get("label_key_3") and request.POST.get("label_key_3") != "" and request.POST.get("label_value_3") and request.POST.get("label_value_3") != "":
					labels[request.POST.get("label_key_3")] = request.POST.get("label_value_3")	


				volumesinfo.createVolumes(volume_name, volume_driver, driver_opts=opt_driver, labels=labels)

				#@@write logs #################################
				logs = writelogs.LogsForVolumes()
				logs.logsCreate(username_current=request.session["username"], volume_name=volume_name, volume_driver=volume_driver, driver_opts=opt_driver, labels=labels)

				return redirect("VolumesBoard")
		else:
			return render(request,"swarm_ui/templates/dashboard/volumes_create.html", result)
