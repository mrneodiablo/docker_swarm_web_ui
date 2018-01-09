from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponse
from swarm_ui.models import Registry
from . import services
from . import writelogs
import json

class ManagerRegistry():

	def __init__(self):
		self.__registry_read_only = "14"
		self.__registry_admin = "15"
		self.__admin = "1"

	def checklogin(self, request):
		try:
			x = request.session["username"]
		except:
			x = None
		return x

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
		if request.method == "POST":
			if  self.__admin in request.session["permission"] or self.__registry_admin  in request.session["permission"]:		
				if request.POST.get("ok_remove") and request.POST.get("ok_remove") != "":
					registry_name = request.POST.get("ok_remove")

					#@@write log ############################
					logs = writelogs.LogsForRegistry()
					logs.logsRemove(username_current=request.session["username"], name_registry=registry_name )
					Registry.objects.filter(name=registry_name).delete()

				elif request.POST.get("ok_add") and request.POST.get("ok_add") != "":
					name = request.POST.get("name_registry")
					ip = request.POST.get("ip_registry")
					port = request.POST.get("port_registry")
					registry = services.RegistryDocker(ip_regsitry=ip, port_regsitry=port)
					if registry.checkRegistry():
						#@@write log ############################
						logs = writelogs.LogsForRegistry()
						logs.logsAdd(username_current=request.session["username"], name_registry=registry, ip_registry=ip, port_registry=port )

						insert = Registry(name=name,ip=ip,port=port)
						insert.save()	


				return redirect("RegistryBoard")					
			else:
				return redirect("PermissionDeny")				
		else:		
	
			registry = Registry.objects.all().values("name", "ip", "port")
			registry_result = []
			for x in xrange(0, len(registry)):
				tmp = {}		
				tmp["name"] = 	registry[x]["name"]
				tmp["port"] = registry[x]["port"]
				tmp["ip"] = registry[x]["ip"]
				registry_result.append(tmp)

			result = {
				"return_value": registry_result
			}
			return render(request, "swarm_ui/templates/dashboard/registry_board.html", result)

	def detail(self, request, name_registry):
		if self.checklogin(request) != None:
			ip = Registry.objects.filter(name=name_registry).values("ip")[0]["ip"]
			port = Registry.objects.filter(name=name_registry).values("port")[0]["port"]
			registry = services.RegistryDocker(ip_regsitry=ip, port_regsitry=port)
			if request.method == "POST":
				if  request.POST.get("okie") != None:
					images = request.POST.get("okie").split("|")[0]
					tag = request.POST.get("okie").split("|")[1]
					list_all = registry.showManifests(images, tag)
					result = {
						"return_value": list_all,
						"registry_name": name_registry,
						"images_name": images,
						"tag_name": tag,
					}
					return render(request, "swarm_ui/templates/dashboard/registry_detail_manifest.html", result)

				elif request.POST.get("okie_remove") != None:
					images = request.POST.get("okie_remove").split("|")[0]
					tag = request.POST.get("okie_remove").split("|")[1]

					#@@write log ############################
					logs = writelogs.LogsForRegistry()
					logs.logsRemoveImage(username_current=request.session["username"], name_registry=images ,tag_registry=tag)

					registry.deleteManifests(images, tag)
					list_repo = registry.listRepo()
					list_all = {}
					for repo in list_repo["repositories"]:
						list_all[repo] = registry.listTags(repo)

					result = {
						"return_value": list_all,
						"registry_name": name_registry
					}
					return render(request, "swarm_ui/templates/dashboard/registry_detail.html", result)					
			else:
				list_repo = registry.listRepo()
				list_all = {}
				for repo in list_repo["repositories"]:
					list_all[repo] = registry.listTags(repo)

				result = {
					"return_value": list_all,
					"registry_name": name_registry
				}
				return render(request, "swarm_ui/templates/dashboard/registry_detail.html", result)
		else:
			return redirect("LoginBoard")	

	@csrf_exempt
	def apiListImages(self, request):
		if request.method == "POST":
			if request.POST.get("registry") != "None":

				name_registry = request.POST.get("registry")
				ip = Registry.objects.filter(name=name_registry).values("ip")[0]["ip"]
				port = Registry.objects.filter(name=name_registry).values("port")[0]["port"]
				registry = services.RegistryDocker(ip_regsitry=ip, port_regsitry=port)
				repo_data = {}

				
				list_repo = registry.listRepo()
				for repo in list_repo["repositories"]:
					repo_data[repo] = registry.listTags(repo)

				data = {
					"repo_ip": ip,
					"repo_port": port,
					"repo_data" : repo_data
				}
				result = {
					"status": 1,
					"data": data,
					}
			elif request.POST.get("registry") == "None":
				result = {
					"status": 0,
					"data": "None",
					}					
		else:
			result = {
				"status": 0,
				"data": "method fail",
				}

		return HttpResponse(json.dumps(result))		