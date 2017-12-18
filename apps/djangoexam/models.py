from __future__ import unicode_literals
from django.db import models
import re
from datetime import datetime
from time import gmtime, strftime
REGEX_password=re.compile(r'[a-zA-Z]')

class userManager(models.Manager):
    def basic_validator(self, postData):
		errors = []
		
		if len(postData['name']) < 3 or len(postData['username']) < 3:
			
			errors.append("name and username should at least 3 characters")
		
		
		if postData['password']!=postData['comfirm_password']:
			
			errors.append("The password is NOT Match")
		if not REGEX_password.match(postData['password']):
			errors.append("The password  is Not a legal one")
		return errors

class travelManager(models.Manager):
	def basic_validator(self, postData):
		errors = []
				#strftime(" %B %d , %Y %H:%M  %p" , gmtime())
		timenow=gmtime()
		timenow=str(strftime("%Y %m %d ",timenow))
		print timenow>"2010 09 09 10:10"
		if len(postData['d1']) < 1 or len(postData['description']) < 1 or len(postData['startdate'])<1 or len(postData['enddate'])<1:
					
			errors.append("all input should at least 1 characters")
				
				 #time validation:
		if postData['startdate']>postData['enddate'] or postData['startdate']>timenow:
			errors.append("the start_date is not valid")

		return errors


class user(models.Model):
	name = models.CharField(max_length=255)
	user_name = models.CharField(max_length=255)
	
	password=models.CharField(max_length=255)
	objects = userManager()
	def __repr__(self):
		return  "<user object: {} {} {}    >".format(self.name, self.user_name,self.password)

class travel(models.Model):
	destination=models.CharField(max_length=255)
	description=models.CharField(max_length=255)
	
	start_date = models.DateTimeField()
	end_date= models.DateTimeField()
	users = models.ManyToManyField(user, related_name="travels")
	objects = travelManager()
	def __repr__(self):
		return  "<travel object: {} {} {}  {}  >".format(self.destination, self.description,self.start_date,self.end_date)