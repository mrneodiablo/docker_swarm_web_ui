from django.shortcuts import render, redirect
from swarm_ui.models import LogsUser
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count

class ManagerLogs(object):

	def __init__(self):
		self.__logs_admin = "14"
		self.__admin = "1"

	def decorator_admin_permission(func):	
		def case_decorator(self, request, *args, **kwargs):
			for key, value in kwargs.items():
				print key + ":" + value
			try:
				session_vali = request.session["username"]
			except:
				session_vali = None

			if session_vali != None:
				if  self.__admin in request.session["permission"] or self.__logs_admin in request.session["permission"]:
					return func(self, request, *args, **kwargs)
				else:
					return redirect("PermissionDeny")	
			else:
				return redirect("LoginBoard")

		return case_decorator				

	@decorator_admin_permission
	def board(self, request):

		if request.method == "POST":
			if request.POST.get("ok_filter") != "" and request.POST.get("ok_filter") == "yes" :
				
				# assign variable
				user_filter = request.POST.get("username")
				function_filter = request.POST.get("function")

				if request.POST.get("date") != "":
					date_filter = request.POST.get("date")
				else:
					date_filter = ""

				#filter 
				if user_filter != "all":
					if function_filter != "all":
						if date_filter != "":
							# Filter user_filter + function_filter + date_filter
							logs_active_user = LogsUser.objects.filter(username=user_filter,feature=function_filter, time__lte=date_filter+" "+"23:59:59", time__gte=date_filter+" "+"00:00:00").values("id","username", "action", "feature", "message", "time", "message").order_by("-id")
						else:
							#Filter user_filter + function_filter
							logs_active_user = LogsUser.objects.filter(username=user_filter,feature=function_filter).values("id","username", "action", "feature", "message", "time", "message").order_by("-id")

					else:
						if date_filter != "":
							# Filter user_filter + date_filter
							logs_active_user = LogsUser.objects.filter(username=user_filter, time__lte=date_filter+" "+"23:59:59", time__gte=date_filter+" "+"00:00:00").values("id","username", "action", "feature", "message", "time", "message").order_by("-id")
						else:
							#Filter user_filter
							logs_active_user = LogsUser.objects.filter(username=user_filter).values("id","username", "action", "feature", "message", "time", "message").order_by("-id")	
				else:
					if function_filter != "all":
						if date_filter != "":
							#Filter function_filter + date
							logs_active_user = LogsUser.objects.filter(time__lte=date_filter+" "+"23:59:59", time__gte=date_filter+" "+"00:00:00",feature=function_filter).values("id","username", "action", "feature", "message", "time", "message").order_by("-id")
						else:
							# filter function_filter
							logs_active_user = LogsUser.objects.filter(feature=function_filter).values("id","username", "action", "feature", "message", "time", "message").order_by("-id")								
					else:
						if date_filter != "":
							#Filter date
							logs_active_user = LogsUser.objects.filter(time__lte=date_filter+" "+"23:59:59", time__gte=date_filter+" "+"00:00:00").values("id","username", "action", "feature", "message", "time", "message").order_by("-id")
						else:
							# No filter
							logs_active_user = LogsUser.objects.values("id","username", "action", "feature", "message", "time", "message").order_by("-id")

				#get user name write logs
				user_filter = LogsUser.objects.values("username").annotate(count=Count('username'))

				#get function logs 
				function_filter = LogsUser.objects.values("feature").annotate(count=Count("feature"))
				
				

				result = {
					"contacts": logs_active_user,
	        		"user_filter": user_filter,
	        		"function_filter": function_filter,
				}

				return render(request, "swarm_ui/templates/dashboard/logs_board.html", result)		
						
		else:			
			#get user name write logs
			user_filter = LogsUser.objects.values("username").annotate(count=Count('username'))

			#get function logs 
			function_filter = LogsUser.objects.values("feature").annotate(count=Count("feature"))

			logs_active_user = LogsUser.objects.values("id","username", "action", "feature", "message", "time", "message").order_by("-id")
			record_per_page = 20
			paginator = Paginator(logs_active_user, record_per_page)

			try:
				page = int(request.GET.get('page'))
			except Exception, e:
				print e
				page = 1
			
			### show range page
			page_range = []
			if page-2 >= 1 and page+2 <= paginator.num_pages:
				for x in xrange(page-2,page+3):
					page_range.append(x)

			if page-2 < 1 and page+2 <= paginator.num_pages:
				for x in xrange(1,page+3):
					page_range.append(x)

			if page-2 >= 1 and page+2 > paginator.num_pages:		
				for x in xrange(page-2,paginator.num_pages+1):
					page_range.append(x)

			if page-2 < 1 and page+2 > paginator.num_pages:		
				for x in xrange(1,paginator.num_pages+1):
					page_range.append(x)							

			#get object per page
			try:
				contacts = paginator.page(page)
			except PageNotAnInteger:
				contacts = paginator.page(1)
			except EmptyPage:
				contacts = paginator.page(paginator.num_pages)
        	

			result = {
				"contacts": contacts,
        		"current_page": page,
        		"page_range": page_range,
        		"user_filter": user_filter,
        		"function_filter": function_filter,
        		"last_page":  paginator.num_pages,
			}

			return render(request, "swarm_ui/templates/dashboard/logs_board.html", result)		
