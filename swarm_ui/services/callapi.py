from __future__ import unicode_literals
from django.conf import settings
import requests, json

class HttpRequestApiSwarm():

	def __connectInfo(self):
		info = {
			"swarm_protocol" : settings.API_DOCKER_SWARM["PROTOCOL"],
			"swarm_host" : settings.API_DOCKER_SWARM["HOST"],
			"swarm_port" : settings.API_DOCKER_SWARM["PORT"],
			"consul_protocol" : settings.API_CONSUL_MANAGER["PROTOCOL"],
			"consul_host" : settings.API_CONSUL_MANAGER["HOST"],
			"consul_port" : settings.API_CONSUL_MANAGER["PORT"],
		}
		return info	

	def listAll(self, parammeter):
		get_api_info = "%s://%s:%s/%s" %( self.__connectInfo()['swarm_protocol'], self.__connectInfo()['swarm_host'], self.__connectInfo()['swarm_port'], parammeter)
		
		try:
			request_get = requests.get(get_api_info, timeout=10)
		except requests.HTTPError , e:
			print e

		try:
		  	respone = {
			  	"respone_code": request_get.status_code,
			  	"respone_header": request_get.headers,
			  	"respone_cookie": request_get.cookies,
		  	}
		except requests.exceptions.RequestException, e:
			return "Error: {}".format(e)

		try:
		  	respone["respone_content"] = request_get.json()
		except:
			respone["respone_content"] = request_get


		request_get.connection.close()					

		return respone["respone_content"]

	def postUrl(self, parammeter, data, type_header):
		respone = {}
		post_api_info = "%s://%s:%s/%s" %( self.__connectInfo()['swarm_protocol'], self.__connectInfo()['swarm_host'], self.__connectInfo()['swarm_port'], parammeter)
		if type_header == 'type_json':
			headers = {'Content-Type': 'application/json'}
			try:
				request_post = requests.post(post_api_info,  data=json.dumps(data), headers=headers)
			except requests.HTTPError , e:
				print e



		elif type_header == 'type_text':
			headers = {'Content-Type': 'application/json'}
			try:
				request_post = requests.post(post_api_info, data=data, headers=headers)
			except requests.HTTPError, e:
				print e
		else:
			headers = {'Content-Type': 'text/plain'}
			try:
				request_post = requests.post(post_api_info, data=data, headers=headers)
			except urllib2.HTTPError, e:
				print e	


		try:
		  	respone = {
			  	"respone_code": request_post.status_code,
			  	"respone_header": request_post.headers,
			  	"respone_cookie": request_post.cookies,
		  	}
		except requests.exceptions.RequestException, e:
			return "Error: {}".format(e)

		try:
		  	respone["respone_content"] = request_post.json()
		except:
			respone["respone_content"] = request_post
			
		request_post.connection.close()
		return 	respone

	def deleteUrl(self, parammeter):

		response = {}
		delete_api_info = "%s://%s:%s/%s" %( self.__connectInfo()['swarm_protocol'], self.__connectInfo()['swarm_host'], self.__connectInfo()['swarm_port'], parammeter)
		headers = {'Content-Type': 'text/plain'}
		try:
			curl = requests.delete(delete_api_info,  headers=headers)
			try:
				content = curl.json()
			except Exception, e:
				content = curl
				
		  	response = {
			  	"code": curl.status_code,
			  	"respone_header": curl.headers,
			  	"respone_cookie": curl.cookies,
			  	"data": content,
		  	}
		except requests.exceptions.RequestException, e:
			return "Error: {}".format(e)
		 
		curl.connection.close()
		return 	response
	

class HttpRequestApiConsul():

	def __init__(self):
		host = settings.API_CONSUL_MANAGER["HOST"]
		port = settings.API_CONSUL_MANAGER["PORT"]
		self.url = "http://%s:%s" %(host, port)

	def get(self, param=None, headers=None):
		api = self.url + param
		try:
			curl = requests.get(api, headers=headers)
			try:
				content = curl.json()
			except Exception, e:
				content = curl
		  	respone = {
			  	"respone_code": curl.status_code,
			  	"respone_header": curl.headers,
			  	"respone_cookie": curl.cookies,
			  	"respone_content": content,
		  	}
		except requests.exceptions.RequestException as e:
			return "Error: {}".format(e)

		curl.connection.close()
		return	respone

	def put(self, param=None ,data={}):
		api = self.url + param
		try:
			curl = requests.put(api, data=json.dumps(data))
		  	respone = {
			  	"respone_code": curl.status_code,
			  	"respone_header": curl.headers,
			  	"respone_cookie": curl.cookies,
			  	"respone_content": curl.json(),
		  	}
		except requests.exceptions.RequestException, e:
			return "Error: {}".format(e)
		 
		curl.connection.close()
		return 	respone	

	def delete(self, param=None, data={}, headers=None):
		api = self.url + param
		try:
			curl = requests.delete(api, data=json.dumps(data), headers=headers)
			try:
				content = curl.json()
			except Exception, e:
				content = curl
				
		  	respone = {
			  	"respone_code": curl.status_code,
			  	"respone_header": curl.headers,
			  	"respone_cookie": curl.cookies,
			  	"respone_content": content,
		  	}
		except requests.exceptions.RequestException, e:
			return "Error: {}".format(e)
		 
		curl.connection.close()
		return 	respone			

class HttpRequestApiRegistry():

	def __init__(self, ip_regsitry, port_regsitry):
	    self.url = 'http://' + str(ip_regsitry) + ':' + str(port_regsitry)

	def get(self, param=None, headers=None):
		api = self.url + param
		try:
			curl = requests.get(api, headers=headers)
		  	respone = {
			  	"respone_code": curl.status_code,
			  	"respone_header": curl.headers,
			  	"respone_cookie": curl.cookies,
		  	}
		  	try:
		  		respone["respone_content"] = curl.json()
		  	except:
		  		respone["respone_content"] = curl
		except requests.exceptions.RequestException as e:
			return "Error: {}".format(e)
		 
		curl.connection.close()
		return	respone

	def post(self, param=None ,data={}):
		api = self.url + param
		try:
			curl = requests.post(api, data=json.dumps(data))
		  	respone = {
			  	"respone_code": curl.status_code,
			  	"respone_header": curl.headers,
			  	"respone_cookie": curl.cookies,
			  	"respone_content": curl.json(),
		  	}
		except requests.exceptions.RequestException, e:
			return "Error: {}".format(e)
		 
		curl.connection.close()
		return 	respone	

	def delete(self, param=None, headers=None):
		api = self.url + param
		try:
			curl = requests.delete(api,headers=headers)
		  	respone = {
			  	"respone_code": curl.status_code,
			  	"respone_header": curl.headers,
			  	"respone_cookie": curl.cookies,
			  	"respone_content": curl.json(),
		  	}
		except requests.exceptions.RequestException, e:
			return "Error: {}".format(e)
		 
		curl.connection.close()
		return 	respone	