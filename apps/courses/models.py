from __future__ import unicode_literals
from django.db import models





class courseManager(models.Manager):
    def basic_validator(self, postData):
		errors = []
		#error=False
		if len(postData['name']) < 5:
			print "lt 5 error"
			errors.append("Course name should be more than 5 characters")
			#error=True
		if len(postData['discription']) < 15:
			print "lt scrip error"
			errors.append("Course description should be more than 15 characters")
			#error=True
		return errors


class course(models.Model):
	name = models.CharField(max_length=255)
	description=models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	objects = courseManager()
	def __repr__(self):
		return  "<users object: {} {}   >".format(self.name, self.description)