from django.db import models


class Product(models.Model):
	name = models.CharField(max_length=200, primary_key=True)
	image = models.CharField(max_length=200, null=False)
	price = models.CharField(max_length=200, null=False)
	discount = models.CharField(max_length=200, default='', blank=True)
	price_sale = models.CharField(max_length=200, default='', blank=True)

	def __str__(self):
		return f'{self.name}:{self.price}:{self.discount}:{self.price_sale}'