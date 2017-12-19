from __future__ import unicode_literals
from django.db import models
import re
REGEX_email=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class userManager(models.Manager):
    def basic_validator(self, postData):
		errors = []
		
		if len(postData['name']) < 1 or len(postData['alias']) < 1:
			
			errors.append("invalid firstname or lastname")
		
		if not postData['name'].isalpha() or not postData['alias'].isalpha():
			errors.append("the name should ONLY contain alpha characters")

		if postData['password']!=postData['comfirm_password']:
			
			errors.append("The password is NOT Match")
		if not REGEX_email.match(postData['email']):
			errors.append("The email address is Not a legal one")
		return errors

class quoteManager(models.Manager):
	def basic_validator(self, postData):
		errors = []
		if len(postData['firstname']) < 2 or len(postData['lastname']) < 2:
				
				errors.append("invalid firstname or lastname")
		return errors

class user(models.Model):
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password=models.CharField(max_length=255)
	birthdate = models.DateTimeField()
	objects = userManager()
	def __repr__(self):
		return  "<user object: {} {} {} {} {}  >".format(self.name, self.alias,self.email,self.password,self.birthdate)

class quote(models.Model):
	message=models.CharField(max_length=255)
	favorite=models.IntegerField(default='0')
	user = models.ForeignKey(user, related_name="quotes")

	objects = quoteManager()
	def __repr__(self):
		return "<travel object: {}  >".format(self.message)