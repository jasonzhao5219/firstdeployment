from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import course


def index(request):
	all_course=course.objects.all()
	
	context={
		'all_course':all_course
	}
	return render(request,"courses/index.html",context)

def add(request):


	errors = course.objects.basic_validator(request.POST)
	if len(errors):
		print errors
		for error in errors:
			messages.error(request, error)
		return redirect('/')

	else:
		if request.method == "POST":

			u1=course.objects.create(name=request.POST['name'],description=request.POST['discription'])
			return redirect('/')
		else:
			return redirect('/')



def delete(request,number):
	c1=course.objects.get(id=number)
	request.session['cid']=c1.id
	request.session['cname']=c1.name
	request.session['cdes']=c1.description
	return render(request,"courses/delete.html")

def destroy(request,number):
	c1=course.objects.get(id=number)

	c1.delete()
	return redirect('/')