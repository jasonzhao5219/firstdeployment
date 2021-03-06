from __future__ import unicode_literals
from django.db import models

class users(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __repr__(self):
		return  "<users object: {} {} {}  >".format(self.first_name, self.last_name, self.email)

class books(models.Model):
	name=models.CharField(max_length=255)
	desc=models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	uploader = models.ForeignKey(users, related_name="uploaded_books")
	liked_users=models.ManyToManyField(users, related_name="liked_books")
	def __repr__(self):
		return  "<books object: {} {}   >".format(self.name, self.desc)

