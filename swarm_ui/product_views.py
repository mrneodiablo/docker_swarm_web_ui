from django.shortcuts import render, redirect
from swarm_ui.models import Product
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import writelogs
import json


class Products():
	
	def __init__(self):
		self.__product_read_only = "16"
		self.__product_admin = "17"
		self.__admin = "1"

	def checksession(func):
		def wrapper(self, request):
			try:
				session_vali = request.session["username"]
			except:
				session_vali = None

			if session_vali != None:

				if  self.__admin in request.session["permission"] or self.__product_read_only in request.session["permission"] or self.__product_admin in request.session["permission"]:
					return func(self, request)
				else:
					return redirect("PermissionDeny")	
			else:
				return redirect("LoginBoard")	
		return wrapper

	@checksession
	def board(self, request):
		product = []
		if request.method == "POST":
			if self.__admin in request.session["permission"] or self.__product_admin in request.session["permission"]:
									
				if request.POST.get("ok_remove"):
					product_name = request.POST.get("ok_remove").split("|")[0]
					vlan_name = request.POST.get("ok_remove").split("|")[1]

					#@@write logs ##########################################
					logs = writelogs.LogsForProduct()
					logs.logsRemove(username_current=request.session["username"], product_name=product_name, vlan_name=vlan_name)

					Product.objects.filter(name=product_name, vlan=vlan_name).delete()
				
				elif request.POST.get("ok_add") and  request.POST.get("ok_add") == "ok_add":
					name = request.POST.get("name_product")
					status = request.POST.get("product_status")
					vlan = request.POST.get("name_vlan")
					subnet = request.POST.get("subnet")
					gateway = request.POST.get("gateway")
					scope = request.POST.get("product_scope")


					#@@write logs ##########################################
					logs = writelogs.LogsForProduct()
					logs.logsAdd(username_current=request.session["username"],  product_name=name, vlan_name=vlan, product_status=status, vlan_subnet=subnet, vlan_gateway=gateway, vlan_scope=scope)

					Product(name=name, status=status, vlan=vlan, subnet=subnet, gateway=gateway, scope=scope).save()
			else:		
				return redirect("PermissionDeny")

		product_tmp = Product.objects.all().values("name", "status", "container", "gateway", "subnet", "vlan", "scope")
		for value in product_tmp:
			product.append(value)			
		result = {"return_value": product}		
		return render(request, "swarm_ui/templates/dashboard/product_board.html", result)

	@csrf_exempt
	def apiInspect(self, request):
		list_product = []
		if request.method == "POST":
			try:
				product_name = request.POST.get("product")
			except:
				product_name = None 
			list_product_tmp = Product.objects.filter(status=1, name=product_name).values("name", "vlan", "gateway", "subnet")
			for key in list_product_tmp:
				list_product.append(key)
			result =  {
				"status": 1,
				"data": list_product,

			}
								
		else:
			result = {
				"status": 0,
				"data": "method fail",
				}		


		return HttpResponse(json.dumps(result))		