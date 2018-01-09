from django.shortcuts import render
from django.shortcuts import render_to_response
from  django.views.defaults import page_not_found

class Error():
	def permissionDeny(self, request):
		return render(request, "swarm_ui/templates/error/permission_deny.html")

def pageNotFound(request):
	page_not_found(request,  template_name="swarm_ui/templates/error/page_not_found.html")
	