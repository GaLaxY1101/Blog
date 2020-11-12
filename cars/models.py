from django.db import models

TYPE_OF_BODY = [
	('SE', 'Sedan'),
	('MI', 'Micro'),
	('CU', 'Compact Utility Vehicle'),
	('SU', 'Sport Utility Vehicle'),
	('HA', 'Hatchback'),
	('MV', 'Minivan'),
	('CA', 'Cabriolet'),
	('CO', 'Coupe'),
	('RO', 'Roadster'),
	('SC', 'Sportcar'),
	('PU', 'Pickup')
	]

class Car(models.Model):
	make				= models.CharField(max_length= 60)
	model 				= models.CharField(max_length= 60)
	year				= models.IntegerField()
	type_of_body		= models.CharField(max_length= 2, choices = TYPE_OF_BODY)

	def __str__(self):
		return self.make

	class Meta:
		verbose_name = 'The car' #Единственное число
		verbose_name_plural = 'Cars' # Множественное число
