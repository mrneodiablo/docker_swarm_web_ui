from django.shortcuts import render, redirect
from django.db.models import Count
from swarm_ui.models import Product 
from . import services

from django.shortcuts import render_to_response
from django.template import RequestContext
 
class DashBoard():

	def checkLogin(func):
		def wrapper(self, request):
			try:
				session_vali = request.session["username"]
			except:
				session_vali = None

			if session_vali != None:
				return func(self, request)
			else:		
				return redirect("LoginBoard")	
		return wrapper

	@checkLogin
	def index(self, request):
		swarminfo = services.InfoApi()
		result = swarminfo.fetchAll()
		result["product_total"] = len(Product.objects.values('name').annotate(dcount=Count('name')))
		return render(request, "swarm_ui/templates/dashboard/index.html", result)

def page_not_found(request):
	return render_to_response('swarm_ui/templates/error/page_not_found.html', RequestContext(request))

