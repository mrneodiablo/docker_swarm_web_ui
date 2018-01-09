from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from . import services
from . import writelogs
import json

class Nodes():

	def __init__(self):
		self.__node_read_only = "8"
		self.__node_admin = "3"
		self.__admin = "1"

	def decorator_node_permission(func):
		def case_decorator(self, request, *args, **kwargs):
			try:
				session_vali = request.session["username"]
			except:
				session_vali = None

			if session_vali != None:

				if  self.__admin in request.session["permission"] or self.__node_read_only in request.session["permission"] or self.__node_admin in request.session["permission"]:
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

				if  self.__admin in request.session["permission"] or self.__node_admin in request.session["permission"]:
					return func(self, request, *args, **kwargs)
				else:
					return redirect("PermissionDeny")	
			else:
				return redirect("LoginBoard")	
		return case_decorator


	@decorator_node_permission
	def board(self, request):
		node_api = services.NodeApi()
		if request.method != "POST":
			result = {"return_value":node_api.fetchAll()}
			return render(request, "swarm_ui/templates/dashboard/node_board.html", result)
		elif request.method == "POST" and request.POST.get("tim") == "tim" :
			host = request.POST.get("host")
			result = {"return_value":node_api.searchNode(host)}
			return render(request, "swarm_ui/templates/dashboard/node_board.html", result)
		elif request.method == "POST" and request.POST.get("ok_remove") != None:
			#@@write log ############################
			logs = writelogs.LogsForNodes()
			logs.logsRemove(username_current=request.session["username"], node_ip=request.POST.get("ok_remove"))
			key_node = request.POST.get("ok_remove")
			node_api.removeNode(key_node)
			result = {"return_value": node_api.fetchAll()}
			return render(request, "swarm_ui/templates/dashboard/node_board.html", result)
		else:
			return redirect("PermissionDeny")											

	@decorator_node_permission
	def detail(self, request, host):
		node_api = services.NodeApi()
		result = {"return_value": node_api.searchNode(host)}
		return render(request, "swarm_ui/templates/dashboard/node_detail.html", result)


	@csrf_exempt
	def apiGetCpuNode(self, request):
		if request.method == "POST":
			if request.POST.get("name") != "None":
				node_api = services.NodeApi()

				data = node_api.searchNode(request.POST.get("name"))
				cpu = data[0]["cpus"].split("/")[1].strip(" ")
				result = {
					"status": 1,
					"data": cpu,
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
