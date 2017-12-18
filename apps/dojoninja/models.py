from __future__ import unicode_literals
from django.db import models

class dojos(models.Model):
	name=models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	state=models.CharField(max_length=2)
	desc=models.TextField()
	def __repr__(self):
		return  "<dojos object: {} {} {} >".format(self.name, self.city, self.state)

class ninjas(models.Model):
	first_name=models.CharField(max_length=255)
	last_name=models.CharField(max_length=255)
	dojos = models.ForeignKey(dojos, related_name="ninjas")
	def __repr__(self):
		return  "<ninjas object: {} {} >".format(self.first_name, self.last_name)
