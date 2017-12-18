from __future__ import unicode_literals
from django.db import models
class books(models.Model):
	name=models.CharField(max_length=255)
	desc=models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __repr__(self):
		return  "<books object: {} {}  >".format(self.name, self.desc)
class authors(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	notes=models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	books_id=models.ManyToManyField(books, related_name="authors")
	def __repr__(self):
		return  "<authors object: {} {} {} >".format(self.first_name, self.last_name,self.email)