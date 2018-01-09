from django.shortcuts import render, redirect
from . import services 
from . import writelogs
 

class Images():

	def __init__(self):
		self.__image_read_only = "11"
		self.__image_admin = "6"
		self.__admin = "1"

	def decorator_image_permission(func):
		def case_decorator(self, request, *args, **kwargs):
			try:
				session_vali = request.session["username"]
			except:
				session_vali = None

			if session_vali != None:

				if  self.__admin in request.session["permission"] or self.__image_admin in request.session["permission"] or self.__image_read_only in request.session["permission"]:
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

				if  self.__admin in request.session["permission"] or self.__image_admin in request.session["permission"]:
					return func(self, request, *args, **kwargs)
				else:
					return redirect("PermissionDeny")	
			else:
				return redirect("LoginBoard")	
		return case_decorator

	@decorator_image_permission
	def board(self, request):
		images_api = services.ImagesApi()
		if request.method == "POST":
			if request.POST.get("ok_remove") and (self.__admin in request.session["permission"] or self.__image_admin in request.session["permission"]):
				if request.POST.get("check_force_remove_image") and request.POST.get("check_force_remove_image") == "1":
					force_remove_image = request.POST.get("check_force_remove_image")
				else:
					force_remove_image = "0"

				result = images_api.removeImage(request.POST.get("ok_remove"), force_remove_image=force_remove_image)
				
				#@@write logs ##########################################
				logs = writelogs.LogsForImages()
				logs.logsRemove(username_current=request.session["username"], image_id=request.POST.get("ok_remove"), force_remove=force_remove_image)

			else:
				return redirect("PermissionDeny")

			if request.POST.get("ok_find") and request.POST.get("ok_find") == 'yes':
				if request.POST.get("name_image"):
					name_image = request.POST.get('name_image')
					result = {"return_value": images_api.searchImage(name_image)}
					return render(request, "swarm_ui/templates/dashboard/image_board.html", result)
				else:
					result = {"return_value": images_api.fetchAll()}	
					return render(request, "swarm_ui/templates/dashboard/image_board.html", result)							
		
		result = {"return_value": images_api.fetchAll()}	
		return render(request, "swarm_ui/templates/dashboard/image_board.html", result)
	
	
	@decorator_admin_permission
	def pull(self, request):
		images_api = services.ImagesApi()
		if request.POST.get("pull"):
			if request.POST.get("registry"):
		 		registry = request.POST.get("registry")
		 	else:
		 		registry = ""

			if request.POST.get("image"):
		 		image = request.POST.get("image")
		 	else:
		 		image = ""

			if request.POST.get("tag"):
		 		tag = request.POST.get("tag")
		 	else:
		 		tag = ""

		 	images_api.pullImage(registry, image, tag)

		 	#@@write logs ############################
		 	logs = writelogs.LogsForImages()
		 	logs.logsPull(username_current=request.session["username"], image=image, registry=registry, tag=tag)

		 	return redirect('ImagesBoard')

	@decorator_admin_permission
	def tag(self, request):
			
		images_api = services.ImagesApi()
		if request.POST.get("ok_tag"):
			id_image = request.POST.get("ok_tag")
			if request.POST.get("repo"):
		 		repo = request.POST.get("repo")
		 	else:
		 		repo = ""

			if request.POST.get("tag"):
		 		tag = request.POST.get("tag")
		 	else:
		 		tag = ""

			if request.POST.get("check_force"):
		 		force = request.POST.get("check_force")
		 	else:
		 		force = 0

		 	images_api.tagImage( id_image, repo, force, tag)

		 	#@@write logs ######################
		 	logs = writelogs.LogsForImages()
		 	logs.logsTag(username_current=request.session["username"], id_image=id_image, repo=repo, tag=tag)

		 	return redirect('ImagesBoard')

	@decorator_image_permission
  	def detail(self, request, images_id):		
  		images_api = services.ImagesApi()
  		if request.method == "POST":
  			if  self.__admin in request.session["permission"] or self.__image_admin in request.session["permission"] :
	  			if request.POST.get("ok_remove"):
	  				if request.POST.get("check_force_remove_image") and request.POST.get("check_force_remove_image") == "1":
						force_remove_image = request.POST.get("check_force_remove_image")
					else:
						force_remove_image = "0"

	  				images_api.removeImage(request.POST.get("ok_remove"), force_remove_image=force_remove_image)

					#@@write logs ##########################################
					logs = writelogs.LogsForImages()
					logs.logsRemove(username_current=request.session["username"], image_id=request.POST.get("ok_remove"), force_remove=force_remove_image)	
							  				
	  				return redirect('ImagesBoard')
			else:
				return redirect("PermissionDeny")

		result = {"return_value":images_api.inspectImage(images_id), "history_value": images_api.historyImage(images_id)}
		return render(request, "swarm_ui/templates/dashboard/image_detail.html", result)

