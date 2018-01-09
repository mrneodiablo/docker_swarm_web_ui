
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class DriverNetworks(models.Model):
	driver = models.CharField(max_length=32)
	scope = models.CharField(max_length=32)
	def __str__(self):
		return self.driver
	class Meta:
		verbose_name_plural = 'Driver Networks'	

class DriverVolumes(models.Model):
	driver = models.CharField(max_length=32)
	scope = models.CharField(max_length=32)
	def __str__(self):
		return self.driver
	class Meta:
		verbose_name_plural = 'Driver Volumes'	
		
class Permissions(models.Model):
	name = models.CharField(max_length=32,verbose_name="Name")
	code = models.AutoField(primary_key=True,verbose_name="Code")
	class Meta:
		verbose_name_plural = 'Permissions'
	def __str__(self):
		return self.name		

class UserPermissions(models.Model):
	username = models.ForeignKey(User, verbose_name="User")
	permission_code = models.ForeignKey(Permissions, verbose_name="permission")
	class Meta:
		verbose_name_plural = 'User Permissions' 
	def __str__(self):
		return self.username.username

		
class LogsUser(models.Model):
	username = models.CharField(max_length=32,verbose_name="User")
	action = models.CharField(max_length=32,verbose_name="Action")
	feature = models.CharField(max_length=32,verbose_name="Feature")
	message = models.CharField(max_length=256,verbose_name="Messages")
	container = models.CharField(max_length=32,verbose_name="Container")
	node = models.CharField(max_length=32,verbose_name="Node")
	time = models.DateTimeField(auto_now_add=True)
	class Meta:
		verbose_name_plural = 'Logs Action User'
	def __str__(self):
		return self.username

class LogsLoginLogout(models.Model):
	username = models.CharField(max_length=32,verbose_name="User")
	action = models.CharField(max_length=32,verbose_name="Messages")
	time = models.DateTimeField(auto_now_add=True)
	class Meta:
		verbose_name_plural = 'Logs Login User'
	def __str__(self):
		return self.username

class Product(models.Model):
	VLAN_TYPE = [("1","private"),("2","public")]
	name = models.CharField(max_length=32, verbose_name="Product Name")
	vlan = models.CharField(max_length=32, verbose_name="Vlan Name")
	scope = models.CharField(max_length=32, choices=VLAN_TYPE, default="1", verbose_name="Type Vlan")
	subnet = models.CharField(max_length=32, verbose_name="IP Subnet ")
	gateway = models.CharField(max_length=32, verbose_name="IP Gateway")
	container = models.IntegerField(verbose_name="Total Container", default=0)
	status = models.BooleanField(default=1, verbose_name="Status")
	class Meta:
		verbose_name_plural = 'Product'
	def __str__(self):
		return self.name


class Registry(models.Model):
	name = models.CharField(max_length=32, verbose_name="Registry Name")
	ip = models.CharField(max_length=32, verbose_name="Ip Adress")
	port = models.IntegerField(default=5000, verbose_name="Port")
	class Meta:
		verbose_name_plural = 'Registry'
	def __str__(self):
		return self.name			