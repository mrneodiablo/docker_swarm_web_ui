from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from swarm_ui.models import UserPermissions
from . import writelogs



class LoginUser():

	def login(self, request):
		
		permission_user = []
		if request.method == "POST":
			username = request.POST.get("username")
			password = request.POST.get("password")
			user = auth.authenticate(username=username, password=password)
			if user is not None:
				request.session["username"] = username
				session_permission = UserPermissions.objects.filter(username_id=User.objects.filter(username=request.session["username"]).values("id")).values("permission_code_id")

				for per in xrange(0, len(session_permission)):
					permission_user.append(str(session_permission[per]["permission_code_id"]))
				request.session["permission"] = permission_user

				#@@write logs
				logs = writelogs.LoginLogout()
				logs.logsLogin(username_current=request.session["username"])

				return redirect("DashBoard")
			else:

				return render(request, "swarm_ui/templates/dashboard/login.html")
		else:	
			return render(request, "swarm_ui/templates/dashboard/login.html")

	def logout(self, request):

		username_current = request.session["username"]
		
		request.session.flush()

		#@@write logs
		logs = writelogs.LoginLogout()
		logs.logsLogout(username_current=username_current)

		return redirect("LoginBoard")

class ManagerUser():

	def __init__(self):
		self.__user_read_only = "13"
		self.__user_admin = "12"
		self.__admin = "1"

	def checklogin(self, request):
		try:
			x = request.session["username"]
		except:
			x = None
		return x

	def decorator_user_permission(func):
		def case_decorator(self, request, *args, **kwargs):
			try:
				session_vali = request.session["username"]
			except:
				session_vali = None

			if session_vali != None:

				if  self.__admin in request.session["permission"] or self.__user_admin in request.session["permission"] or self.__user_read_only in request.session["permission"]:
					return func(self, request, *args, **kwargs)
				else:
					return redirect("PermissionDeny")	
			else:
				return redirect("LoginBoard")
		return case_decorator

	def decorator_admin_permission(func):	
		def case_decorator(self, request, *args, **kwargs):
			for key, value in kwargs.items():
				print key + ":" + value
			try:
				session_vali = request.session["username"]
			except:
				session_vali = None

			if session_vali != None:
				if  self.__admin in request.session["permission"] or self.__user_admin in request.session["permission"]:
					return func(self, request, *args, **kwargs)
				else:
					return redirect("PermissionDeny")	
			else:
				return redirect("LoginBoard")

		return case_decorator							
			
	@decorator_user_permission
	def board(self, request):		
		if request.method == "POST":
			if  self.__admin in request.session["permission"] or self.__user_admin in request.session["permission"]:		
				if request.POST.get("ok_remove_user") and request.POST.get("ok_remove_user") != "":
					user_id = request.POST.get("ok_remove_user")
					self.remove(request, user_id)

					return redirect("UserBoard")
			else:
				return redirect("PermissionDeny")				
		else:		
			user_result = []		
			sqlusers = User.objects.filter(is_staff=0, is_active=1).values("id","username", "first_name", "last_name")
			for x in xrange(0, len(sqlusers)):
				user = {}
				user["user_id"] = 	sqlusers[x]["id"]
				user["username"] = 	sqlusers[x]["username"]
				user["first_name"] = sqlusers[x]["first_name"]
				user["last_name"] = sqlusers[x]["last_name"]
				user["permission"] = UserPermissions.objects.filter(username_id=sqlusers[x]["id"]).values("permission_code__name")
				user_result.append(user)
			result = {
			"return_value": user_result
			}
			return render(request, "swarm_ui/templates/dashboard/user_board.html", result)

	@decorator_admin_permission		
	def update(self, request, username):
		if request.method == "POST":
			if  self.__admin in request.session["permission"] or self.__user_admin in request.session["permission"]:
				if request.POST.get("ok_update") and request.POST.get("ok_update") != "":
					username_id = request.POST.get("ok_update")
					username = request.POST.get("username")
					password = request.POST.get("password")
					if 	request.POST.get("firstname") and request.POST.get("firstname") != "":
						firstname = request.POST.get("firstname")
					else:
						firstname = ""

					if 	request.POST.get("lastname") and request.POST.get("lastname") != "":
						lastname = request.POST.get("lastname")
					else:
						lastname = ""

					permission_code = {
						"1": request.POST.get("administrator"),
						"2": request.POST.get("container_admin"),
						"3": request.POST.get("node_admin"),
						"4": request.POST.get("volume_admin"),
						"5": request.POST.get("network_admin"),
						"6": request.POST.get("image_admin"),
						"7": request.POST.get("container_read_only"),
						"8": request.POST.get("node_read_only"),
						"9": request.POST.get("volume_read_only"),
						"10": request.POST.get("network_read_only"),
						"11": request.POST.get("image_read_only"),
						"12": request.POST.get("user_admin"),
						"13": request.POST.get("user_read_only"),
						"14": request.POST.get("log_admin"),
					}
					update_user = User.objects.get(id=username_id)
					update_user.username = username
					update_user.first_name = firstname
					update_user.last_name = lastname
					if password and password != "":
						update_user.set_password(password)
					update_user.save()	


					remove_permission = UserPermissions.objects.filter(username_id=username_id)
					remove_permission.delete()
					permission_user_logs = []
					for key_permission, value_permission in permission_code.items():
						if value_permission == "1" and value_permission != None :
							permission_user_logs.append(key_permission)
							p = UserPermissions(username_id=username_id, permission_code_id=key_permission)
							p.save()

					#@@write logs
					logs = writelogs.LogsForusers()
					logs.logsUpdate(username_current=request.session["username"], username=username, firstname=firstname, lastname=lastname, permission_user_logs=permission_user_logs)

				return redirect("UserBoard")			
			else:
				return redirect("PermissionDeny")			
		else:		
			user_result = []
			sqlusers = User.objects.filter(is_staff=0, is_active=1, username=username).values("id","username", "first_name", "last_name")
			for x in xrange(0, len(sqlusers)):
				user = {}
				user["user_id"] = 	int(sqlusers[x]["id"])
				user["username"] = 	sqlusers[x]["username"]
				user["first_name"] = sqlusers[x]["first_name"]
				user["last_name"] = sqlusers[x]["last_name"]
				user["permission"] = []
				user_permission = UserPermissions.objects.filter(username_id=sqlusers[x]["id"]).values("permission_code_id")					
				for value in user_permission:
					user["permission"].append(str(value["permission_code_id"]))
				user_result.append(user)
			result = {
			"return_value": user_result
			}
			return render(request, "swarm_ui/templates/dashboard/user_detail.html", result)					
	
	@decorator_admin_permission
	def create(self, request):
		if request.method == "POST":
			if request.POST.get("ok_create") and request.POST.get("ok_create") == "ok_create":
				username = request.POST.get("username")
				password = request.POST.get("password")
				if 	request.POST.get("firstname") and request.POST.get("firstname") != "":
					firstname = request.POST.get("firstname")
				else:
					firstname = ""

				if 	request.POST.get("lastname") and request.POST.get("lastname") != "":
					lastname = request.POST.get("lastname")
				else:
					lastname = ""

				permission_code = {
					"1": request.POST.get("administrator"),
					"2": request.POST.get("container_admin"),
					"3": request.POST.get("node_admin"),
					"4": request.POST.get("volume_admin"),
					"5": request.POST.get("network_admin"),
					"6": request.POST.get("image_admin"),
					"7": request.POST.get("container_read_only"),
					"8": request.POST.get("node_read_only"),
					"9": request.POST.get("volume_read_only"),
					"10": request.POST.get("network_read_only"),
					"11": request.POST.get("image_read_only"),
					"12": request.POST.get("user_admin"),
					"13": request.POST.get("user_read_only"),
				}

				User.objects.create_user(username=username, first_name=firstname, last_name=lastname, password=password, is_staff=0, is_active=1)
				user_id = User.objects.filter(username=username).values("id")[0]["id"]

				permission_user_logs = []
				for key_permission, value_permission in permission_code.items():
					if value_permission == "1" and value_permission != None:
						permission_user_logs.append(key_permission)
						p = UserPermissions(username_id=user_id, permission_code_id=key_permission)
						p.save()

				#@@ write logs
				logs =	writelogs.LogsForusers()
				logs.logsCreate(username_current=request.session["username"], username=username, firstname=firstname, lastname=lastname, permission_user_logs=permission_user_logs)	
				
				return redirect("UserBoard")										
		return render(request, "swarm_ui/templates/dashboard/user_create.html")	

	@decorator_admin_permission
	def remove(self, request, user_id): 
		username_remove = User.objects.filter(id=user_id).values("username")[0]["username"]
		#@@delete user, delete permission
		User.objects.filter(id=user_id).delete()
		UserPermissions.objects.filter(username_id=user_id).delete()

		#@@write logs
		logs = writelogs.LogsForusers()
		logs.logsRemove(username_remove=username_remove, username_current=request.session["username"])

