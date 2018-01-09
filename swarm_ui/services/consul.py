#!/usr/bin/python
from .callapi import HttpRequestApiConsul

class ConsulApi():
	def __init__(self):
	    self.api = HttpRequestApiConsul()

	def listDatacenters(self):
		param = "/v1/catalog/datacenters"
		return self.api.get(param)


############### node ##########################
	def listNodes(self):
		param = "/v1/catalog/nodes"
		return self.api.get(param)

	def listServiceNodes(self, node):
		param = "/v1/catalog/node/%s" %(node)
		return self.api.get(param)


############### health check ##################
	
	# Returns the health info of a node
	def healthNode(self, node):
		param = "/v1/health/node/%s" %(node)
		return self.api.get(param)

	# Returns the checks of a service
	def healthCheck(self, service):
		param = "/v1/health/checks/%s" %(service)
		return self.api.get(param)

	# Returns the nodes and health info of a service
	def serviceCheck(self, service):
		param = "/v1/health/service/%s" %(service)
		return self.api.get(param)


############### list all key ##################
	
	# List all key 
	def listKeys(self):
		param = "/v1/kv/?recurse"
		return self.api.get(param)

	# Remove key
	def removeKeys(self, mdindex=None, removeall=None, key=None):
		if removeall == 1:
			param = "/v1/kv/?recurse"
			return self.api.delete(param)
		else:
			payload = {
				"cas": mdindex,
			}
			param = "/v1/kv/%s" %(key)
			return self.api.delete(param, data=payload)

	# Add key
	def addKeys(self, key, value):
		param = "/v1/kv/%s" %(key)
		data = {
			"Value": value
		}
		return self.api.put(param, data=data)

	# Update key
	def updateKeys(self, key, value, mdindex):
		param = "/v1/kv/%s" %(key)
		data = {
			"Value": value,
			"cas": mdindex

		}
		return self.api.put(param, data=data)
