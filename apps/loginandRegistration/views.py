from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import user

def index(request):


	return render(request,"loginandregistration/index.html")

def process(request):
	errors = user.objects.basic_validator(request.POST)
	if len(errors):
		print errors
		for error in errors:
			messages.error(request, error)
		return redirect('/')

	else:
		if request.method == "POST":

			u1=user.objects.create(first_name=request.POST['firstname'],last_name=request.POST['lastname'],email=request.POST['email'],password=request.POST['password'])
			request.session['name']=u1.first_name
			return redirect('/suc')
		else:
			return redirect('/')

def login(request):
	u2=user.objects.filter(email = request.POST['email'],password=request.POST['password'])
	
	
	if len(u2)==1:
		request.session['uid']=u2[0].id
		request.session['name']=u2[0].first_name

		return redirect('/suc')
	else:
		return redirect('/')


def suc(request):

	return render(request,'loginandRegistration/suc.html')

