from __future__ import unicode_literals
from django.db import models

class users(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	def __repr__(self):
		return  "<users object: {} {} {}  >".format(self.first_name, self.last_name, self.email)


