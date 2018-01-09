from swarm_ui.models import Product
from django.db.models import Count

class ProductApi():

	def fetchAll(self):
		list_prd = Product.objects.filter(status=1)
		return list_prd

	def listProduct(self):
		list_prd = Product.objects.filter(status=1).values("name").annotate(total=Count("name"))
		return list_prd
