from .callapi import HttpRequestApiRegistry
import json

class RegistryDocker():

	def __init__(self, ip_regsitry, port_regsitry):
	 self.request = HttpRequestApiRegistry(ip_regsitry=ip_regsitry, port_regsitry=port_regsitry)  

	def checkRegistry(self):
		param = "/v2/"
		check = self.request.get(param)
		try:
			if check["respone_code"] == 200:
				return 1
			else:
				return 0	
		except:
			return check

	def listRepo(self):
		param = "/v2/_catalog"
		list_repo = self.request.get(param)
		try:
			return list_repo["respone_content"]
		except:
			raise list_repo

	def listTags(self, name):
		param = "/v2/%s/tags/list" %(name)
		list_repo = self.request.get(param)
		respone = {}
		try:
			respone["data"] = list_repo["respone_content"]["errors"]
			respone["status"] = 0		
		except Exception:
			respone["status"] = 1
			respone["data"] = list_repo["respone_content"]
		return respone

	def __listManifestsSchema1(self, name, tag):

		param = "/v2/%s/manifests/%s" %(name, tag)
		list_repo = self.request.get(param)
		respone = {}
		try:
			respone["data"] = list_repo["respone_content"]["errors"]
			respone["status"] = 0		
		except Exception:
			respone["status"] = 1
			respone["data"] = list_repo["respone_content"]
		return respone	

	def __listManifestsSchema2(self, name, tag):

		param = "/v2/%s/manifests/%s" %(name, tag)
		headers = {
					'accept': 'application/vnd.docker.distribution.manifest.v2+json',
		}
		list_repo = self.request.get(param,headers=headers)
		respone = {}
		try:
			respone["data"] = list_repo["respone_content"]["errors"]
			respone["status"] = 0		
		except Exception:
			respone["status"] = 1
			respone["data"] = list_repo["respone_content"]
		return respone

	def __getDigest(self, name, tag):

		param = "/v2/%s/manifests/%s" %(name, tag)
		headers = {
					'accept': 'application/vnd.docker.distribution.manifest.v2+json',
		}
		list_repo = self.request.get(param,headers=headers)
		respone = {}
		try:
			respone["data"] = list_repo["respone_content"]["errors"]
			respone["status"] = 0		
		except Exception:
			respone["status"] = 1
			respone["data"] = list_repo["respone_header"]
		return respone	

	def deleteManifests(self, name, tag):
		try:
			digest = self.__getDigest(name, tag)["data"]["Docker-Content-Digest"]
		except Exception, e:
			raise e
			digest = None
		
		param = "/v2/%s/manifests/%s" %(name, digest)
		headers = {
					'accept': 'application/vnd.docker.distribution.manifest.v2+json',
		}
		list_repo = self.request.delete(param, headers=headers)
		respone = {}
		try:
			respone["data"] = list_repo["respone_content"]["errors"]
			respone["status"] = 0		
		except Exception:
			respone["status"] = 1
			respone["data"] = list_repo["respone_header"]
		return respone

	def showManifests(self, name, tag):
		schema1 = self.__listManifestsSchema1(name, tag)
		schema2 = self.__listManifestsSchema2(name, tag)
		return_value = []
		for x in xrange(0,len(schema1["data"]["fsLayers"])):
			result = None
			for z in xrange(0,len(schema2["data"]["layers"])):
				if schema1["data"]["fsLayers"][x]["blobSum"] == schema2["data"]["layers"][z]["digest"]:
					result = {
						"Image": json.loads(schema1["data"]["history"][x]["v1Compatibility"])["id"],
						"Cmd": json.loads(schema1["data"]["history"][x]["v1Compatibility"])["container_config"]["Cmd"],
						"Created": json.loads(schema1["data"]["history"][x]["v1Compatibility"])["created"].split("T")[0] + " " + json.loads(schema1["data"]["history"][x]["v1Compatibility"])["created"].split("T")[1].split("Z")[0],
						"Size": schema2["data"]["layers"][z]["size"]
					}
			if result == None:			
				result = {
					"Image": json.loads(schema1["data"]["history"][x]["v1Compatibility"])["id"],
					"Cmd": json.loads(schema1["data"]["history"][x]["v1Compatibility"])["container_config"]["Cmd"],
					"Created": json.loads(schema1["data"]["history"][x]["v1Compatibility"])["created"].split("T")[0] + " " + json.loads(schema1["data"]["history"][x]["v1Compatibility"])["created"].split("T")[1].split("Z")[0],
					"Size": 0,
				}

			return_value.append(result)
				
		return 	return_value