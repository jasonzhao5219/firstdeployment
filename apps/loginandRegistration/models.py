from __future__ import unicode_literals
from django.db import models
import re
REGEX_email=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class userManager(models.Manager):
    def basic_validator(self, postData):
		errors = []
		
		if len(postData['firstname']) < 2 or len(postData['lastname']) < 2:
			
			errors.append("invalid firstname or lastname")
		
		if not postData['firstname'].isalpha() or not postData['lastname'].isalpha():
			errors.append("the name should ONLY contain alpha characters")

		if postData['password']!=postData['comfirm_password']:
			
			errors.append("The password is NOT Match")
		if not REGEX_email.match(postData['email']):
			errors.append("The email address is Not a legal one")
		return errors



class user(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password=models.CharField(max_length=255)
	objects = userManager()
	def __repr__(self):
		return  "<users object: {} {} {} {}   >".format(self.first_name, self.last_name,self.email,self.password)
